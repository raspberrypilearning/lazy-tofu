#!/usr/bin/env python3
"""Prepare the completed project while retaining the supplied starter unchanged."""

import argparse
import copy
import hashlib
import json
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[2]
COMPLETE = ROOT / "en/code/lazy-tofu-complete/lazy-tofu-complete.sb3"
STARTER = ROOT / "en/code/lazy-tofu-starter/lazy-tofu-starter.sb3"


def find_block(target, opcode, predicate=lambda block: True):
    matches = [
        (block_id, block)
        for block_id, block in target["blocks"].items()
        if block["opcode"] == opcode and predicate(block)
    ]
    if len(matches) != 1:
        raise ValueError(f"Expected one {opcode} on {target['name']}, got {len(matches)}")
    return matches[0]


def chain(target, ids):
    for index, block_id in enumerate(ids):
        block = target["blocks"][block_id]
        block["parent"] = ids[index - 1] if index else None
        block["next"] = ids[index + 1] if index + 1 < len(ids) else None


def make_block(opcode, **extra):
    return {
        "opcode": opcode,
        "next": None,
        "parent": None,
        "inputs": {},
        "fields": {},
        "shadow": False,
        "topLevel": False,
        **extra,
    }


def save_project(destination, project, assets):
    destination.parent.mkdir(parents=True, exist_ok=True)
    payloads = {"project.json": json.dumps(project, separators=(",", ":")).encode()}
    payloads.update(assets)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, payload in payloads.items():
            entry = zipfile.ZipInfo(name, date_time=(2026, 11, 9, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(entry, payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path, default=COMPLETE)
    parser.add_argument("--starter", type=Path, default=STARTER, help="Supplied starter to copy without modification")
    args = parser.parse_args()
    source = args.source
    starter_bytes = args.starter.read_bytes()
    with zipfile.ZipFile(args.starter) as archive:
        starter = json.loads(archive.read("project.json"))
    with zipfile.ZipFile(source) as archive:
        project = json.loads(archive.read("project.json"))
        assets = {name: archive.read(name) for name in archive.namelist() if name != "project.json"}
    original = copy.deepcopy(project)
    targets = {target["name"]: target for target in project["targets"]}
    stage, tofu = targets["Stage"], targets["Tofu"]
    variables = {value[0]: variable_id for variable_id, value in stage["variables"].items()}
    speed = variables["speed"]
    start_id = next(key for key, value in stage["broadcasts"].items() if value == "start")

    # Keep the existing gameplay graph, making only the documented setup changes.
    setup_id, _ = find_block(
        stage, "event_whenflagclicked",
        lambda block: stage["blocks"][block["next"]]["opcode"] == "data_setvariableto",
    )
    score_id, _ = find_block(stage, "data_setvariableto", lambda b: b["fields"]["VARIABLE"][0] == "score")
    health_id, _ = find_block(stage, "data_setvariableto", lambda b: b["fields"]["VARIABLE"][0] == "health")
    volume_id, volume = find_block(stage, "sound_setvolumeto")
    forever_id = volume["next"]
    stage["blocks"]["lazy-tofu-speed-reset"] = make_block(
        "data_setvariableto", inputs={"VALUE": [1, [4, "1"]]}, fields={"VARIABLE": ["speed", speed]},
    )
    chain(stage, [setup_id, "lazy-tofu-speed-reset", score_id, health_id, volume_id, forever_id])
    wait_id, wait = find_block(stage, "control_wait_until")
    stop_hat = stage["blocks"][wait["parent"]]
    stop_hat["opcode"] = "event_whenbroadcastreceived"
    stop_hat["fields"] = {"BROADCAST_OPTION": ["start", start_id]}
    for monitor in project["monitors"]:
        if monitor["params"].get("VARIABLE") == "speed":
            monitor["sliderMin"] = 1
            monitor["value"] = 1
    stage["variables"][speed][1] = 1
    stage["variables"][variables["score"]][1] = 0
    stage["variables"][variables["health"]][1] = 3

    flag_id, flag = find_block(tofu, "event_whenflagclicked")
    size_id, _ = find_block(tofu, "looks_setsizeto")
    position_id, _ = find_block(tofu, "motion_gotoxy", lambda b: b["inputs"]["X"][1] == [4, "-197"])
    direction_id, _ = find_block(tofu, "motion_pointindirection", lambda b: b["parent"] in (flag_id, size_id))
    costume_id, _ = find_block(
        tofu, "looks_switchcostumeto",
        lambda b: tofu["blocks"][b["inputs"]["COSTUME"][1]]["fields"]["COSTUME"][0] == "tofu-sleeping",
    )
    rest_id = tofu["blocks"][costume_id]["next"]
    awake_id = "lazy-tofu-awake"
    tofu["variables"][awake_id] = ["awake", 0]
    tofu["blocks"]["lazy-tofu-awake-reset"] = make_block(
        "data_setvariableto", inputs={"VALUE": [1, [4, "0"]]}, fields={"VARIABLE": ["awake", awake_id]},
    )
    tofu["blocks"]["lazy-tofu-wake-key"] = make_block(
        "event_whenkeypressed", fields={"KEY_OPTION": ["space", None]}, topLevel=True, x=520, y=0,
    )
    tofu["blocks"]["lazy-tofu-wake-set"] = make_block(
        "data_setvariableto", inputs={"VALUE": [1, [4, "1"]]}, fields={"VARIABLE": ["awake", awake_id]},
    )
    chain(tofu, ["lazy-tofu-wake-key", "lazy-tofu-wake-set"])
    old_condition = tofu["blocks"][rest_id]["inputs"]["CONDITION"][1]
    if tofu["blocks"][old_condition]["opcode"] == "sensing_keypressed":
        old_menu = tofu["blocks"][old_condition]["inputs"]["KEY_OPTION"][1]
        del tofu["blocks"][old_menu]
        del tofu["blocks"][old_condition]
    tofu["blocks"]["lazy-tofu-awake-check"] = make_block(
        "operator_equals", parent=rest_id,
        inputs={"OPERAND1": [3, [12, "awake", awake_id], [10, ""]], "OPERAND2": [1, [10, "1"]]},
    )
    tofu["blocks"][rest_id]["inputs"]["CONDITION"] = [2, "lazy-tofu-awake-check"]
    tofu["blocks"]["lazy-tofu-rotation-reset"] = make_block(
        "motion_setrotationstyle", fields={"STYLE": ["left-right", None]},
    )
    tofu["blocks"]["lazy-tofu-show"] = make_block("looks_show")
    chain(tofu, [flag_id, position_id, size_id, direction_id, "lazy-tofu-rotation-reset", "lazy-tofu-show", "lazy-tofu-awake-reset", costume_id, rest_id])
    # The repeat-until block continues into the original wake-up and jump sequence.
    tofu["blocks"][rest_id]["next"] = original["targets"][1]["blocks"][rest_id]["next"]
    tofu["size"] = 23

    for name in ("water-ripples", "objects"):
        for block in targets[name]["blocks"].values():
            if block["opcode"] == "operator_random" and block["inputs"] == {"FROM": [1, [4, "180"]], "TO": [1, [4, "-180"]]}:
                block["inputs"] = {"FROM": [1, [4, "-180"]], "TO": [1, [4, "180"]]}

    for name in ("grass-left", "grass-right"):
        for block in targets[name]["blocks"].values():
            if block["opcode"] == "operator_gt" and block["inputs"]["OPERAND2"] == [1, [10, "190"]]:
                block["inputs"]["OPERAND2"] = [1, [10, "180"]]

    for before, after in zip(original["targets"], project["targets"]):
        assert before["costumes"] == after["costumes"], before["name"]
        assert before["sounds"] == after["sounds"], before["name"]
    save_project(COMPLETE, project, assets)
    STARTER.write_bytes(starter_bytes)
    (ROOT / "en/resources/lazy-tofu-starter.sb3").write_bytes(starter_bytes)
    save_project(ROOT / "en/solutions/lazy-tofu-complete.sb3", project, assets)
    report = {
        "source_filename": source.name,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "starter_source_filename": args.starter.name,
        "starter_sha256": hashlib.sha256(starter_bytes).hexdigest(),
        "sprites": [t["name"] for t in project["targets"] if not t["isStage"]],
        "costumes_including_backdrop": sum(len(t["costumes"]) for t in project["targets"]),
        "sound_assignments": sum(len(t["sounds"]) for t in project["targets"]),
        "unique_assets": len(assets),
        "starter_blocks": sum(len(t["blocks"]) for t in starter["targets"]),
        "complete_blocks": sum(len(t["blocks"]) for t in project["targets"]),
        "all_costume_and_sound_records_preserved": True,
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

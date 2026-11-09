# Scratch version verification

Checked on 9 November 2026.

## Source checks passed

- All 13 section headings match `en/meta.yml`.
- The guide contains 46 task panels and 12 save panels.
- All 30 `blocks3` examples parse with scratchblocks 3.7.1: 231 blocks recognised, with no obsolete/unrecognised blocks.
- The introduction embeds completed Scratch project `1438005262` and links to its project page.
- The starter section embeds `1438003425`, links directly to its editor and explains remixing and saving to a computer.
- Both Scratch projects are shared and published by `RPiFoundation`, as confirmed through Scratch's public project API. Their sprite, costume and sound names match the guide.
- The sprite submission credit names Gabriella van Niekerk, Holy Cross Coding club and South Africa under ‘Your Club, Your Sprite’.
- All 11 local Markdown links resolve.
- The only image is the existing game banner copied unchanged from `editor-lazy-tofu`; no new screenshots or generated artwork were created.
- The starter and offline solution are unchanged from the editor repository, as are the matching downloads. The source preparation script was run successfully after adapting its paths.
- The supplied starter's SHA-256 remains `f8273e9d269e78a017a9151d5087cb29b45d96383f55ac23b6c9fd65b4570147`.
- The completed solution's SHA-256 remains `3ec61ef8291b0a9ea0203c2e4c11f4e687ad5152335b021f2bcee8af8a58409f`.
- Both project YAML files have matching directory/identifier/SB3 names and `build: true`.
- The guide has no `landing: true` and no directions assuming an editor is already open beside the instructions. The first step is **What you will make**.
- `listed` remains `false`.

## Verification scope

The offline completed game is byte-identical to the previously runtime-tested editor solution. The new checks cover the grouped Scratch tutorial, links, source preservation and metadata; they do not claim a new playtest of the two externally hosted Scratch projects.

After the site import, check the published content and ensure the backend's `editorStarterProject` is empty and `directToEditor` is false. A successful GitHub push alone does not establish this.

The 259-block offline solution retains the earlier reliability fixes. The supplied playable Scratch example has the original 254-block implementation; this known difference is recorded in the authoring notes.

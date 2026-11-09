# Scratch project-site authoring notes

## Scope and format

This is the separate `lazy-tofu` Scratch tutorial. Mark chose to keep `editor-lazy-tofu` unchanged alongside it, matching the relationship between `dino-jump` and `editor-dino-jump`.

The guide uses 13 grouped sections with the standard project site's task, save, no-print and print-only panels. It starts with **What you will make**, rather than an editor landing page. Learners open and remix the Scratch starter in a separate tab; there is no assumption that a Code Club Editor project is open beside the guide.

The two shared Scratch projects were verified through Scratch's public project API:

- Completed game: `1438005262`, titled `Lazy Tofu!`, published by `RPiFoundation`.
- Starter: `1438003425`, titled `Lazy Tofu! starter`, published by `RPiFoundation`.

Both are embedded with Scratch's project player, with direct links as an alternative. The starter page explains remixing for signed-in learners and saving to a computer without an account.

## Preserved decisions

- Audience: ages 10–14.
- All seven sprites, every costume, sound and implemented animation are retained.
- Build swimming and a playable river game before adding the full opening.
- Code left-bank foliage, copy both scripts to the existing right-hand sprite and explain the x-coordinate changes before testing.
- Keep the distinct right-hand overhanging-tree artwork.
- Preserve the submission credit for Gabriella van Niekerk, Holy Cross Coding club, South Africa, under ‘Your Club, Your Sprite’.
- Use the existing repository banner. No new screenshots or AI-generated images were made for this conversion.
- Keep `listed: false` until Mark requests otherwise.

## Source code and assets

The supplied starter SB3 is copied byte-for-byte from the editor repository. The offline completed project is also unchanged and retains the tested fixes from that version: deterministic setup, remembered wake-up keypress, safe positive speed values and reachable grass-clone cleanup.

The published Scratch completed game has the original 254-block implementation. The tutorial and offline solution retain the 259-block reliability revision already made for the editor guide; all gameplay features, animations and sounds remain. The externally supplied Scratch projects were not edited.

Code folders use the `lazy-tofu-starter` and `lazy-tofu-complete` identifiers. Both project YAML files retain `build: true`, as requested. Their `code_editor_scratch` build type creates the optional code artefacts; it does not choose the tutorial's presentation. Dino Jump's classic repository likewise builds a code-editor starter while presenting a normal Scratch tutorial.

For this project's site record, `editorStarterProject` must be empty and `directToEditor` must be false. The learner pages use the supplied Scratch links, not the optional code artefacts.

To synchronise the source archives and downloads:

```sh
python3 .github/authoring/prepare_projects.py
```

The script keeps the supplied starter unchanged. Keep all notes and tools inside `.github/authoring/`; extra top-level directories can be mistaken for locales by the site importer.

## Reference comparison

The comparison used `raspberrypilearning/dino-jump` at `867645b1ec78d7e6757e46b84a8d452f67c51979` and `raspberrypilearning/editor-dino-jump` at `5fe1f3cbae5733f006481657150097e9073b1449`.

The classic version has an introductory step, task panels and explicit Scratch-opening instructions. The editor version has `landing: true`, shorter micro-steps and an already-open editor. Those presentation differences informed this conversion; the earlier Lazy Tofu build order remains.

## Acceptance checks

- Match all headings and completion markers to the 13-section metadata.
- Parse and render each `blocks3` example.
- Check the completed and starter iframe URLs and the direct Scratch links.
- Check all local image and download links.
- Confirm the supplied starter and completed SB3 files remain unchanged.
- Verify the published site data has the intro as its first step, the two embeds and the full credit.
- Verify `editorStarterProject` is empty, `directToEditor` is false and the project remains unlisted.
- Preserve the existing editor repository and its live project.

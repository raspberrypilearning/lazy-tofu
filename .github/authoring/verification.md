# Scratch version verification

Checked on 9 November 2026.

## Source checks passed

- All 13 section headings match `en/meta.yml`.
- The guide contains 45 task panels and 12 save panels.
- All 29 current `blocks3` examples parse with scratchblocks 3.7.1: 227 blocks recognised, with no obsolete/unrecognised blocks.
- The introduction embeds completed Scratch project `1438005262` and links to its project page.
- The starter section embeds `1438003425`, links directly to its editor and explains remixing and saving to a computer.
- Both Scratch projects are shared and published by `RPiFoundation`, as confirmed through Scratch's public project API. Their sprite, costume and sound names match the guide.
- The sprite submission credit names Gabriella van Niekerk, Holy Cross Coding club and South Africa under ‘Your Club, Your Sprite’.
- All 11 local Markdown links resolve.
- The only image is the existing game banner copied unchanged from `editor-lazy-tofu`; no new screenshots or generated artwork were created.
- The starter and offline solution match the corresponding archives in the editor repository, as do the downloads. The source preparation script was run successfully with the updated sleeping sequence.
- The supplied starter's SHA-256 remains `f8273e9d269e78a017a9151d5087cb29b45d96383f55ac23b6c9fd65b4570147`.
- The updated completed solution's SHA-256 is `d96dc390cee7509de5f80f4d896e00fcfbde49096b974382260e310ec114c029`.
- Both project YAML files have matching directory/identifier/SB3 names and `build: true`.
- The guide has no `landing: true` and no directions assuming an editor is already open beside the instructions. The first step is **What you will make**.
- `listed` remains `false`.

## Verification scope

The offline completed game is byte-identical to the updated editor solution. Checks cover the grouped Scratch tutorial, links, source preservation, metadata and the four-breath animation logic; they do not claim a new visual or audio playtest of the externally hosted Scratch projects.

After the site import, check the published content and ensure the backend's `editorStarterProject` is empty and `directToEditor` is false. A successful GitHub push alone does not establish this.

The first import reported storage errors while fetching the template's zero-byte `.keep` files. Those placeholders were removed from the now-populated images, resources and solutions directories before retrying the import.

## Four-breath sleeping-animation update

Mark's updated `Lazy Tofu! (1).sb3` and shared Scratch project both use `repeat (4)` around the breathing animation, then `wait until <key (space) pressed?>` outside the loop. This guide and its completed archives now use the same sequence, with no `awake` variable or extra keypress script.

The source has 255 blocks; the offline solution has 258 after retaining the earlier setup and clone-cleanup fixes. All 33 asset files and all costume/sound records are preserved. The supplied starter remains unchanged.

A focused Scratch VM logic check confirmed four full cycles (40 growth and 40 shrink changes), a space-key wait after all four, the full wake/wave/waddle/jump/splash sequence after that keypress, and correct restart behaviour. No screenshots were generated.

The introductory making step now says “add the sleeping animation”.

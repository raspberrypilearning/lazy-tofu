## Grow grass on the banks

Reuse the tree-cloning pattern for smaller plants that appear more often, at different positions along each bank.

> [!TASK]
>
> Copy both scripts from **tree-left** to **grass-left**, then select **grass-left** to edit the copies.
>
> In the generator, add `go to back layer`{:class="block3looks"} after `hide`{:class="block3looks"}.
>
> Move the `go to x: () y: ()`{:class="block3motion"} block inside the forever loop, before creating a clone. Choose a random x from `-220` to `-180`, keeping y at `-200`.
>
> Change the wait to `0.5` divided by `speed`{:class="block3variables"}.
>
> ```blocks3
> when I receive [start v]
> hide
> go to [back v] layer
> forever
> go to x: (pick random (-220) to (-180)) y: (-200)
> create clone of (myself v)
> wait ((0.5) / (speed)) seconds
> end
> ```
>
> Choosing a position inside the loop gives each new plant its own spot.

> [!TASK]
>
> Grass has four costumes. In its clone script, change the random costume range to `1`–`4`.
>
> ```blocks3
> when I start as a clone
> switch costume to (pick random (1) to (4))
> show
> repeat until <(y position) > (180)>
> change y by (speed)
> end
> delete this clone
> ```
>
> **Test your project.** Tufts, flowers, reeds and bushes should move up the left bank, behind the trees.

> [!TASK]
>
> Copy both completed **grass-left** scripts to the existing **grass-right** sprite.
>
> Select **grass-right**. Change the random x range in its `go to`{:class="block3motion"} block from `-220`–`-180` to `180`–`220`.
>
> These positive numbers put the plants on the right bank. Keep y at `-200`, and leave the wait, costume range and clone movement unchanged.
>
> ```blocks3
> go to x: (pick random (180) to (220)) y: (-200)
> ```

> [!TASK]
>
> **Test your project.** Click the green flag. Plants should stay on the banks on both sides of the water.

> [!SAVE]

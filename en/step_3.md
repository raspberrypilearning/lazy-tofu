## Make Tofu swim

Start by getting Tofu swimming. You'll add the nap and the jump into the river later.

> [!TASK]
>
> Click on the `Tofu`{:class="block3looks"} sprite and add a script to set the starting position, size, direction and costume.
>
> ```blocks3
> when green flag clicked
> go to x: (0) y: (0)
> set size to (23) %
> point in direction (90)
> set rotation style [left-right v]
> show
> switch costume to (tofu v)
> ```
>
> **Test your project.** Click the green flag. Tofu moves into the middle of the river.

> [!TASK]
>
> Add a separate green-flag script with a `forever`{:class="block3control"} loop.
>
> Use `if then else`{:class="block3control"} to check the left arrow first. In its `else` section, check the right arrow. Set the direction and change x to move Tofu.
>
> ```blocks3
> when green flag clicked
> forever
> if <key (left arrow v) pressed?> then
> point in direction (-90)
> change x by (-10)
> else
> if <key (right arrow v) pressed?> then
> point in direction (90)
> change x by (10)
> end
> end
> end
> ```
>
> Negative x changes move left; positive changes move right. The `left-right` rotation style flips Tofu without turning the artwork upside down.

> [!TASK]
>
> Show the `tofu-swimming` costume during each stroke and start the `Plunge` sound.
>
> After each x change, grow Tofu by `2`, wait `0.1` seconds, then shrink by `2`. These changes balance, so Tofu returns to the same size.
>
> Change the right-arrow check to `if then else`{:class="block3control"} too. Its final `else` section should switch back to `tofu` when neither key is pressed.
>
> Your movement script should now look like this:
>
> ```blocks3
> when green flag clicked
> forever
> if <key (left arrow v) pressed?> then
> switch costume to (tofu-swimming v)
> start sound (Plunge v)
> point in direction (-90)
> change x by (-10)
> change size by (2)
> wait (0.1) seconds
> change size by (-2)
> else
> if <key (right arrow v) pressed?> then
> switch costume to (tofu-swimming v)
> start sound (Plunge v)
> point in direction (90)
> change x by (10)
> change size by (2)
> wait (0.1) seconds
> change size by (-2)
> else
> switch costume to (tofu v)
> end
> end
> end
> ```

> [!TASK]
>
> **Test your project.** Move Tofu left and right, then release the keys. Tofu faces the direction of travel, pulses and makes a sound while swimming, then returns to the resting pose.

> [!SAVE]

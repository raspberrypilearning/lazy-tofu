## Make the river scroll

Tofu will stay near the middle while trees move past. Use clones to make a stream of trees from each bank's sprite.

> [!TASK]
>
> Click on the **Stage**. Create a variable called `speed`{:class="block3variables"}, **For all sprites**, and untick its checkbox for now.
>
> Set speed to `1` on the green flag. Make a new message called `start` and broadcast it afterwards.
>
> ```blocks3
> when green flag clicked
> set [speed v] to (1)
> broadcast (start v)
> ```
>
> The Stage sets up the shared speed before telling the game to start.

> [!TASK]
>
> Click on **Tofu**. Replace the hat block on its movement loop with `when I receive (start)`{:class="block3events"}.
>
> Keep the separate starting-position script on the green flag.
>
> ```blocks3
> when I receive [start v]
> ```
>
> **Test your project.** Tofu should still move when you click the green flag and use the arrow keys.

> [!TASK]
>
> Click on `tree-left`{:class="block3looks"}. Hide the original sprite and put it just below the left bank. Make a clone every three seconds.
>
> ```blocks3
> when I receive [start v]
> hide
> go to x: (-180) y: (-200)
> forever
> create clone of (myself v)
> wait (3) seconds
> end
> ```

> [!TASK]
>
> Add a clone script. Pick one of the three tree costumes, show the clone and move it upwards by `speed`{:class="block3variables"} each time through the loop.
>
> Once its y position is greater than `180`, delete the clone to make room for new trees.
>
> ```blocks3
> when I start as a clone
> switch costume to (pick random (1) to (3))
> show
> repeat until <(y position) > (180)>
> change y by (speed)
> end
> delete this clone
> ```

> [!TASK]
>
> In the generator script, change the wait to a random number from `3` to `10`, divided by `speed`{:class="block3variables"}.
>
> ```blocks3
> wait ((pick random (3) to (10)) / (speed)) seconds
> ```
>
> A faster river will move the trees faster and create them more often, keeping the bank filled as it passes.
>
> **Test your project.** Trees should appear on the left bank, move upwards and disappear at the top, with different gaps between them.

> [!TASK]
>
> Copy both complete scripts from **tree-left** to the existing **tree-right** sprite by dragging each script's top block onto its sprite thumbnail.
>
> Select **tree-right** and change the x number in its `go to`{:class="block3motion"} block from `-180` to `180` **before testing**.
>
> Negative x positions are on the left; positive positions are on the right. Keep y at `-200` so trees on both banks enter at the same height.
>
> ```blocks3
> go to x: (180) y: (-200)
> ```
>
> The right-hand sprite already has the overhanging-tree artwork facing into the river. You only need to change that x number; keep the rest of both scripts.

> [!TASK]
>
> **Test your project.** Click the green flag. Trees travel along both banks, with water between them.

> [!SAVE]

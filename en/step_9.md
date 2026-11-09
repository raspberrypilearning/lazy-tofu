## Watch out for trees

Make the trees into obstacles, and stop the game when Tofu runs out of health.

> [!TASK]
>
> On **Tofu**, add another script for the `start` message.
>
> In a forever loop, check whether Tofu touches **tree-left** or **tree-right**. Use an `or`{:class="block3operators"} block to join the two checks.
>
> Start `Scream1`, send Tofu back to the middle and take away one health.
>
> ```blocks3
> when I receive [start v]
> forever
> if <<touching (tree-left v)?> or <touching (tree-right v)?>> then
> start sound (Scream1 v)
> go to x: (0) y: (0)
> change [health v] by (-1)
> end
> end
> ```
>
> Touching a sprite also checks its clones, so these two conditions cover every tree on both banks.

> [!TASK]
>
> On the **Stage**, add a script that starts on `start`, waits until health is less than `1`, then stops all scripts.
>
> ```blocks3
> when I receive [start v]
> wait until <(health) < (1)>
> stop [all v]
> ```
>
> The Stage resets health before broadcasting `start`, so the check always uses the current game's health.

> [!TASK]
>
> **Test your project.** Steer into a tree on each bank. Each collision should send Tofu to the middle and cost one health.
>
> When health reaches zero, Tofu and the river scenery should stop. Click the green flag to start a new game.

> [!SAVE]

## Collect food and dodge rubbish

Give the player a score to build and some health to protect.

> [!TASK]
>
> Click on the **Stage**. Create `score`{:class="block3variables"} and `health`{:class="block3variables"}, both **For all sprites**.
>
> Keep both checkboxes ticked so the player can see them. Drag their displays to clear spaces at the top of the Stage.
>
> In the Stage's green-flag script, set score to `0` and health to `3` before sending `start`.
>
> ```blocks3
> when green flag clicked
> set [speed v] to (1)
> set [score v] to (0)
> set [health v] to (3)
> broadcast (start v)
> ```

> [!TASK]
>
> Click on **objects** and find its movement script.
>
> Inside `repeat until`{:class="block3control"}, after the y change, check whether the clone is touching **Tofu**.
>
> Inside that check, use `if then else`{:class="block3control"} to check whether the costume number is less than `4`.
>
> Costumes `1`, `2` and `3` are food: add `5` to score, start `Chomp` and delete the clone. The other costumes are rubbish: take `1` from health, start `Scream1` and delete the clone.
>
> ```blocks3
> when I start as a clone
> switch costume to (pick random (1) to (6))
> show
> repeat until <(y position) > (180)>
> change y by (speed)
> if <touching (Tofu v)?> then
> if <(costume [number v]) < (4)> then
> change [score v] by (5)
> start sound (Chomp v)
> delete this clone
> else
> change [health v] by (-1)
> start sound (Scream1 v)
> delete this clone
> end
> end
> end
> delete this clone
> ```
>
> Keep the last `delete this clone`{:class="block3control"} outside the loop. It still removes objects that reach the top without touching Tofu.

> [!TASK]
>
> **Test your project.** Click the green flag and collect some food. Each piece should add `5` points and disappear.
>
> Touch some rubbish too. Each piece should disappear and take away one health, without adding points.
>
> The green flag resets both values. You'll add the game ending next.

> [!SAVE]

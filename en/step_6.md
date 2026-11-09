## Add river ripples

Make the water look as though it's flowing too, with ripples that drift and pulse.

> [!TASK]
>
> Copy both scripts from **grass-left** to **water-ripples**, then select **water-ripples**.
>
> In the generator, choose a random x from `-180` to `180`, between the two banks. Change the wait to a random number from `1` to `2`, divided by `speed`{:class="block3variables"}.
>
> ```blocks3
> when I receive [start v]
> hide
> go to [back v] layer
> forever
> go to x: (pick random (-180) to (180)) y: (-200)
> create clone of (myself v)
> wait ((pick random (1) to (2)) / (speed)) seconds
> end
> ```

> [!TASK]
>
> The ripple sprite has two costumes facing opposite ways. In the clone script, replace the random costume choice with an `if then else`{:class="block3control"} block.
>
> If x is less than `0`, the ripple is on the left: use `water-ripples2`. Otherwise, use `water-ripples`.
>
> ```blocks3
> when I start as a clone
> if <(x position) < (0)> then
> switch costume to (water-ripples2 v)
> else
> switch costume to (water-ripples v)
> end
> show
> repeat until <(y position) > (180)>
> change y by (speed)
> end
> delete this clone
> ```

> [!TASK]
>
> Add a second clone script. Grow the ripple by `5`, wait `0.1` seconds, then shrink it by `5` and wait again, repeating forever.
>
> ```blocks3
> when I start as a clone
> forever
> change size by (5)
> wait (0.1) seconds
> change size by (-5)
> wait (0.1) seconds
> end
> ```
>
> Both clone scripts run together: one moves the ripple and the other pulses its size. Deleting the clone stops both.

> [!TASK]
>
> **Test your project.** Ripples pulse and move through the river. Watch for the two different costumes on opposite sides.

> [!SAVE]

## Add music and choose the speed

Add the final sounds and give the player control of the river's speed.

> [!TASK]
>
> Click on the **Stage**. At the end of its green-flag setup, set the volume to `10%`, then add a forever loop.
>
> Inside the loop, play `Flowers Passing By` until done. Waiting for the track to finish lets it repeat from the beginning.
>
> ```blocks3
> when green flag clicked
> set [speed v] to (1)
> set [score v] to (0)
> set [health v] to (3)
> set volume to (10) %
> forever
> play sound (Flowers Passing By v) until done
> end
> ```
>
> This volume setting affects the Stage's sounds. Tofu and the objects keep their own sound volumes.

> [!TASK]
>
> On the **Stage**, add a separate space-key script for `Squeaky Toy`.
>
> ```blocks3
> when [space v] key pressed
> play sound (Squeaky Toy v) until done
> ```
>
> The squeak can play alongside Tofu's wake-up script and the background music.

> [!TASK]
>
> Tick the checkbox beside `speed`{:class="block3variables"} to show it on the Stage.
>
> Right-click its display and choose **slider**. Right-click again and choose **change slider range**. Set the minimum to `1` and the maximum to `20`.
>
> Keep the minimum above zero: the clone generators divide their waits by speed, so zero would not give them a usable interval.
>
> Move the slider to a clear space near the top of the Stage.

> [!TASK]
>
> **Test your project.** Click the green flag, wait for the four breaths, then press space to wake Tofu. Music should play during the sleeping animation and the game. Pressing space should squeak too.
>
> Start at speed `1`, then move the slider up a little. Plants, ripples and objects move faster, and appear more often. Choose a speed that gives you time to dodge and collect food.
>
> When health runs out, everything stops, including the music. The green flag resets score, health and speed for a new game.

> [!SAVE]

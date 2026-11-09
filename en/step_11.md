## Jump into the river

Finish the opening with a waddle, a jump and a splash.

> [!TASK]
>
> On **Tofu**, add these blocks after the wave sequence, before the final position change.
>
> Switch to `tofu-running` and allow full rotation. Repeat a pair of downward steps three times, leaning left and right as Tofu moves.
>
> ```blocks3
> switch costume to (tofu-running v)
> set rotation style [all around v]
> repeat (3)
> change y by (-10)
> turn ccw (15) degrees
> wait (0.2) seconds
> change y by (-10)
> turn cw (15) degrees
> wait (0.2) seconds
> end
> ```
>
> The two turns balance each other, so Tofu finishes facing the original direction.

> [!TASK]
>
> Replace the final `go to x: (0) y: (0)`{:class="block3motion"} in this opening script with a jump.
>
> Switch to `tofu-jumping`, return to `left-right` rotation, then glide through three positions to reach the middle of the river.
>
> ```blocks3
> switch costume to (tofu-jumping v)
> set rotation style [left-right v]
> glide (0.2) secs to x: (-149) y: (82)
> glide (0.2) secs to x: (-62) y: (69)
> glide (0.2) secs to x: (0) y: (0)
> ```

> [!TASK]
>
> After the last glide, before `broadcast (start)`{:class="block3events"}, start `Splash`, switch to the `splash` costume and wait a second.
>
> The end of the opening script should look like this:
>
> ```blocks3
> glide (0.2) secs to x: (0) y: (0)
> start sound (Splash v)
> switch costume to (splash v)
> wait (1) seconds
> broadcast (start v)
> ```
>
> The movement script chooses Tofu's next costume once it receives `start`.

> [!TASK]
>
> **Test your project.** Click the green flag and press space. Tofu wakes, waves, waddles down the bank, jumps and makes a splash. Swimming and scenery should begin after the splash.
>
> Try restarting during the animation too. Tofu should return to the sleeping position, size and rotation style.

> [!SAVE]

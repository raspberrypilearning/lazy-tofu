## Wake Tofu up

Your game works. Now add Tofu's nap and wave before the swimming begins.

> [!TASK]
>
> On **Tofu**, create a variable called `awake`{:class="block3variables"}, **For this sprite only**, and untick its checkbox.
>
> Use `0` for asleep and `1` for awake. Make a separate script to remember when the player presses space:
>
> ```blocks3
> when [space v] key pressed
> set [awake v] to (1)
> ```

> [!TASK]
>
> On the **Stage**, remove `broadcast (start)`{:class="block3events"} from the green-flag setup. Keep all three variable resets.
>
> On **Tofu**, change the green-flag starting-position script to the version below. Tofu starts asleep on the bank and sends `start` after waking and entering the river.
>
> ```blocks3
> when green flag clicked
> go to x: (-197) y: (107)
> set size to (23) %
> point in direction (90)
> set rotation style [left-right v]
> show
> set [awake v] to (0)
> switch costume to (tofu-sleeping v)
> wait until <(awake) = (1)>
> go to x: (0) y: (0)
> broadcast (start v)
> ```
>
> Keep both existing `when I receive (start)`{:class="block3events"} scripts on Tofu. They will start movement and collision checks once Tofu is in the river.
>
> **Test your project.** Click the green flag. Tofu waits on the bank and the river stays still. Press space to start the game.

> [!TASK]
>
> Replace the opening script's `wait until`{:class="block3control"} with a `repeat until`{:class="block3control"} loop, keeping the condition `awake = 1`.
>
> Start `Snoring`, then use two repeat loops to grow and shrink Tofu gently. Keep the position change and broadcast after the outer loop.
>
> ```blocks3
> repeat until <(awake) = (1)>
> start sound (Snoring v)
> repeat (10)
> wait (0.04) seconds
> change size by (1)
> end
> repeat (10)
> wait (0.04) seconds
> change size by (-1)
> end
> end
> ```
>
> Each breath adds ten to Tofu's size and takes ten away again. The separate key-press script remembers a quick press, so Tofu can finish the breath before waking.

> [!TASK]
>
> After the whole sleeping loop, before the final `go to x: (0) y: (0)`{:class="block3motion"}, add a wave.
>
> ```blocks3
> switch costume to (tofu v)
> wait (1) seconds
> start sound (Magic Spell v)
> switch costume to (tofu-waving v)
> wait (0.5) seconds
> switch costume to (tofu v)
> wait (0.5) seconds
> ```

> [!TASK]
>
> **Test your project.** Click the green flag. Tofu snores and breathes on the bank. Press space: Tofu finishes the breath, wakes, waves, then starts swimming.

> [!SAVE]

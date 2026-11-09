## Wake Tofu up

Your game works. Now add Tofu's sleeping animation and wave before the swimming begins.

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
> switch costume to (tofu-sleeping v)
> wait until <key (space v) pressed?>
> go to x: (0) y: (0)
> broadcast (start v)
> ```
>
> Keep both existing `when I receive (start)`{:class="block3events"} scripts on Tofu. They will start movement and collision checks once Tofu is in the river.
>
> **Test your project.** Click the green flag. Tofu waits on the bank and the river stays still. Press space to start the game.

> [!TASK]
>
> Add a `repeat (4)`{:class="block3control"} loop before the opening script's `wait until`{:class="block3control"} block.
>
> Inside it, start `Snoring`, then use two repeat loops to grow and shrink Tofu gently. Keep the space-key wait **outside and after** the outer loop, followed by the position change and broadcast.
>
> ```blocks3
> repeat (4)
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
> wait until <key (space v) pressed?>
> ```
>
> Each breath adds ten to Tofu's size and takes ten away again. Tofu completes all four breaths, then waits for the player to press space.

> [!TASK]
>
> After `wait until <key (space) pressed?>`{:class="block3control"}, before the final `go to x: (0) y: (0)`{:class="block3motion"}, add a wave.
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
> **Test your project.** Click the green flag. Tofu snores and takes four breaths, then waits on the bank. Press space after the breaths: Tofu wakes, waves, then starts swimming.

> [!SAVE]

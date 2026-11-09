## Float food and rubbish

Fill the river with things for Tofu to collect or avoid.

> [!TASK]
>
> Select **objects** and open its **Costumes** tab. The first three costumes are food: shrimp, snail and worm. The next three are rubbish: bottle, can and crisp packet.
>
> Keep them in this order. You'll use the costume number to tell food from rubbish.

> [!TASK]
>
> Go back to **Code**. Copy the generator and movement scripts from **water-ripples** to **objects**. Leave the size-changing script behind for now.
>
> The generator already picks positions in the river and waits between clones. Keep it as it is.
>
> In the movement script, remove the whole `if then else`{:class="block3control"} that chooses ripple costumes. Replace it with a costume block that picks a random number from `1` to `6`.
>
> ```blocks3
> when I start as a clone
> switch costume to (pick random (1) to (6))
> show
> repeat until <(y position) > (180)>
> change y by (speed)
> end
> delete this clone
> ```

> [!TASK]
>
> Give **objects** a second clone script to make the food and rubbish bob. You can copy the ripple's size-changing script and change both size values to `2` and `-2`.
>
> ```blocks3
> when I start as a clone
> forever
> change size by (2)
> wait (0.1) seconds
> change size by (-2)
> wait (0.1) seconds
> end
> ```

> [!TASK]
>
> **Test your project.** Food and rubbish should bob as they float through the water. They don't affect Tofu yet.

> [!SAVE]

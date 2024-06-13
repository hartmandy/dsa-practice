## Sort Colors

❔Given an array, colors, which contains a combination of the following three elements:

- 0 (representing red)
- 1 (representing white)
- 2 (representing blue)

Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue. To improve your problem-solving skills, do not utilize the built-in sort function.

```python
def sort_colors(colors):
    # one pointer at the start, one at the end, one moving through the list
    red, white, blue = 0, 0, len(colors)-1

    while (white <= blue):
    #if number is 0, it swaps to the left side of the list
        if colors[white] == 0:
            colors[white], colors[red] = colors[red], colors[white]
            white +=1
            red +=1
    # if number is 1, it's already in the middle, so continue through list
        elif colors[white] == 1:
            white +=1
    # if number is 2, it needs to go to the end
    # decrement blue(2), but don't move white(1)
        else:
            colors[white], colors[blue] = colors[blue], colors[white]
            blue -=1
    return colors
```

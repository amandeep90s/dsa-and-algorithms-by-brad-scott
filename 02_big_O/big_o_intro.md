# Big O, Time Complexity, and Space Complexity

**Big O** describes how an algorithm’s resource needs grow as the amount of input grows. It helps us compare algorithms without relying on a particular computer’s speed. Big O is written with the letter **O**, not the number zero.

## Time complexity

**Time complexity** describes how the amount of work an algorithm does grows as its input gets bigger. It doesn’t tell us the exact number of seconds; it gives us a general idea of how the work increases.

Imagine looking for a name in a list:

- **O(1) — constant time:** The amount of work stays about the same, no matter how large the list is. For example, looking up an item directly by its position.
- **O(n) — linear time:** If the list gets twice as long, the work may take about twice as long. For example, checking names one by one.
- **O(n²) — quadratic time:** If the list gets twice as long, the work may grow to about four times as much. This can happen when each item is compared with every other item.
- **O(log n) — logarithmic time:** The work grows slowly because the problem is repeatedly cut into smaller pieces. For example, searching a sorted list by repeatedly checking the middle.

Here, **n** means the amount of input—for example, the number of names in a list.

## Space complexity

**Space complexity** describes how much extra memory an algorithm needs as its input gets bigger.

For example, an algorithm that checks a list using only a few temporary values uses about **O(1)** extra space. An algorithm that creates a second list containing one item for every input item uses about **O(n)** extra space.

In short:

- **Time complexity:** How the work grows.
- **Space complexity:** How the extra memory grows.
- **Big O:** A way to describe that growth.

# Big O, Time Complexity, and Space Complexity

Imagine searching for a name in a list. With a short list, it is quick. With a long list, it may take more work.

**Time complexity** describes how the work grows as the list gets bigger. It does not tell you the exact number of seconds. **Space complexity** describes how much extra memory the algorithm needs.

In these examples, **n** means the number of names in the list.

## Common time complexities

- **O(1) — constant:** The work stays about the same, even if the list gets bigger. Example: go straight to the name at a known position. (Constant)
- **O(n) — linear:** You may check each name once. If the list doubles in size, you may do about twice as much work. (Divide and Conquer)
- **O(n²) — quadratic:** Each name gets compared with every other name. If the list doubles, the work may become about four times as much. (Proportial - straight line)
- **O(log n) — logarithmic:** Each check cuts the remaining search in half. Example: find a name in an alphabetically sorted list by repeatedly checking the middle. (Loop within a loop)

## O, Ω, Θ, and little o

These symbols describe and compare how the work grows for large lists:

- **O (Big O):** An upper limit on how quickly the work grows. For example, checking names one by one takes **O(n)** work: the amount of work grows no faster than the size of the list.
- **Ω (Big Omega):** A lower limit on how quickly the work grows. If you must check every name, the work is **Ω(n)**: a longer list requires at least that much checking.
- **Θ (Big Theta):** A close match: both the upper and lower limits grow at the same rate. If you always check every name, the work is **Θ(n)**.
- **o (little o):** The work grows more slowly than the comparison rate. For example, checking one name per list item is **o(n²)**: it grows slower than comparing every pair of names.

For a simple search that checks each name one by one, the work is **O(n)** and **Ω(n)**, so it is also **Θ(n)**. It is **o(n²)** because checking one name at a time grows more slowly than comparing every pair.

## Space complexity examples

- **O(1) extra space:** Keep track of just the current name while searching.
- **O(n) extra space:** Make a new list that stores one extra item for every name in the original list.

**In short:** time complexity is how the work grows; space complexity is how extra memory grows. Big O notation helps describe that growth. O is the letter “O,” not the number zero.

[https://www.bigocheatsheet.com/](https://www.bigocheatsheet.com/)

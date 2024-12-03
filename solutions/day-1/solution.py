"""
Your analysis only confirmed what everyone feared: the two lists of location IDs are indeed very different.

Or are they?

The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting, but in the commotion you notice an interesting detail: a lot of location IDs appear in both lists! Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3

For these example lists, here is the process of finding the similarity score:

    The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
    The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
    The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
    The fourth number, 1, also does not appear in the right list.
    The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
    The last number, 3, appears in the right list three times; the similarity score again increases by 9.

So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).
"""

from collections import Counter


def get_input_lines(use_example: bool) -> list[str]:
    if use_example:
        filename = "example.txt"
    else:
        filename = "input.txt"
    with open(filename) as f:
        return f.readlines()


def main(use_example: bool) -> None:
    lines = get_input_lines(use_example)

    def get_col(index: int) -> list[int]:
        return sorted([int(line.split()[index]) for line in lines])

    left_col = get_col(0)
    right_col = get_col(1)

    total_distance = sum(abs(l - r) for l, r in zip(left_col, right_col))
    print(f"total distance: {total_distance}")
    right_counts = Counter(right_col)
    similarity_score = sum(l * right_counts[l] for l in left_col)
    print(f"similarity score: {similarity_score}")


if __name__ == "__main__":
    main(use_example=False)

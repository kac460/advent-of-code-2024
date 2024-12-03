"""
The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
--- Part Two ---

The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""


def get_input_lines(use_example: bool) -> list[str]:
    if use_example:
        filename = "example.txt"
    else:
        filename = "input.txt"
    with open(filename) as f:
        return f.readlines()


def get_levels(report_line: str) -> list[int]:
    return [int(level) for level in report_line.split()]


def is_safe(report_levels: list[int]) -> bool:
    if len(report_levels) == 0:
        raise ValueError(f"levels resulted has 0 levels")
    if len(report_levels) == 1:
        print(f"{report_levels} has only 1 level and so is safe")
        return True
    if report_levels[0] == report_levels[1]:
        # No non-changes
        return False
    elif report_levels[0] < report_levels[1]:
        # Increasing
        inc_or_dec = lambda i: report_levels[i] < report_levels[i + 1]
    else:
        # Decreasing
        inc_or_dec = lambda i: report_levels[i] > report_levels[i + 1]
    # Don't need to check indexes 0 and 1
    # Go up to i=2nd to last index
    for i in range(len(report_levels) - 1):
        if not inc_or_dec(i):
            return False
        # Don't need at least 1 diff check bc we know it's either inc or dec
        if abs(report_levels[i] - report_levels[i + 1]) > 3:
            return False
    return True


def is_safe_with_dampener(report_levels: list[int]) -> bool:
    if is_safe(report_levels):
        return True
    # Pops at the end are better performance-wise
    # So try to return True sooner from the end
    for i in reversed(range(len(report_levels))):
        report_levels_copy = report_levels.copy()
        report_levels_copy.pop(i)
        if is_safe(report_levels_copy):
            return True
    return False


def main() -> None:
    lines = get_input_lines(use_example=False)
    reports = [get_levels(line) for line in lines]
    safe_reports = [
        report_levels for report_levels in reports if is_safe(report_levels)
    ]
    print(f"Num safe reports: {len(safe_reports)}")

    safe_reports_with_dampener = [
        report_levels
        for report_levels in reports
        if is_safe_with_dampener(report_levels)
    ]
    print(f"Num safe reports with dampener: {len(safe_reports_with_dampener)}")


if __name__ == "__main__":
    main()

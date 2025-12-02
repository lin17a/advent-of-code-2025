import re
from pathlib import Path

# invalid IDs made only of some sequence of digits repeated twice (Part A)
PART_A_ID_REGEX = re.compile(r"^(?P<seq>\d+)(?P=seq)$")
# invalid IDs made only of some sequence of digits repeated at least twice (Part B)
PART_B_ID_REGEX = re.compile(r"^(?P<seq>\d+)(?P=seq)+$")


def is_invalid_id(id: int, id_regex: re.Pattern) -> bool:
    """check if the given ID is invalid based on the given regex pattern

    Args:
        id (int): ID to be checked
        id_regex (re.Pattern): regular expression that the ID has to match

    Returns:
        bool: if the ID is invalid
    """
    return bool(id_regex.fullmatch(str(id)))


def find_invalid_ids_in_range(
    range_start: int, range_end: int, id_regex: re.Pattern
) -> list[int]:
    """find all invalid IDs in the given range

    Args:
        range_start (int): beginning of the range
        range_end (int): end of the range (included)
        id_regex (re.Pattern): regex to validate the IDs

    Returns:
        list[int]: list of the invalid IDs
    """
    invalid_ids = []

    for i in range(range_start, range_end + 1):
        if is_invalid_id(i, id_regex):
            invalid_ids.append(i)

    return invalid_ids


def get_invalid_id_sum(input_ranges_str: str, id_regex: re.Pattern) -> int:
    """get the sum of invalid IDs in the input

    Args:
        input_ranges_str (str): input string with comma-separated ranges to check
        id_regex (re.Pattern): regex to validate the IDs

    Returns:
        int: sum of the invalid IDs
    """
    ranges = input_ranges_str.split(",")

    invalid_ids = []

    for r in ranges:
        range_start, range_end = map(int, r.split("-"))

        invalid_ids.extend(find_invalid_ids_in_range(range_start, range_end, id_regex))

    invalid_id_sum = sum(invalid_ids)

    return invalid_id_sum


def main():
    input_path = Path("./Day_02/input.txt")

    with open(input_path) as file:
        input_ranges_str = file.read()

    invalid_id_sum_part_a = get_invalid_id_sum(input_ranges_str, PART_A_ID_REGEX)
    print(f"Sum of invalid IDs (Part A): {invalid_id_sum_part_a}")

    invalid_id_sum_part_b = get_invalid_id_sum(input_ranges_str, PART_B_ID_REGEX)
    print(f"Sum of invalid IDs (Part B): {invalid_id_sum_part_b}")


if __name__ == "__main__":
    main()

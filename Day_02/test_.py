import pytest

from Day_02.main import (
    PART_A_ID_REGEX,
    PART_B_ID_REGEX,
    get_invalid_id_sum,
    is_invalid_id,
)


@pytest.mark.parametrize(
    "id, expected",
    [
        (1, False),
        (100, False),
        (3355, False),
        (121212, False),
        (1212, True),
        (566566, True),
        (77, True),
        (999999, True),
    ],
)
def test_id_validation_part_a(id, expected):
    assert is_invalid_id(id, PART_A_ID_REGEX) == expected


@pytest.mark.parametrize(
    "id, expected",
    [
        (1, False),
        (100, False),
        (3355, False),
        (121212, True),
        (1111111, True),
        (12341234, True),
        (1212121212, True),
        (1212, True),
        (566566, True),
        (77, True),
        (999999, True),
    ],
)
def test_id_validation_part_b(id, expected):
    assert is_invalid_id(id, PART_B_ID_REGEX) == expected


def write_file(tmp_path, content: str):
    file = tmp_path / "input.txt"
    file.write_text(content)
    return file


def test_get_invalid_id_sum(tmp_path):
    """Test with example input."""
    input_path = write_file(
        tmp_path,
        """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
""",
    )
    with open(input_path) as file:
        input_ranges_str = file.read()

    invalid_id_sum = get_invalid_id_sum(input_ranges_str, PART_A_ID_REGEX)
    assert invalid_id_sum == 1227775554

    invalid_id_sum = get_invalid_id_sum(input_ranges_str, PART_B_ID_REGEX)
    assert invalid_id_sum == 4174379265

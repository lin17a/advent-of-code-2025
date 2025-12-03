import pytest

from Day_03.main import (
    get_max_joltage,
    get_max_joltage_for_bank_part_1,
    get_max_joltage_for_bank_part_2,
)


@pytest.mark.parametrize(
    "bank, expected",
    [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
        (
            "2232546378857275787561723292343835435343333776427842773354273372424413455462238746648634437374254318",
            98,
        ),
    ],
)
def test_max_joltage_per_bank_part1(bank, expected):
    bank_int = list(map(int, list(bank)))
    assert get_max_joltage_for_bank_part_1(bank_int) == expected


@pytest.mark.parametrize(
    "bank, expected",
    [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ],
)
def test_max_joltage_per_bank_part2(bank, expected):
    bank_int = list(map(int, list(bank)))
    assert get_max_joltage_for_bank_part_2(bank_int) == expected


def write_file(tmp_path, content: str):
    file = tmp_path / "input.txt"
    file.write_text(content)
    return file


def test_get_password(tmp_path):
    """Test with example input."""
    input_path = write_file(
        tmp_path,
        """987654321111111
811111111111119
234234234234278
818181911112111
""",
    )

    with open(input_path) as file:
        banks = file.readlines()

    max_joltage_part1 = get_max_joltage(banks, get_max_joltage_for_bank_part_1)
    assert max_joltage_part1 == 357

    max_joltage_part2 = get_max_joltage(banks, get_max_joltage_for_bank_part_2)
    assert max_joltage_part2 == 3121910778619

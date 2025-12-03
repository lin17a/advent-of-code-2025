from collections.abc import Callable
from pathlib import Path


def get_max_joltage_for_bank_part_1(bank: list[int]) -> int:
    """get the maximum possible joltage when turning on two batteries in the bank

    Args:
        bank (list[int]): joltage values per battery

    Returns:
        int: maximum possible joltage
    """
    max_joltage = bank[0]
    max_joltage_2 = bank[1]

    bank_len = len(bank)

    for i in range(1, bank_len):
        if bank[i] > max_joltage and i < bank_len - 1:
            max_joltage = bank[i]
            max_joltage_2 = bank[i + 1]

        elif bank[i] > max_joltage_2:
            max_joltage_2 = bank[i]

    combined_joltage = 10 * max_joltage + max_joltage_2

    return combined_joltage


def get_combined_joltage(joltages: list[int]) -> int:
    """get the combined joltage for the joltage list

    Args:
        joltages (list[int]): list of the joltages

    Returns:
        int: combined joltage
    """
    return sum([j * 10 ** (len(joltages) - 1 - i) for i, j in enumerate(joltages)])


def get_first_max_and_idx(jolt_list: list[int]) -> tuple[int, int]:
    """get the first maximum value in the given list and the corresponding index

    Args:
        jolt_list (list[int]): list of joltages

    Returns:
        tuple[int, int]: maximum value, index of maximum value
    """
    idx, val = max(enumerate(jolt_list), key=lambda x: x[1])
    return val, idx


def get_max_joltage_for_bank_part_2(bank: list[int]) -> int:
    """get the maximum possible joltage when combining 12 batteries in one bank

    Args:
        bank (list[int]): joltage values of each battery

    Returns:
        int: maximum possible joltage value for the bank
    """
    bank_len = len(bank)
    num_active_bat = 12
    active_bat = []
    start_idx = 0

    for i in range(12):
        end_idx = bank_len - (num_active_bat - 1 - i)
        window = bank[start_idx:end_idx]

        max_jolt, idx = get_first_max_and_idx(window)
        active_bat.append(max_jolt)

        start_idx += idx + 1

    combined_joltage = get_combined_joltage(active_bat)

    return combined_joltage


def get_max_joltage(banks: list[str], max_jolt_func: Callable[[list[int]], int]):
    """get the sum of maximum possible voltage per battery bank based on the the max_jolt_func

    Args:
        banks (list[str]): list with battery bank joltage values as string
        max_jolt_func (Callable[[list[int]], int]): function to calculate the maxium possible joltage per battery bank

    Returns:
        int: maximum possible joltage
    """
    max_joltage = 0

    for bank in banks:
        joltages = list(map(int, list(bank.strip())))
        max_joltage += max_jolt_func(joltages)

    return max_joltage


def main():
    """get the maximum possible joltage in the battery banks"""
    input_path = Path("./Day_03/input.txt")

    with open(input_path) as file:
        banks = file.readlines()

    max_joltage_part1 = get_max_joltage(banks, get_max_joltage_for_bank_part_1)

    max_joltage_part2 = get_max_joltage(banks, get_max_joltage_for_bank_part_2)

    print(f"Maximum possible joltage for part1 is {max_joltage_part1}.")
    print(f"Maximum possible joltage for part2 is {max_joltage_part2}.")


if __name__ == "__main__":
    main()

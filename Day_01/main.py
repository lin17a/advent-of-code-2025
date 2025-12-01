import re
from pathlib import Path
from typing import Tuple

INSTRUCTION_REGEX = re.compile(r"^(?P<dir>[LR])(?P<step>\d+)$")


def interpret_instruction(instruction: str) -> Tuple[str, int]:
    """interpret instruction

    Args:
        instruction (str): instruction of the form '<[LR]>\\d+'

    Raises:
        ValueError: if instruction does not fit the format

    Returns:
        Tuple[str, int]: direction (L or R), number of steps
    """
    match = INSTRUCTION_REGEX.fullmatch(instruction)
    if match:
        direction = match.groupdict()["dir"]
        step = int(match.groupdict()["step"])
    else:
        raise ValueError(
            f"The instruction format has to be of the form: '<[LR]>\\d+', but was {instruction!r}"
        )

    return direction, step


def get_password(instructions: list[str], start_pos: int) -> Tuple[int, int]:
    """get the passwords: number of times the dial stops at zero and number of times the dial crosses zero

    Args:
        instructions (list[str]): list of instructions
        start_pos (int): starting position

    Raises:
        ValueError: if the direction is not L or R

    Returns:
        Tuple[int, int]: number of times the dial stops at zero, number of times the dial crosses zero
    """
    cur_pos = start_pos
    num_zero_pointings = 0
    num_zero_crossings = 0

    for line in instructions:
        direction, step = interpret_instruction(line.strip())

        if direction == "L":
            interim = cur_pos - step
            # if old position is 0, one zero-crossing less
            if cur_pos == 0:
                num_zero_crossings -= 1
            cur_pos = interim % 100
            # if new position is 0, one zero-crossing more
            if cur_pos == 0:
                num_zero_crossings += 1
        elif direction == "R":
            interim = cur_pos + step
            cur_pos = interim % 100
        else:
            raise ValueError(
                f"Direction in the instruction has to be L or R but was {direction}."
            )

        num_zero_crossings += abs(interim // 100)

        assert cur_pos >= 0 and cur_pos < 100, (
            f"Positions have to be between 0 and 99, but it is {cur_pos}."
        )

        if cur_pos == 0:
            num_zero_pointings += 1

    return num_zero_pointings, num_zero_crossings


def main():
    """get the password open the doorf to the North Pole"""
    input_path = Path("./Day_01/input.txt")

    with open(input_path) as file:
        instructions = file.readlines()

    start_pos = 50

    num_zero_pointings, num_zero_crossings = get_password(instructions, start_pos)

    print(f"Number of times dial is pointing at zero: {num_zero_pointings}")
    print(f"Number of times dial is crossing zero: {num_zero_crossings}")


if __name__ == "__main__":
    main()

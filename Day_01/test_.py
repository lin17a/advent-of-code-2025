import pytest

from Day_01.main import get_password, interpret_instruction


@pytest.mark.parametrize(
    "instruction, expected",
    [
        ("L3", ("L", 3)),
        ("R100", ("R", 100)),
        ("L42", ("L", 42)),
        ("R1", ("R", 1)),
    ],
)
def test_known_instructions(instruction, expected):
    """Test instruction parsing.

    Args:
        instruction (str): instruction
        expected (str, int): corresponding instruction
    """
    assert interpret_instruction(instruction) == expected


@pytest.mark.parametrize("invalid", ["", "LL5", "S42", "hello", "123"])
def test_invalid_instructions(invalid):
    """Test invalid instructions.

    Args:
        invalid (str): invalid instruction
    """
    with pytest.raises(ValueError):
        interpret_instruction(invalid)


def write_file(tmp_path, content: str):
    file = tmp_path / "input.txt"
    file.write_text(content)
    return file


def test_get_password(tmp_path):
    """Test with example input."""
    input_path = write_file(
        tmp_path,
        """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""",
    )
    with open(input_path) as file:
        instructions = file.readlines()

    num_zero_pointings, num_zero_crossings = get_password(instructions, start_pos=50)

    assert num_zero_pointings == 3
    assert num_zero_crossings == 6

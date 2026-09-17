import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent)
)

from app import calculate_total, calculate_average, get_result


def test_total():
    marks = [80, 70, 90]
    assert calculate_total(marks) == 240


def test_average():
    marks = [80, 70, 90]
    assert calculate_average(marks) == 80


def test_result():
    assert get_result(80) == "PASS"
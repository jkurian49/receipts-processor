from app.utils import (
    calculate_retailer_points,
    calculate_total_points,
    calculate_items_points,
    calculate_day_points,
    calculate_time_points,
)

def test_calculate_retailer_points():
    assert calculate_retailer_points("Target") == 6  # 6 alphabetic chars
    assert calculate_retailer_points("123") == 0
    assert calculate_retailer_points("A1B2C3") == 3  # 3 alphabetic chars

def test_calculate_total_points():
    # round dollar, multiple of 0.25
    assert calculate_total_points("20.00") == 75  # 50 + 25
    # not round, but multiple of 0.25
    assert calculate_total_points("20.25") == 25
    # not round, not multiple of 0.25
    assert calculate_total_points("20.10") == 0

def test_calculate_items_points():
    items = [
        {"shortDescription": "abc", "price": "5.00"},    # len=3, triggers bonus: ceil(5*0.2)=1
        {"shortDescription": "abcd", "price": "2.00"},   # len=4, no bonus
        {"shortDescription": "abcdef", "price": "3.00"}, # len=6, triggers bonus: ceil(3*0.2)=1
    ]
    # 3 items: 1 pair = 5 points, 2 description bonuses = 2 points
    assert calculate_items_points(items) == 7

def test_calculate_day_points():
    assert calculate_day_points("2022-01-01") == 6  # odd day
    assert calculate_day_points("2022-01-02") == 0  # even day

def test_calculate_time_points():
    assert calculate_time_points("15:00") == 10  # within bonus window
    assert calculate_time_points("13:59") == 0  # before window
    assert calculate_time_points("16:01") == 0  # after window

import math
from app.constants import *

def calculate_retailer_points(retailer: str) -> int:
    return sum(RETAILER_MULTIPLIER for char in retailer if char.isalpha())

def calculate_total_points(total: str) -> int:
    points = 0
    total = float(total)
    if total % 1 == 0:
        points += TOTAL_ROUND_DOLLAR_BONUS
    if total % 0.25 == 0:
        points += TOTAL_MULTIPLE_OF_25_BONUS
    return points

def calculate_items_points(items: list) -> int:
    points = 0
    points += PER_2_ITEMS_BONUS * (len(items) // 2)
    for item in items:
        if len(item['shortDescription'].strip()) % 3 == 0:
            points += math.ceil(float(item['price']) * PRICE_MULTIPLIER)
    return points

def calculate_day_points(purchase_date: str) -> int:
    points = 0
    day = int(purchase_date[-2:])
    if day % 2 != 0:
        points += ODD_DAY_BONUS
    return points

def calculate_time_points(purchase_time: str) -> int:
    points = 0
    hour, minute = map(int, purchase_time.split(":"))
    total_minutes = hour * 60 + minute
    lower_bound = TIME_BONUS_BOUNDS[0] * 60  # e.g., 14*60 = 840
    upper_bound = TIME_BONUS_BOUNDS[1] * 60  # e.g., 16*60 = 960
    if lower_bound < total_minutes < upper_bound:
        points += TIME_BONUS
    return points
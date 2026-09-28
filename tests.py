from calculator import calculate_water_use
from analyzer import classify_usage, find_highest_use

def test_calculation():
    data = {
        "bathing": 10, "tap": 5, "toilet": 4,
        "laundry": 1, "dishes": 5, "drinking": 3
    }
    result = calculate_water_use(data)
    expected = 10*9 + 5*6 + 4*6 + 1*60 + 5*8 + 3
    assert result["total"] == expected

def test_classification():
    assert classify_usage(200) == "Low"
    assert classify_usage(300) == "Moderate"
    assert classify_usage(600) == "High"

def test_highest_activity():
    usage = {
        "bathing": 90, "tap": 20, "toilet": 24,
        "laundry": 60, "dishes": 16, "drinking": 3,
        "total": 213
    }
    assert find_highest_use(usage) == "bathing"

print("Running Water Footprint tests...")
test_calculation()
test_classification()
test_highest_activity()
print("All tests passed.")

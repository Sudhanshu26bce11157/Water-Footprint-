from data import WATER_FACTORS

def calculate_water_use(data):
    result = {}

    for activity, amount in data.items():
        result[activity] = round(amount * WATER_FACTORS[activity], 2)

    result["total"] = round(sum(result.values()), 2)
    return result

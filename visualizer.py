from data import ACTIVITY_NAMES

def show_summary(usage, level, highest):
    print("\n" + "-" * 55)
    print(f"Estimated direct water use : {usage['total']:.1f} litres/day")
    print(f"Project usage category     : {level}")
    if highest:
        print(f"Largest part of your use  : {ACTIVITY_NAMES[highest]}")
    print("-" * 55)

def show_bars(usage):
    print("\nWater-use breakdown")
    values = {k: v for k, v in usage.items() if k != "total"}
    maximum = max(values.values()) if values else 0

    for key, value in values.items():
        length = int((value / maximum) * 25) if maximum else 0
        print(f"{ACTIVITY_NAMES[key]:12} | {'#' * length:<25} {value:.1f} L")

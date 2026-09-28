from input_handler import get_user_data
from calculator import calculate_water_use
from analyzer import classify_usage, find_highest_use
from visualizer import show_summary, show_bars
from tips import get_tips

def main():
    print("\n" + "=" * 55)
    print("             WATER FOOTPRINT CHECK")
    print("=" * 55)
    print("A small project to estimate everyday direct water use.\n")

    data = get_user_data()
    usage = calculate_water_use(data)
    level = classify_usage(usage["total"])
    highest = find_highest_use(usage)

    show_summary(usage, level, highest)
    show_bars(usage)

    print("\nA few things you can try:")
    for tip in get_tips(data, highest):
        print(" - " + tip)

    print("\nThanks for using the Water Footprint Check!")

if __name__ == "__main__":
    main()

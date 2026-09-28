def read_number(message):
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Please enter 0 or a positive number.")
            else:
                return value
        except ValueError:
            print("Please enter a number, such as 10 or 2.5.")

def get_user_data():
    print("Enter your approximate daily usage.\n")
    return {
        "bathing": read_number("Bath/shower time (minutes): "),
        "tap": read_number("Tap use (minutes): "),
        "toilet": read_number("Toilet flushes: "),
        "laundry": read_number("Washing-machine loads: "),
        "dishes": read_number("Dish washing (minutes): "),
        "drinking": read_number("Drinking water (litres): ")
    }

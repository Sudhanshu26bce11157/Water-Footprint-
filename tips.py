def get_tips(data, highest):
    tips = []

    tips_by_activity = {
        "bathing": "Try cutting a few minutes from your bath or shower.",
        "tap": "Turn off the tap when water is not needed.",
        "toilet": "Avoid unnecessary flushing.",
        "laundry": "Run the washing machine with a fuller load.",
        "dishes": "Do not leave the tap running continuously while washing dishes.",
        "drinking": "Take only the drinking water you expect to finish."
    }

    if highest in tips_by_activity:
        tips.append(tips_by_activity[highest])

    if data["laundry"] > 1:
        tips.append("Try combining laundry into fuller loads.")

    if not tips:
        tips.append("Keep avoiding unnecessary water use.")

    return tips[:3]

def classify_usage(total):
    # Simple categories created for this educational project.
    if total < 250:
        return "Low"
    elif total < 500:
        return "Moderate"
    else:
        return "High"

def find_highest_use(usage):
    activities = {key: value for key, value in usage.items()
                  if key != "total"}
    return max(activities, key=activities.get) if activities else None

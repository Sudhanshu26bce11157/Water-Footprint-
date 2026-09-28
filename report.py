from pathlib import Path
from data import ACTIVITY_NAMES

def save_text_report(usage, level):
    path = Path("water_footprint_report.txt")

    lines = [
        "WATER FOOTPRINT CHECK - RESULT",
        "================================",
        f"Estimated water use: {usage['total']:.1f} litres/day",
        f"Usage category: {level}",
        "",
        "Breakdown:"
    ]

    for key, value in usage.items():
        if key != "total":
            lines.append(f"- {ACTIVITY_NAMES[key]}: {value:.1f} L")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path

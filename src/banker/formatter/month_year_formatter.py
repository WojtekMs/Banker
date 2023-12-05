from banker.analyzer.analyze import MonthYear


def format_month_year(month_year: MonthYear) -> str:
    mapping = {1: "Styczeń", 2: "Luty", 3: "Marzec", 4: "Kwiecień", 5: "Maj", 6: "Czerwiec", 7: "Lipiec", 8: "Sierpień",
               9: "Wrzesień", 10: "Październik", 11: "Listopad", 12: "Grudzień"}
    return f"{mapping[month_year.month]} {month_year.year}"

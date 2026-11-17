# Bengali date formatting and day ordinals
from datetime import date
from typing import Tuple
from .digits import to_bangla_digits

# Day suffixes according to traditional Bengali practice
# ১লা, ২রা, ৩রা, ৪ঠা, ৫ই ... ১৮ই, ১৯শে ... ৩১শে
DATE_ORDINALS = {
    1: "১লা", 2: "২রা", 3: "৩রা", 4: "৪ঠা",
    5: "৫ই", 6: "৬ই", 7: "৭ই", 8: "৮ই", 9: "৯ই", 10: "১০ই",
    11: "১১ই", 12: "১২ই", 13: "১৩ই", 14: "১৪ই", 15: "১৫ই",
    16: "১৬ই", 17: "১৭ই", 18: "১৮ই",
    19: "১৯শে", 20: "২০শে", 21: "২১শে", 22: "২২শে", 23: "২৩শে",
    24: "২৪শে", 25: "২৫শে", 26: "২৬শে", 27: "২৭শে", 28: "২৮শে",
    29: "২৯শে", 30: "৩০শে", 31: "৩১শে"
}

GREGORIAN_MONTHS_BN = [
    "", "জানুয়ারি", "ফেব্রুয়ারি", "মার্চ", "এপ্রিল", "মে", "জুন",
    "জুলাই", "আগস্ট", "সেপ্টেম্বর", "অক্টোবর", "নভেম্বর", "ডিসেম্বর"
]

BENGALI_MONTHS = [
    "", "বৈশাখ", "জ্যৈষ্ঠ", "আষাঢ়", "শ্রাবণ", "ভাদ্র",
    "আশ্বিন", "কার্তিক", "অগ্রহায়ণ", "পৌষ", "মাঘ", "ফাল্গুন", "চৈত্র"
]

def is_gregorian_leap_year(year: int) -> bool:
    """Returns True if the given Gregorian year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def gregorian_to_bongabdo(year: int, month: int, day: int) -> Tuple[int, int, int]:
    """
    Converts a Gregorian date (year, month, day) to the revised Bengali calendar (বঙ্গাব্দ)
    adopted by the Bangla Academy and Government of Bangladesh (2019 revision).
    Returns (byear, bmonth, bday).

    Bengali Calendar rules:
    - Pahela Baishakh starts on April 14.
    - Months 1-6 (Boishakh to Ashwin) have 31 days each.
    - Months 7-10 (Kartik to Magh) have 30 days each.
    - Month 11 (Falgun) has 29 days (30 in Gregorian leap years).
    - Month 12 (Chaitra) has 30 days.
    - April 14 to Dec 31: Bangabda = Gregorian - 593.
    - Jan 1 to April 13: Bangabda = Gregorian - 594.
    """
    target = date(year, month, day)

    if (month, day) >= (4, 14):
        byear = year - 593
        start_date = date(year, 4, 14)
        falgun_leap = is_gregorian_leap_year(year + 1)
    else:
        byear = year - 594
        start_date = date(year - 1, 4, 14)
        falgun_leap = is_gregorian_leap_year(year)

    days_elapsed = (target - start_date).days

    month_days = [
        31,  # 1. Boishakh
        31,  # 2. Jaishtha
        31,  # 3. Asharh
        31,  # 4. Shraban
        31,  # 5. Bhadro
        31,  # 6. Ashwin
        30,  # 7. Kartik
        30,  # 8. Agrahayan
        30,  # 9. Poush
        30,  # 10. Magh
        30 if falgun_leap else 29,  # 11. Falgun
        30,  # 12. Chaitra
    ]

    bmonth = 1
    rem_days = days_elapsed
    for md in month_days:
        if rem_days < md:
            bday = rem_days + 1
            return (byear, bmonth, bday)
        rem_days -= md
        bmonth += 1

    return (byear, 12, 30)

def format_date_bangla(year: int, month: int, day: int) -> str:
    """
    Format a Gregorian date with Bengali month name, date suffix, and Bengali year digits.
    Example: (2026, 3, 26) -> "২৬শে মার্চ, ২০২৬"
    """
    day_str = DATE_ORDINALS.get(day, f"{to_bangla_digits(day)}ই")
    month_str = GREGORIAN_MONTHS_BN[month] if 1 <= month <= 12 else str(month)
    year_str = to_bangla_digits(year)
    return f"{day_str} {month_str}, {year_str}"

def format_date_bongabdo(year: int, month: int, day: int, from_gregorian: bool = False) -> str:
    """
    Format a traditional Bengali calendar date (বঙ্গাব্দ) with Bengali month name,
    date ordinal suffix, and Bengali year digits.
    If from_gregorian is True or year >= 1800, automatically converts from Gregorian date.
    Example: (1433, 1, 1) -> "১লা বৈশাখ, ১৪৩৩ বঙ্গাব্দ"
    Example: (2026, 4, 14, from_gregorian=True) -> "১লা বৈশাখ, ১৪৩৩ বঙ্গাব্দ"
    """
    if from_gregorian or year >= 1800:
        year, month, day = gregorian_to_bongabdo(year, month, day)

    day_str = DATE_ORDINALS.get(day, f"{to_bangla_digits(day)}ই")
    month_str = BENGALI_MONTHS[month] if 1 <= month <= 12 else str(month)
    year_str = to_bangla_digits(year)
    return f"{day_str} {month_str}, {year_str} বঙ্গাব্দ"

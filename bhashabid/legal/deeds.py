# bhashabid/legal/deeds.py
# Land Registry Conveyancing & Deed Formatter (নিবন্ধন পরিদপ্তর সাফ-কবলা ও হস্তান্তর দলিল)
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional
from ..normalize.unicode import canonicalize_unicode

class DeedType(Enum):
    SAF_KABALA = "সাফ-কবলা বিক্রয় দলিল (Outright Sale Deed)"
    HEBA_BIL_EWAJ = "হেবা-বিল-এওয়াজ (Gift for Consideration)"
    BAYNANAMA = "বায়নানামা (Agreement for Sale)"
    BANTANNAMA = "বণ্টননামা দলিল (Partition Deed)"
    MOKTAR_NAMA = "আমমোক্তারনামা (Power of Attorney)"

@dataclass
class DeedSchedule:
    district: str = ""
    subregistry: str = ""
    mouza: str = ""
    jl_number: str = ""
    khatian_type: str = "আরএস"
    khatian_number: str = ""
    dag_number: str = ""
    land_class: str = "নাল"
    area: str = ""
    boundaries: Dict[str, str] = field(default_factory=dict)

    def __init__(
        self,
        district: str = "",
        subregistry: str = "",
        mouza: str = "",
        jl_number: str = "",
        khatian_type: str = "আরএস",
        khatian_number: str = "",
        dag_number: str = "",
        land_class: str = "নাল",
        area: str = "",
        boundaries: Optional[Dict[str, str]] = None,
        # Common aliases for ease of consumption
        thana: Optional[str] = None,
        jl_no: Optional[str] = None,
        khatian_no: Optional[str] = None,
        dag_no: Optional[str] = None,
        land_area: Optional[str] = None
    ):
        self.district = district
        self.subregistry = thana if thana is not None else subregistry
        self.mouza = mouza
        self.jl_number = jl_no if jl_no is not None else jl_number
        self.khatian_type = khatian_type
        self.khatian_number = khatian_no if khatian_no is not None else khatian_number
        self.dag_number = dag_no if dag_no is not None else dag_number
        self.land_class = land_class
        self.area = land_area if land_area is not None else area
        self.boundaries = boundaries if boundaries is not None else {}

def format_deed_schedule(sch: DeedSchedule) -> str:
    """Formats an authentic Directorate of Registration Schedule of Property (জমির তফশিল বিবরণ)."""
    district = canonicalize_unicode(sch.district)
    subregistry = canonicalize_unicode(sch.subregistry)
    mouza = canonicalize_unicode(sch.mouza)
    jl_number = canonicalize_unicode(sch.jl_number)
    khatian_type = canonicalize_unicode(sch.khatian_type)
    khatian_number = canonicalize_unicode(sch.khatian_number)
    dag_number = canonicalize_unicode(sch.dag_number)
    land_class = canonicalize_unicode(sch.land_class)
    area = canonicalize_unicode(sch.area)

    lines = [
        "তফশিল সম্পত্তি পরিচয়:",
        f"জেলা: {district}, উপজেলা ও সাব-রেজিস্ট্রি অফিস: {subregistry}।",
        f"মৌজা: {mouza}, জে. এল. নম্বর: {jl_number}।",
        f"খতিয়ান ({khatian_type}): {khatian_number}, দাগ নম্বর: {dag_number}।",
        f"জমির শ্রেণি: {land_class}, হস্তান্তরিত জমির পরিমাণ: {area}।",
    ]
    if sch.boundaries:
        b = sch.boundaries
        north = canonicalize_unicode(b.get("north", ""))
        south = canonicalize_unicode(b.get("south", ""))
        east = canonicalize_unicode(b.get("east", ""))
        west = canonicalize_unicode(b.get("west", ""))
        b_str = f"উত্তর: {north}, দক্ষিণ: {south}, পূর্ব: {east}, পশ্চিম: {west}।"
        lines.append(f"চৌহদ্দির বিবরণ: {b_str}")
    return "\n".join(lines)

def generate_encumbrance_free_clause(vendor_name: str = "বিক্রেতা") -> str:
    """Generates statutory encumbrance-free warranty clause (দায়মুক্ততার ঘোষণা)."""
    vendor = canonicalize_unicode((vendor_name or "বিক্রেতা").strip())
    return (
        f"{vendor} নিশ্চয়তা প্রদান করিতেছেন যে, তফশিলবর্ণিত সম্পত্তি পূর্বে কাহারও নিকট বিক্রয়, বন্ধক, "
        "বা কোনো প্রকার দায়বদ্ধ করা হয় নাই এবং ইহা যাবতীয় ঋণভার, ক্রোকি পরোয়ানা ও সরকারি দাবি হইতে সর্বতোভাবে দায়মুক্ত ও নির্ভেজাল।"
    )

def generate_saf_kabala_clause(
    vendor_name: str,
    purchaser_name: str,
    consideration_bengali: str = "",
    schedule: Optional[DeedSchedule] = None,
    **kwargs
) -> str:
    """Generates an authentic Saf-Kabala conveyance clause."""
    vendor = canonicalize_unicode(vendor_name.strip())
    purchaser = canonicalize_unicode(purchaser_name.strip())

    if "consideration_taka" in kwargs:
        consideration_bengali = kwargs["consideration_taka"]
    elif "consideration" in kwargs:
        consideration_bengali = kwargs["consideration"]

    if isinstance(consideration_bengali, (int, float)):
        from ..numbers import format_currency_words
        consideration = format_currency_words(float(consideration_bengali))
    elif isinstance(consideration_bengali, str) and consideration_bengali.strip().replace(".", "", 1).isdigit():
        from ..numbers import format_currency_words
        consideration = format_currency_words(float(consideration_bengali.strip()))
    else:
        consideration = canonicalize_unicode(str(consideration_bengali).strip())

    if schedule:
        sch_parts = []
        if getattr(schedule, "mouza", None):
            sch_parts.append(f"মৌজা {schedule.mouza}")
        if getattr(schedule, "khatian_number", None):
            k_type = getattr(schedule, "khatian_type", "") or "আরএস"
            sch_parts.append(f"{k_type} খতিয়ান নং {schedule.khatian_number}")
        if getattr(schedule, "dag_number", None):
            sch_parts.append(f"দাগ নং {schedule.dag_number}")
        if getattr(schedule, "area", None):
            l_class = getattr(schedule, "land_class", "") or "নাল"
            sch_parts.append(f"{schedule.area} {l_class}")
        sch_summary = "-স্থিত ".join(sch_parts) if sch_parts else "সম্পত্তি"
    else:
        sch_summary = "সম্পত্তি"

    return (
        f"যেহেতু {vendor} নগদ বাবদ পণমূল্য {consideration} বুঝিয়া পাইয়া তফশিলবর্ণিত {sch_summary} "
        f"যাবতীয় স্বত্ব, স্বার্থ ও অধিকারসহ {purchaser}-এর অনুকূলে চিরতরে সাফ-কবলা বিক্রয়পূর্বক দখল বুঝাইয়া দিলেন; "
        f"অতএব অদ্য হইতে {purchaser} উক্ত সম্পত্তির নিরঙ্কুশ মালিক গণ্য হইয়া নামজারি ও ভূমি উন্নয়ন কর পরিশোধক্রমে পুরুষানুক্রমে ভোগদখল করিতে থাকিবেন।"
    )

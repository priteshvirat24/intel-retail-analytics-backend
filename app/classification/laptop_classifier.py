"""
Strict Laptop Classification Module.
Implements the 12 product classes and rigorous positive/negative rule enforcement.
Rejects accessories, software, peripherals, appliances, and category pages.
"""
import re
from enum import Enum
from typing import Dict, Any, List, Optional, Tuple
from pydantic import BaseModel, Field


class ProductClass(str, Enum):
    LAPTOP = "LAPTOP"
    DESKTOP = "DESKTOP"
    TABLET = "TABLET"
    PHONE = "PHONE"
    MONITOR = "MONITOR"
    ACCESSORY = "ACCESSORY"
    SOFTWARE = "SOFTWARE"
    PERIPHERAL = "PERIPHERAL"
    COMPONENT = "COMPONENT"
    APPLIANCE = "APPLIANCE"
    CATEGORY_PAGE = "CATEGORY_PAGE"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"


class ClassificationResult(BaseModel):
    product_class: ProductClass
    is_genuine_laptop: bool
    confidence_score: float
    detected_brand: Optional[str] = None
    model_or_sku: Optional[str] = None
    extracted_specs: Dict[str, Any] = Field(default_factory=dict)
    positive_signals: List[str] = Field(default_factory=list)
    negative_signals: List[str] = Field(default_factory=list)
    rejection_reason: Optional[str] = None


class LaptopClassifier:
    """Strict classifier for genuine laptop computer products."""

    # Explicit Hard Negative Patterns - Immediately Disqualify
    HARD_NEGATIVE_PATTERNS = [
        # Accessories / Bags / Cases
        (r"\b(bag|bags|case|cases|sleeve|sleeves|backpack|backpacks|cover|covers|skin|skins|pouch|briefcase|tote)\b", ProductClass.ACCESSORY, "Laptop Bag / Case / Sleeve"),
        (r"\b(pasta|mochila|housse|sacoche|tasche|h[üu]lle|funda|custodia|bolsa|malet[ií]n|etui|k[ıi]l[ıi]f[ıi]?|[çc]anta(s[ıi])?|torba|plecak|t[uú]i|balo)\b", ProductClass.ACCESSORY, "Laptop Bag / Sleeve (Multilingual)"),
        (r"\b(stand|stands|cooling\s*pad|cooler|so[gğ]utucu|riser|holder|mount|dock|docking\s*station|hub)\b", ProductClass.ACCESSORY, "Laptop Stand / Dock / Cooling Pad"),
        (r"\b(charger|chargers|adapter|adapters|power\s*supply|carregador|cargador|chargeur|netzteil|alimentatore|[sş]arj|[sş]arj\s*aleti|[lł]adowarka|zasilacz|s[aạ]c)\b", ProductClass.ACCESSORY, "Laptop Charger / Power Adapter"),
        (r"\b(power\s*bank|bateria\s*port[aá]til|batterie\s*externe|powerbank|portable\s*battery)\b", ProductClass.ACCESSORY, "Power Bank / Portable Battery"),
        (r"\b(cable|cables|cord|cords|hdmi|usb-c\s*to|dongle|splitter|wire)\b", ProductClass.ACCESSORY, "Cable / Connector / Dongle"),
        (r"\b(screen\s*protector|privacy\s*filter|keyboard\s*cover|trackpad\s*film)\b", ProductClass.ACCESSORY, "Screen Protector / Film"),
        (r"\b(replacement\s*screen|replacement\s*battery|internal\s*battery|spare\s*part|touchpad\s*replacement)\b", ProductClass.ACCESSORY, "Replacement Part / Internal Battery"),
        
        # Peripherals & Input Devices
        (r"\b(mouse|mice|maus|rat[oó]n|mousepad|mouse\s*pad)\b", ProductClass.PERIPHERAL, "Computer Mouse / Peripheral"),
        (r"\b(keyboard|keyboards|tastatur|tastiera)\b", ProductClass.PERIPHERAL, "Computer Keyboard"),
        (r"\b(souris\s+(sans\s+fil|optique|gamer|filaire|usb|bluetooth))\b", ProductClass.PERIPHERAL, "Computer Mouse (French)"),
        (r"\b(clavier\s+(sans\s+fil|m[eé]canique|gamer|filaire|usb|bluetooth))\b", ProductClass.PERIPHERAL, "Computer Keyboard (French)"),
        (r"\b(teclado\s+(sem\s+fio|gamer|mec[aâ]nico|inal[aá]mbrico|usb|bluetooth))\b", ProductClass.PERIPHERAL, "Computer Keyboard (ES/PT)"),
        (r"\b(headset|headphone|headphones|earbuds|earphones|casque|kopfh[oö]rer|auriculares|cuffie)\b", ProductClass.PERIPHERAL, "Headset / Headphones"),
        (r"\b(webcam|web\s*camera|camera|micro|microphone)\b", ProductClass.PERIPHERAL, "Webcam / Microphone"),
        (r"\b(printer|printers|scanner|scanners|imprimante|drucker|stampante|impressora)\b", ProductClass.PERIPHERAL, "Printer / Scanner"),
        (r"\b(monitor|monitors|display|ecran|bildschirm|schermo|pantalla)\b", ProductClass.MONITOR, "Standalone Monitor / Display"),

        # Software & Licenses
        (r"\b(antivirus|anti-virus|livesafe|total\s*protection|mcafee|norton|kaspersky|bitdefender|avast|eset|avg)\b", ProductClass.SOFTWARE, "Antivirus / Security Software"),
        (r"\b(microsoft\s*365|office\s*365|windows\s*1[01]\s*(pro|home)?\s*(license|key|download\s*code)|software\s*license|digital\s*code)\b", ProductClass.SOFTWARE, "Software / OS License"),

        # Appliances & Non-Computers
        (r"\b(condizionatore|air\s*conditioner|climatiseur|klimaanlage|aire\s*acondicionado|ventilateur|fan|heater)\b", ProductClass.APPLIANCE, "Air Conditioner / Appliance"),

        # Non-Laptop Devices
        (r"\b(smartphone|phone|cellphone|iphone|galaxy\s*s2[0-9]|redmi|xiaomi\s*1[0-9]|t[eé]l[eé]phone)\b", ProductClass.PHONE, "Smartphone / Mobile Phone"),
        (r"\b(desktop|tower|pc\s*de\s*bureau|all-in-one|aio|workstation\s*tower|gaming\s*desktop)\b", ProductClass.DESKTOP, "Desktop / All-in-One PC"),
        (r"\b(ipad\s*(air|pro|mini)?|galaxy\s*tab|kindle|fire\s*hd|android\s*tablet)\b", ProductClass.TABLET, "Tablet / E-Reader"),

        # Category / Hub / Listing Indicator
        (r"\b(all\s*laptops|best\s*laptops\s*of|buying\s*guide|catalog|departments|all-in-one\s*category|laptopy\s*i\s*komputery|everyday\s*value\s*laptops|gaming\s*laptops|laptop\s*gaming)\b", ProductClass.CATEGORY_PAGE, "Category Hub / Buying Guide")
    ]

    # Positive Laptop Product Families
    LAPTOP_FAMILIES = [
        "thinkpad", "ideapad", "yoga", "legion", "loq", "macbook", "macbook air", "macbook pro",
        "vivobook", "zenbook", "rog", "tuf gaming", "expertbook", "proart",
        "inspiron", "xps", "alienware", "latitude", "vostro", "precision",
        "pavilion", "envy", "spectre", "omen", "victus", "omnibook", "omnipad", "elitebook", "probook", "chromebook",
        "aspire", "swift", "predator", "nitro", "travelmate",
        "surface laptop", "surface pro", "surface book",
        "galaxy book", "gram", "blade", "razer blade", "stealth", "prestige", "modern", "katana", "cyborg",
        # Monster Notebook TR families
        "abra", "tulpar", "semruk", "huma",
        # Korean transliterations
        "오멘", "빅터스", "그램", "갤럭시북", "비전", "씽크패드", "아이디어패드", "리전", "요가", "맥북", "젠북", "비보북", "파빌리온", "인스피론",
        # Japanese transliterations
        "レグザ", "ダイナブック", "レッツノート", "シンクパッド", "マックブック",
        # Chinese product families
        "拯救者", "小新", "天选", "战66", "暗影精灵", "光影精灵", "灵耀", "无畏", "机械革命",
    ]

    # Laptop Keywords (Multilingual)
    LAPTOP_KEYWORDS = [
        "laptop", "laptops", "notebook", "notebooks", "macbook", "chromebook",
        "portatil", "portátil", "portatiles", "portátiles", "ordenador portátil",
        "ordinateur portable", "pc portable",
        "dizüstü", "dizustu", "bilgisayar", "bilgisayarı", "bilgisayari",
        "oyun bilgisayar", "taşınabilir bilgisayar",
        "máy tính xách tay",
        "노트북", "노트북컴퓨터", "랩탑", "랩톱",
        "ノートパソコン", "ノートpc", "ノートブック",
        "笔记本电脑", "手提电脑", "笔记本",
        "bærbar", "bärbar", "kannettava",
        "caderno", "computador portátil",
        "portatile", "computer portatile",
    ]

    # Major Laptop Brands
    LAPTOP_BRANDS = [
        "Apple", "Lenovo", "Dell", "HP", "ASUS", "Acer", "MSI", "Microsoft", "Samsung",
        "LG", "Razer", "Gigabyte", "Huawei", "Honor", "Xiaomi", "Toshiba", "Dynabook",
        "Monster", "Medion", "Fujitsu", "Panasonic", "Infinix", "Avita",
        "삼성", "LG전자", "엘지", "한성컴퓨터", "레노버", "델", "에이수스", "아수스", "에이서", "한성",
    ]

    @classmethod
    def classify(cls, title: str, html: str = "", url: str = "", price: Optional[float] = None) -> ClassificationResult:
        """Strictly classifies whether a target product is a genuine laptop computer."""
        title_clean = (title or "").strip()
        title_lower = title_clean.lower()
        url_lower = (url or "").lower()
        combined_text = f"{title_lower} {url_lower}"

        pos_signals = []
        neg_signals = []

        # 1. Check Hard Negatives FIRST
        for pattern, prod_class, desc in cls.HARD_NEGATIVE_PATTERNS:
            if re.search(pattern, title_lower, re.IGNORECASE):
                neg_signals.append(f"Hard negative match: {desc}")
                return ClassificationResult(
                    product_class=prod_class,
                    is_genuine_laptop=False,
                    confidence_score=0.0,
                    positive_signals=pos_signals,
                    negative_signals=neg_signals,
                    rejection_reason=f"Rejected as {prod_class.value}: {desc}"
                )

        # Check for Category Page / Listing Page URLs
        if any(cat in url_lower for cat in ["/category/", "/categories/", "/laptops.html", "/laptops/", "/laptop-gaming", "/search?", "/s?k=", "/c/technology/"]):
            # If title is generic category title
            if any(title_lower == t.lower() for t in ["laptops", "laptop", "notebooks", "gaming laptops", "laptop gaming", "everyday value laptops", "laptop computers"]):
                neg_signals.append("Category / Department listing page, not an individual SKU")
                return ClassificationResult(
                    product_class=ProductClass.CATEGORY_PAGE,
                    is_genuine_laptop=False,
                    confidence_score=0.0,
                    positive_signals=pos_signals,
                    negative_signals=neg_signals,
                    rejection_reason="Category page / Catalog hub, not a single laptop product SKU"
                )

        # 2. Check Positive Signals
        # 2a. Laptop Keywords in Title (and HTML body fallback)
        has_laptop_kw = False
        # Check title first, then URL, then first 5000 chars of HTML body
        search_targets = [title_lower, url_lower]
        html_snippet = html[:5000].lower() if html else ""
        for kw in cls.LAPTOP_KEYWORDS:
            if re.search(rf"\b{re.escape(kw)}\b", title_lower) or kw in title_lower:
                pos_signals.append(f"Laptop keyword: '{kw}'")
                has_laptop_kw = True
                break
            elif kw in url_lower:
                pos_signals.append(f"Laptop keyword in URL: '{kw}'")
                has_laptop_kw = True
                break
        # If not found in title/URL, check HTML body (lower weight)
        if not has_laptop_kw and html_snippet:
            for kw in cls.LAPTOP_KEYWORDS:
                if kw in html_snippet:
                    pos_signals.append(f"Laptop keyword in body: '{kw}'")
                    has_laptop_kw = True
                    break

        # 2b. Known Laptop Family
        detected_family = None
        for fam in cls.LAPTOP_FAMILIES:
            if any(ord(c) > 127 for c in fam):
                if fam in title_lower or fam in combined_text:
                    pos_signals.append(f"Laptop family: '{fam}'")
                    detected_family = fam
                    break
            elif re.search(rf"\b{re.escape(fam)}\b", title_lower):
                pos_signals.append(f"Laptop family: '{fam}'")
                detected_family = fam
                break

        # 2c. Laptop Brand Detection (title + URL/domain)
        detected_brand = None
        for b in cls.LAPTOP_BRANDS:
            b_low = b.lower()
            if any(ord(c) > 127 for c in b):
                if b_low in title_lower or b_low in url_lower:
                    detected_brand = b
                    pos_signals.append(f"Brand: '{b}'")
                    break
            elif re.search(rf"\b{re.escape(b_low)}\b", title_lower):
                detected_brand = b
                pos_signals.append(f"Brand: '{b}'")
                break
            elif re.search(rf"\b{re.escape(b_low)}\b", url_lower):
                detected_brand = b
                pos_signals.append(f"Brand in URL: '{b}'")
                break

        # 2d. Hardware Specification Extraction
        extracted_specs = {}

        # Screen Size (e.g. 13.3", 14", 15.6", 16", 17.3")
        screen_m = re.search(r"(\b1[1-7](\.[0-9])?)\s*(\"|''|inch|po|\s*pulgadas|\s*zoll|\s*pollici)", title_lower)
        if screen_m:
            extracted_specs["screen_size"] = f"{screen_m.group(1)}\""
            pos_signals.append(f"Screen size: {screen_m.group(1)}\"")

        # Processor / CPU
        cpu_patterns = [
            r"(?:^|\b|[^a-zA-Z0-9])(intel\s*core\s*(?:i[3579]|ultra\s*[579])[\w-]*)",
            r"(?:^|\b|[^a-zA-Z0-9])(i[3579]-?[0-9]{4,5}[a-z0-9]*)",
            r"(?:^|\b|[^a-zA-Z0-9])(core\s*[3579]-?[0-9]{3,4}[a-z0-9]*)",
            r"(?:^|\b|[^a-zA-Z0-9])(ultra\s*[579]-?[0-9]{3,4}[a-z0-9]*)",
            r"(?:^|\b|[^a-zA-Z0-9])(ryzen\s*[3579](?:\s*pro)?(?:\s*[0-9]{4}[a-z0-9]*)?)",
            r"(?:^|\b|[^a-zA-Z0-9])(r[3579]-?[0-9]{4}[a-z0-9]*)",
            r"(?:^|\b|[^a-zA-Z0-9])(apple\s*m[1-4](?:\s*pro|\s*max)?|m[1-4]\s*chip)",
            r"(?:^|\b|[^a-zA-Z0-9])(snapdragon\s*x(?:\s*plus|\s*elite)?)",
            r"(?:^|\b|[^a-zA-Z0-9])(celeron\s*[a-z0-9]*|pentium\s*[a-z0-9]*|athlon\s*[a-z0-9]*)",
            r"(?:^|\b|[^a-zA-Z0-9])(mediatek\s*kompanio\s*[0-9]+|kompanio\s*[0-9]+)"
        ]
        for cp in cpu_patterns:
            cpu_m = re.search(cp, title_lower)
            if cpu_m:
                val = cpu_m.group(1).strip().title()
                extracted_specs["cpu"] = val
                pos_signals.append(f"CPU: {val}")
                break

        # GPU / Graphics
        gpu_patterns = [
            r"(?:^|\b|[^a-zA-Z0-9])(rtx\s*[2345]0[0-9]{2}(?:\s*ti|\s*super)?)",
            r"(?:^|\b|[^a-zA-Z0-9])(gtx\s*1[60][0-9]{2}(?:\s*ti)?)",
            r"(?:^|\b|[^a-zA-Z0-9])(geforce\s*(?:rtx|gtx)\s*[0-9]{4})",
            r"(?:^|\b|[^a-zA-Z0-9])(radeon\s*(?:rx\s*[0-9]{4}[a-z]*|[0-9]{3}m|graphics))",
            r"(?:^|\b|[^a-zA-Z0-9])(intel\s*(?:iris\s*xe|arc\s*[a-z0-9]+|uhd\s*graphics))"
        ]
        for gp in gpu_patterns:
            gpu_m = re.search(gp, title_lower)
            if gpu_m:
                val = gpu_m.group(1).strip().upper()
                extracted_specs["gpu"] = val
                pos_signals.append(f"GPU: {val}")
                break

        # RAM (e.g. 8GB RAM, 16GB, 32GB, 8 Go, 16 Go)
        ram_m = re.search(r"\b([48]|12|16|24|32|64)\s*(gb|go|g)\s*(ram|memory|ddr[45]|lpddr[45]|memoria)?\b", title_lower)
        if ram_m:
            extracted_specs["ram"] = f"{ram_m.group(1)}GB"
            pos_signals.append(f"RAM: {ram_m.group(1)}GB")

        # Storage (e.g. 64GB eMMC, 128GB, 256GB, 512GB SSD, 1TB SSD)
        storage_m = re.search(r"\b(64|128|256|512)\s*(gb|go)\s*(ssd|nvme|emmc|m\.2)?\b|\b(1|2)\s*tb\s*(ssd|nvme|hdd|m\.2)?\b", title_lower)
        if storage_m:
            extracted_specs["storage"] = storage_m.group(0).upper()
            pos_signals.append(f"Storage: {storage_m.group(0).upper()}")

        # Operating System
        os_m = re.search(r"\b(windows\s*1[01]|macos|chrome\s*os|linux|keepos|freedos)\b", title_lower)
        if os_m:
            extracted_specs["os"] = os_m.group(0).title()
            pos_signals.append(f"OS: {os_m.group(0).title()}")

        # Model / SKU Extraction from Title / URL
        sku_m = re.search(r"\b([a-z0-9]{2,5}-[a-z0-9]{4,8}|b0[a-z0-9]{8}|[0-9]{7,10})\b", combined_text, re.IGNORECASE)
        model_or_sku = sku_m.group(0) if sku_m else None

        # 3. Calculate Strict Confidence Score
        score = 0.0
        if has_laptop_kw:
            score += 0.40
        if detected_family:
            score += 0.35
        if detected_brand:
            score += 0.15
        if "cpu" in extracted_specs:
            score += 0.20
        if "gpu" in extracted_specs:
            score += 0.15
        if "screen_size" in extracted_specs:
            score += 0.15
        if "ram" in extracted_specs:
            score += 0.10
        if "storage" in extracted_specs:
            score += 0.10
        if price and price > 100.0:  # Real laptops generally cost > $100 USD
            score += 0.10

        score = min(1.0, round(score, 2))

        # Strict acceptance criteria:
        # Must have (Laptop Keyword OR Laptop Family) AND (Brand OR Hardware Spec) AND Score >= 0.60
        is_genuine = (
            (has_laptop_kw or detected_family is not None) and
            (detected_brand is not None or len(extracted_specs) >= 1) and
            score >= 0.60
        )

        prod_class = ProductClass.LAPTOP if is_genuine else ProductClass.OTHER

        return ClassificationResult(
            product_class=prod_class,
            is_genuine_laptop=is_genuine,
            confidence_score=score,
            detected_brand=detected_brand,
            model_or_sku=model_or_sku,
            extracted_specs=extracted_specs,
            positive_signals=pos_signals,
            negative_signals=neg_signals,
            rejection_reason=None if is_genuine else f"Insufficient laptop confidence (Score: {score} < 0.70)"
        )

    @classmethod
    def validate_candidate_url(cls, url: str, title: str = "") -> Tuple[bool, str]:
        """Pre-filters candidate URLs and titles to discard obvious non-laptop accessories and category hubs."""
        combined = f"{url} {title}".lower()

        # Reject category listings
        if any(x in url.lower() for x in ["/category/", "/categories/", "/katalog/", "/departments/", "/cart", "/checkout", "/login"]):
            return False, "Category or transactional URL"

        # Check hard negative patterns
        for pattern, prod_class, desc in cls.HARD_NEGATIVE_PATTERNS:
            if re.search(pattern, combined, re.IGNORECASE):
                return False, f"Matched negative pattern: {desc}"

        return True, "Valid candidate"

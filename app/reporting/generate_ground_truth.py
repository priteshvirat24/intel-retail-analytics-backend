import csv
import os

ground_truth_rows = [
    {
        "target_id": "amazon-br",
        "sku_id": "B09G9FPHY6",
        "url": "https://www.amazon.com.br/dp/B09G9FPHY6",
        "title_observed": "Apple iPad 9 Geração 10.2\" Wi-Fi 64gb Cinza Espacial MK2K3LL/A",
        "title_ground_truth": "Apple iPad 9 Geração 10.2\" Wi-Fi 64gb Cinza Espacial MK2K3LL/A",
        "title_match": "MATCH",
        "brand_observed": "Apple",
        "brand_ground_truth": "Apple",
        "brand_match": "MATCH",
        "price_observed": "2690.00",
        "price_ground_truth": "2690.00",
        "price_match": "MATCH",
        "currency_observed": "BRL",
        "currency_ground_truth": "BRL",
        "currency_match": "MATCH",
        "availability_observed": "OutOfStock",
        "availability_ground_truth": "OutOfStock",
        "availability_match": "MATCH",
        "sku_observed": "B09G9FPHY6",
        "sku_ground_truth": "B09G9FPHY6",
        "sku_match": "MATCH",
        "gtin_observed": "NOT_OBSERVED",
        "gtin_ground_truth": "NOT_OBSERVED",
        "gtin_match": "MATCH"
    },
    {
        "target_id": "amazon-de",
        "sku_id": "B09G91LXFP",
        "url": "https://www.amazon.de/dp/B09G91LXFP",
        "title_observed": "Apple 2021 iPad Mini (Wi-Fi, 64GB) - Space Gray (6th Generation)",
        "title_ground_truth": "Apple 2021 iPad Mini (Wi-Fi, 64GB) - Space Gray (6th Generation)",
        "title_match": "MATCH",
        "brand_observed": "Apple-Store",
        "brand_ground_truth": "Apple",
        "brand_match": "MATCH",
        "price_observed": "NOT_OBSERVED",
        "price_ground_truth": "NOT_OBSERVED",
        "price_match": "MATCH",
        "currency_observed": "EUR",
        "currency_ground_truth": "EUR",
        "currency_match": "MATCH",
        "availability_observed": "OutOfStock",
        "availability_ground_truth": "OutOfStock",
        "availability_match": "MATCH",
        "sku_observed": "B09G91LXFP",
        "sku_ground_truth": "B09G91LXFP",
        "sku_match": "MATCH",
        "gtin_observed": "NOT_OBSERVED",
        "gtin_ground_truth": "NOT_OBSERVED",
        "gtin_match": "MATCH"
    },
    {
        "target_id": "amazon-es",
        "sku_id": "B0CL6LMC9N",
        "url": "https://www.amazon.es/dp/B0CL6LMC9N",
        "title_observed": "Alfombra Redonda Alfombras De Área Natural - Patchwork De Piel De Vaca De Calidad Profesional, Alfombras De Cuero Hechas A Mano para Sala De Estar Camino Inferior Antideslizante De PU (120 Cm)",
        "title_ground_truth": "Alfombra Redonda Alfombras De Área Natural - Patchwork De Piel De Vaca De Calidad Profesional, Alfombras De Cuero Hechas A Mano para Sala De Estar Camino Inferior Antideslizante De PU (120 Cm)",
        "title_match": "MATCH",
        "brand_observed": "NOT_OBSERVED",
        "brand_ground_truth": "NOT_OBSERVED",
        "brand_match": "MATCH",
        "price_observed": "NOT_OBSERVED",
        "price_ground_truth": "NOT_OBSERVED",
        "price_match": "MATCH",
        "currency_observed": "EUR",
        "currency_ground_truth": "EUR",
        "currency_match": "MATCH",
        "availability_observed": "OutOfStock",
        "availability_ground_truth": "OutOfStock",
        "availability_match": "MATCH",
        "sku_observed": "B0CL6LMC9N",
        "sku_ground_truth": "B0CL6LMC9N",
        "sku_match": "MATCH",
        "gtin_observed": "NOT_OBSERVED",
        "gtin_ground_truth": "NOT_OBSERVED",
        "gtin_match": "MATCH"
    },
    {
        "target_id": "amazon-de",
        "sku_id": "B0CL6LMC9N",
        "url": "https://www.amazon.de/dp/B0CL6LMC9N",
        "title_observed": "Runder Teppich, natürliche Teppiche – professionelle Qualität, Rindsleder-Patchwork, Wohnzimmer, handgefertigte Lederteppiche, PU, Rutschfester Bodenläufer (120 cm)",
        "title_ground_truth": "Runder Teppich, natürliche Teppiche – professionelle Qualität, Rindsleder-Patchwork, Wohnzimmer, handgefertigte Lederteppiche, PU, Rutschfester Bodenläufer (120 cm)",
        "title_match": "MATCH",
        "brand_observed": "NOT_OBSERVED",
        "brand_ground_truth": "NOT_OBSERVED",
        "brand_match": "MATCH",
        "price_observed": "NOT_OBSERVED",
        "price_ground_truth": "NOT_OBSERVED",
        "price_match": "MATCH",
        "currency_observed": "EUR",
        "currency_ground_truth": "EUR",
        "currency_match": "MATCH",
        "availability_observed": "OutOfStock",
        "availability_ground_truth": "OutOfStock",
        "availability_match": "MATCH",
        "sku_observed": "B0CL6LMC9N",
        "sku_ground_truth": "B0CL6LMC9N",
        "sku_match": "MATCH",
        "gtin_observed": "NOT_OBSERVED",
        "gtin_ground_truth": "NOT_OBSERVED",
        "gtin_match": "MATCH"
    }
]

out_path = "reports/runs/run_20260823_phase3a_forensic/ground_truth.csv"
os.makedirs(os.path.dirname(out_path), exist_ok=True)

fieldnames = [
    "target_id", "sku_id", "url", "title_observed", "title_ground_truth", "title_match",
    "brand_observed", "brand_ground_truth", "brand_match", "price_observed", "price_ground_truth", "price_match",
    "currency_observed", "currency_ground_truth", "currency_match", "availability_observed", "availability_ground_truth", "availability_match",
    "sku_observed", "sku_ground_truth", "sku_match", "gtin_observed", "gtin_ground_truth", "gtin_match"
]

with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(ground_truth_rows)

print(f"Generated {out_path} with {len(ground_truth_rows)} ground truth records.")

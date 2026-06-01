import os
import pandas as pd

from pipeline_a.ocr_llm import extract_invoice_ocr_llm
from pipeline_b.azure_invoice_extractor import extract_invoice_azure
from validator.compare_results import compare_results

INPUT_FOLDER = "input_images"

results = []

for image_file in os.listdir(INPUT_FOLDER):

    if image_file.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):

        image_path = os.path.join(
            INPUT_FOLDER,
            image_file
        )

        print(f"Processing {image_file}")

        ocr_result = extract_invoice_ocr_llm(
            image_path
        )

        azure_result = extract_invoice_azure(
            image_path
        )

        results.append({
            "image_name": image_file,

            "ocr_invoice_number":
                ocr_result["invoice_number"],

            "azure_invoice_number":
                azure_result["invoice_number"],

            "ocr_invoice_date":
                ocr_result["invoice_date"],

            "azure_invoice_date":
                azure_result["invoice_date"],

            "ocr_vendor_name":
                ocr_result["vendor_name"],

            "azure_vendor_name":
                azure_result["vendor_name"],

            "ocr_total_amount":
                ocr_result["total_amount"],

            "azure_total_amount":
                azure_result["total_amount"]
        })

df = pd.DataFrame(results)

os.makedirs("outputs", exist_ok=True)

output_file = "outputs/output.csv"

df.to_csv(output_file, index=False)

report_df = compare_results(df)

report_file = (
    "outputs/comparison_report.csv"
)

report_df.to_csv(
    report_file,
    index=False
)

print(f"Saved: {output_file}")
print(f"Saved: {report_file}")

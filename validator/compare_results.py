import pandas as pd


def compare_results(df):

    report = []

    for _, row in df.iterrows():

        score = 0

        if row["ocr_invoice_number"] == row["azure_invoice_number"]:
            score += 1

        if row["ocr_invoice_date"] == row["azure_invoice_date"]:
            score += 1

        if row["ocr_vendor_name"] == row["azure_vendor_name"]:
            score += 1

        if row["ocr_total_amount"] == row["azure_total_amount"]:
            score += 1

        accuracy = (score / 4) * 100

        report.append({
            "image_name": row["image_name"],
            "accuracy": accuracy
        })

    return pd.DataFrame(report)

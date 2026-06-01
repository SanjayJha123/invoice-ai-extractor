import os

from azure.core.credentials import AzureKeyCredential

from azure.ai.documentintelligence import (
    DocumentIntelligenceClient
)

AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_KEY = os.getenv("AZURE_KEY")


client = DocumentIntelligenceClient(
    endpoint=AZURE_ENDPOINT,
    credential=AzureKeyCredential(AZURE_KEY)
)


def extract_invoice_azure(image_path):

    with open(image_path, "rb") as f:

        poller = client.begin_analyze_document(
            "prebuilt-invoice",
            body=f
        )

        result = poller.result()

    invoice_number = ""
    invoice_date = ""
    vendor_name = ""
    total_amount = ""

    if result.documents:

        doc = result.documents[0]

        fields = doc.fields

        if "InvoiceId" in fields:
            invoice_number = fields["InvoiceId"].value_string

        if "InvoiceDate" in fields:
            invoice_date = str(fields["InvoiceDate"].value_date)

        if "VendorName" in fields:
            vendor_name = fields["VendorName"].value_string

        if "InvoiceTotal" in fields:
            total_amount = str(
                fields["InvoiceTotal"].value_currency.amount
            )

    return {
        "invoice_number": invoice_number,
        "invoice_date": invoice_date,
        "vendor_name": vendor_name,
        "total_amount": total_amount
    }

from pydantic import BaseModel


class InvoiceSchema(BaseModel):
    image_name: str

    seller_name: str = ""
    seller_tax_id: str = ""

    client_name: str = ""
    client_tax_id: str = ""

    invoice_number: str = ""
    invoice_date: str = ""

    net_worth: str = ""
    vat: str = ""
    gross_worth: str = ""

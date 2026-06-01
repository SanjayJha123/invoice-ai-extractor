# Invoice AI Extractor

## Objective

Compare two invoice extraction approaches:

1. OCR + LLM
2. Azure Document Intelligence

## Setup

```bash
pip install -r requirements.txt
```

## Configure Azure

```bash
export AZURE_ENDPOINT=<endpoint>
export AZURE_KEY=<key>
```

## Run

```bash
python main.py
```

## Outputs

### output.csv

Contains extracted fields from both pipelines.

### comparison_report.csv

Contains accuracy comparison.

## Fields Extracted

- Invoice Number
- Invoice Date
- Vendor Name
- Total Amount

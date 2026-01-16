# Medical Document Processing Pipeline

A Kedro pipeline for processing French medical documents with OCR, event extraction using DrBERT, and patient timeline aggregation.

## Overview

This project implements a complete end-to-end pipeline for extracting structured clinical information from French medical documents. The pipeline consists of 8 sequential nodes organized into 3 stages:

### Stage 1: Data Engineering (Harmonization)
1. **OCR Text Extraction**: Extracts and standardizes text from PDF and TXT files with OCR support
2. **Text Normalization**: Normalizes and cleans French medical text, handles abbreviations and OCR artifacts

### Stage 2: Data Science (Detection & Extraction)
3. **Date Detection**: Detects all dates within medical documents using French date patterns
4. **Event Span Classification**: Multi-label classification using DrBERT to detect clinical events (Diagnosis, Treatment, Complications, Follow-up)
5. **Date-Event Association**: Links each detected event to its corresponding date

### Stage 3: Aggregation & Reporting
6. **Patient Longitudinal Aggregator**: Aggregates document-level data into patient-level chronological timelines
7. **Ambiguity Confidence Flagging**: Calculates confidence levels and flags ambiguous associations
8. **Evaluation Metrics**: Tracks Precision, Recall, F1-score, execution time, and memory usage

## Project Structure

```
data_challenge/
├── conf/
│   ├── base/
│   │   ├── catalog.yml          # Data catalog definitions
│   │   └── parameters.yml       # Pipeline parameters
├── src/
│   └── data_challenge/
│       ├── __init__.py
│       ├── pipeline_registry.py  # Pipeline registration
│       ├── pipelines/
│       │   ├── __init__.py
│       │   └── medical_processing/
│       │       ├── __init__.py
│       │       ├── nodes.py      # 8 node functions
│       │       └── pipeline.py   # Pipeline definition
│       └── settings.py
├── README.md
├── pyproject.toml               # Project dependencies
└── .gitignore
```

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/rosanajurdi/data_challenge.git
cd data_challenge
```

2. Install dependencies:
```bash
pip install -e .
```

3. For development dependencies:
```bash
pip install -e ".[dev]"
```

## Usage

### Running the Pipeline

To run the complete medical document processing pipeline:

```bash
kedro run
```

To run specific pipeline stages:

```bash
# Data Engineering stage only
kedro run --tags=data_engineering

# Data Science stage only
kedro run --tags=data_science

# Aggregation & Reporting stage only
kedro run --tags=aggregation,evaluation
```

To run individual nodes:

```bash
kedro run --node=ocr_text_extraction_node
kedro run --node=event_span_classification_node
```

### Visualizing the Pipeline

To visualize the pipeline structure:

```bash
kedro viz
```

## Data Requirements

### Input Data

Place your input data in the following locations:

- **Raw Medical Documents**: `data/01_raw/medical_docs/` (PDF or TXT files)
- **Patient Metadata**: `data/01_raw/patient_metadata.pkl` (optional, maps document IDs to patient IDs)
- **Ground Truth**: `data/01_raw/ground_truth.pkl` (optional, for evaluation)

### Output Data

Pipeline outputs are stored in:

- **Intermediate Results**: `data/02_intermediate/`, `data/03_primary/`, `data/04_feature/`
- **Model Outputs**: `data/05_model_input/`, `data/06_model_output/`
- **Reports**: `data/08_reporting/performance_report.json`

## Configuration

### Parameters

Edit `conf/base/parameters.yml` to customize:

- Event types to detect
- DrBERT model configuration
- Confidence thresholds
- Date formats
- Text normalization settings
- Aggregation settings

### Data Catalog

Edit `conf/base/catalog.yml` to customize:

- Input/output data sources
- Data formats and locations
- Dataset types

## Implementation Status

This is a skeleton implementation with TODO comments indicating where actual logic needs to be implemented:

- [ ] OCR library integration (pytesseract, pdf2image)
- [ ] French text normalization
- [ ] Date detection with French patterns
- [ ] DrBERT model loading and inference
- [ ] Temporal association logic
- [ ] Patient timeline aggregation and deduplication
- [ ] Confidence scoring algorithm
- [ ] Evaluation metrics calculation

## Dependencies

Key dependencies:
- **kedro**: Pipeline framework
- **transformers**: For DrBERT model
- **torch**: Deep learning backend
- **pandas**: Data manipulation

See `pyproject.toml` for complete list.

## Development

### Testing

```bash
pytest tests/
```

### Code Formatting

```bash
black src/
isort src/
```

### Linting

```bash
flake8 src/
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
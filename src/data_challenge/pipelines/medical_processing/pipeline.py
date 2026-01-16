"""
Medical document processing pipeline definition.

Single pipeline with 8 sequential nodes covering:
- Data Engineering (OCR + normalization)
- Data Science (detection + extraction + association)
- Aggregation & Reporting (timelines + confidence + metrics)
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    ocr_text_extraction,
    text_normalization,
    date_detection,
    event_span_classification,
    date_event_association,
    patient_longitudinal_aggregator,
    ambiguity_confidence_flagging,
    evaluation_metrics,
)


def create_pipeline(**kwargs) -> Pipeline:
    """
    Create the medical document processing pipeline.
    
    Returns:
        Pipeline: Kedro pipeline with all 8 nodes in sequence
    """
    return pipeline(
        [
            # ================================================================
            # STAGE 1: DATA ENGINEERING (HARMONIZATION)
            # ================================================================
            node(
                func=ocr_text_extraction,
                inputs="raw_medical_docs",
                outputs="extracted_raw_text",
                name="ocr_text_extraction_node",
                tags=["data_engineering", "preprocessing"],
            ),
            node(
                func=text_normalization,
                inputs="extracted_raw_text",
                outputs="primary_harmonized_text",
                name="text_normalization_node",
                tags=["data_engineering", "preprocessing"],
            ),
            # ================================================================
            # STAGE 2: DATA SCIENCE (DETECTION & EXTRACTION)
            # ================================================================
            node(
                func=date_detection,
                inputs="primary_harmonized_text",
                outputs="document_dates",
                name="date_detection_node",
                tags=["data_science", "extraction"],
            ),
            node(
                func=event_span_classification,
                inputs=["primary_harmonized_text", "params:medical_processing"],
                outputs="event_predictions",
                name="event_span_classification_node",
                tags=["data_science", "extraction", "ml"],
            ),
            node(
                func=date_event_association,
                inputs=["document_dates", "event_predictions"],
                outputs="document_level_outputs",
                name="date_event_association_node",
                tags=["data_science", "association"],
            ),
            # ================================================================
            # STAGE 3: AGGREGATION & REPORTING
            # ================================================================
            node(
                func=patient_longitudinal_aggregator,
                inputs=["document_level_outputs", "patient_metadata"],
                outputs="patient_level_timelines",
                name="patient_longitudinal_aggregator_node",
                tags=["aggregation", "reporting"],
            ),
            node(
                func=ambiguity_confidence_flagging,
                inputs="patient_level_timelines",
                outputs="final_results_with_metadata",
                name="ambiguity_confidence_flagging_node",
                tags=["aggregation", "quality"],
            ),
            node(
                func=evaluation_metrics,
                inputs=["final_results_with_metadata", "ground_truth"],
                outputs="performance_report",
                name="evaluation_metrics_node",
                tags=["evaluation", "mlops"],
            ),
        ]
    )

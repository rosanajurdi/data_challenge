"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from data_challenge.pipelines.medical_processing import pipeline as mp

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines."""
    medical_processing_pipeline = mp.create_pipeline()
    
    return {
        "__default__": medical_processing_pipeline,
        "medical_processing": medical_processing_pipeline,
    }
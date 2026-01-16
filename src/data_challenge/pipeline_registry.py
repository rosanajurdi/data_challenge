"""Project pipelines registry."""

from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from data_challenge.pipelines import medical_processing as mp


def register_pipelines() -> Dict[str, Pipeline]:
    """
    Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    medical_processing_pipeline = mp.create_pipeline()
    
    return {
        "__default__": medical_processing_pipeline,
        "medical_processing": medical_processing_pipeline,
    }

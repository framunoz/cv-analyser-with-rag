"""
This is a boilerplate pipeline 'json2yaml'
generated using Kedro 0.19.12
"""

from kedro.pipeline import Pipeline, node, pipeline  # noqa

from .nodes import convert_json_to_yaml


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=convert_json_to_yaml,
            inputs="json_resume",
            outputs="resume",
            name="convert_json_to_yaml_node",
            tags=["conversion"],
        )
    ])

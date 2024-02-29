from c_custom_specs import experiment_name, experiment_spec
from kfp import components
from kfp.dsl import pipeline, ContainerOp
from kubeflow.katib import ApiClient

katib_experiment_launcher_op = components.load_component_from_url(
    "https://raw.githubusercontent.com/kubeflow/pipelines/master/components/kubeflow/katib-launcher/component.yaml"
)


@pipeline(
    name="Launch Katib Experiment",
    description="An example to launch Katib Experiment with custom logic",
)
def main():

    experiment_namespace = "luke"
    # Katib launcher component.
    # Experiment Spec should be serialized to a valid Kubernetes object.
    op = katib_experiment_launcher_op(
        experiment_name=experiment_name,
        experiment_namespace=experiment_namespace,
        experiment_spec=ApiClient().sanitize_for_serialization(experiment_spec),
        experiment_timeout_minutes=60,
        delete_finished_experiment=False,
    )

    # Output container to print the results.
    op_out = ContainerOp(
        name="best-hp",
        image="library/bash:4.4.23",
        command=["sh", "-c"],
        arguments=["echo Best HyperParameters: %s" % op.output],
    )


if __name__ == "__main__":
    from kfp.compiler import Compiler

    Compiler().compile(pipeline_func=main, package_path="pipeline.yaml")

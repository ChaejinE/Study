from kubeflow.katib import (
    V1beta1Experiment,
    V1beta1ExperimentSpec,
    V1beta1ObjectiveSpec,
    V1beta1AlgorithmSpec,
    V1beta1ParameterSpec,
    V1beta1FeasibleSpace,
    V1beta1TrialTemplate,
    V1beta1TrialParameterSpec,
    KatibClient,
)
from kubernetes.client import V1ObjectMeta

# Objective
_type = "maximize"
goal = 50
metric = "result"
objective = V1beta1ObjectiveSpec(type=_type, goal=50, objective_metric_name=metric)

# Algorithm
algorithm = V1beta1AlgorithmSpec(algorithm_name="grid")

# Paramters
parameters = [
    V1beta1ParameterSpec(
        name="x",
        parameter_type="int",
        feasible_space=V1beta1FeasibleSpace(min="0", max="50"),
    ),
    V1beta1ParameterSpec(
        name="y",
        parameter_type="int",
        feasible_space=V1beta1FeasibleSpace(min="0", max="50"),
    ),
]

# Trial Template
## # Trial Spec
main_container_name: str = "main-container"
image: str = "129231402580.dkr.ecr.ap-northeast-1.amazonaws.com/base_image:katib-test"
trial_spec = {
    "apiVersion": "batch/v1",
    "kind": "Job",
    "spec": {
        "template": {
            "metadata": {"annotations": {"sidecar.istio.io/inject": "false"}},
            "spec": {
                "containers": [
                    {
                        "name": main_container_name,
                        "image": image,
                        "command": ["python"],
                        "args": [
                            "--x",
                            "${trialParameters.X}",
                            "--y",
                            "${trialParameters.Y}",
                        ],
                    }
                ],
                "restartPolicy": "Never",
            },
        }
    },
}

## Template
trial_template = V1beta1TrialTemplate(
    retain=True,
    primary_container_name=main_container_name,
    trial_parameters=[
        V1beta1TrialParameterSpec(
            name="X",
            description="argument 1",
            reference="x",
        ),
        V1beta1TrialParameterSpec(
            name="Y",
            description="argument 2",
            reference="y",
        ),
    ],
    trial_spec=trial_spec,
)

max_trial_count = 1
max_failed_trial_count = 1
parallel_trial_count = 1
experiment_spec = V1beta1ExperimentSpec(
    max_trial_count=max_trial_count,
    max_failed_trial_count=max_failed_trial_count,
    parallel_trial_count=parallel_trial_count,
    objective=objective,
    algorithm=algorithm,
    parameters=parameters,
    trial_template=trial_template,
)

experiment_name = "katib-example"
experiment = V1beta1Experiment(
    api_version="kubeflow.org/v1beta1",
    kind="Experiment",
    metadata=V1ObjectMeta(name=experiment_name),
    spec=experiment_spec,
)

kclient = KatibClient()
kclient.create_experiment(experiment, namespace="luke")
kclient.get_logs(name=experiment_name, master=True, follow=True)

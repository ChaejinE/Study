from typing import Union
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

import logging
import os

logging.basicConfig(level=logging.INFO)


class KatibInterface:
    def __init__(self, namespace=os.getenv("NAMESPACE", default=None)) -> None:
        self._objective: Union[V1beta1ObjectiveSpec, None] = None
        self._algorithm: Union[V1beta1AlgorithmSpec, None] = None
        self._parameters: list[V1beta1ParameterSpec] = []
        self._trial_spec: dict = dict()
        self._trial_parameter_spec: list = list()
        self._trial_template: Union[V1beta1TrialTemplate, None] = None
        self._experiment_spec: Union[V1beta1ExperimentSpec, None] = None
        self._experiment: Union[V1beta1Experiment, None] = None
        self._client: Union[KatibClient, None] = KatibClient(namespace=namespace)

    @property
    def objective(self) -> V1beta1ObjectiveSpec:
        assert self.is_defined([self._objective]), "Define objective spec"
        return self._objective

    def set_objective(
        self, objective_type: str, goal: Union[int, float], objective_metric: str
    ):
        self._objective = V1beta1ObjectiveSpec(
            type=objective_type, goal=goal, objective_metric_name=objective_metric
        )

    @property
    def algorithm(self) -> V1beta1AlgorithmSpec:
        assert self.is_defined([self._algorithm]), "Define algorithm spec"
        return self._algorithm

    def set_algorithm(self, name: str) -> None:
        self._algorithm = V1beta1AlgorithmSpec(algorithm_name=name)

    @property
    def parameters(self) -> list[V1beta1ParameterSpec]:
        assert self.is_defined([self._parameters]), "Define parameters spec"
        return self._parameters

    def set_parameters(self, parameter_specs: list[V1beta1ParameterSpec]) -> None:
        self._parameters = parameter_specs

    def add_parameter_spec(
        self, name: str, parameter_type: Union[int, float, list], feasible_space: dict
    ) -> None:
        if issubclass(parameter_type, (int, list)):
            parameter_type = parameter_type.__name__
        elif issubclass(parameter_type, float):
            parameter_type = "double"
        else:
            raise ValueError(f"Unknown parameter type : {parameter_type}")
        logging.info(f"parameter type is {parameter_type}, {type(parameter_type)}")

        spec = V1beta1ParameterSpec(
            name=name,
            parameter_type=parameter_type,
            feasible_space=V1beta1FeasibleSpace(
                list=feasible_space.get("list"),
                max=str(feasible_space.get("max")),
                min=str(feasible_space.get("min")),
            ),
        )
        self._parameters.append(spec)

    @property
    def trial_spec(self) -> dict:
        assert self.is_defined([self._trial_spec]), "Define trial spec"
        return self._trial_spec

    def set_trial_spec(
        self,
        container_name: str,
        repository: str,
        image: str,
        tag: str,
        command: list,
        args: list,
        api_version: str = "batch/v1",
        kind: str = "Job",
    ):
        self._trial_spec.update(
            {
                "apiVersion": api_version,
                "kind": kind,
                "spec": {
                    "template": {
                        "metadata": {
                            "annotations": {"sidecar.istio.io/inject": "false"}
                        },
                        "spec": {
                            "containers": [
                                {
                                    "name": container_name,
                                    "image": f"{repository}/{image}:{tag}",
                                    "command": command,
                                    "args": args,
                                }
                            ],
                            "restartPolicy": "Never",
                        },
                    }
                },
            }
        )

    @property
    def trial_template(self) -> V1beta1TrialTemplate:
        assert self.is_defined([self._trial_template]), "Define trial template"
        return self._trial_template

    def set_trial_template(
        self,
        primary_container_name: str,
        trial_paramters: list[V1beta1TrialParameterSpec] = [],
    ) -> None:
        if not trial_paramters:
            trial_paramters = self.trial_parameter_spec

        self._trial_template = V1beta1TrialTemplate(
            retain=True,
            primary_container_name=primary_container_name,
            trial_parameters=trial_paramters,
            trial_spec=self.trial_spec,
        )

    @property
    def trial_parameter_spec(self) -> list[V1beta1TrialParameterSpec]:
        assert self.is_defined(
            [self._trial_parameter_spec]
        ), "Define trial parameter spec"
        return self._trial_parameter_spec

    def add_trial_parameter_spec(
        self, name: str, description: str, reference: str
    ) -> None:
        spec = V1beta1TrialParameterSpec(
            name=name, description=description, reference=reference
        )
        self._trial_parameter_spec.append(spec)

    @property
    def experiment_spec(self) -> V1beta1ExperimentSpec:
        assert self.is_defined([self._experiment_spec]), "Define experiment spec"
        return self._experiment_spec

    def set_experiment_spec(
        self,
        max_trial_count: int,
        max_failed_trial_count: int,
        parallel_trial_count: int,
    ) -> None:
        self._experiment_spec = V1beta1ExperimentSpec(
            max_trial_count=max_trial_count,
            max_failed_trial_count=max_failed_trial_count,
            parallel_trial_count=parallel_trial_count,
            objective=self.objective,
            algorithm=self.algorithm,
            parameters=self.parameters,
            trial_template=self.trial_template,
        )

    @property
    def experiment(self) -> V1beta1Experiment:
        assert self.is_defined([self._experiment]), "Define experiment"
        return self._experiment

    def set_experiment(
        self,
        experiment_name: str,
        api_version: str = "kubeflow.org/v1beta1",
        kind: str = "Experiment",
    ) -> None:
        self._experiment = V1beta1Experiment(
            api_version=api_version,
            kind=kind,
            metadata=V1ObjectMeta(name=experiment_name),
            spec=self.experiment_spec,
        )

    def is_defined(self, variables: list) -> bool:
        for var in variables:
            if not var:
                return False
        return True

    def make_trial_parameter_name(self, parameter_name: str) -> str:
        """Make parameter name for trials

        Args:
            parameter_name (str): source parameter

        Returns:
            str: converted parameter
                eq) ${trialsParameters.<parametername>}
        """
        name = "${trialParameters." + parameter_name + "}"
        logging.info(f"trials parameter name : {name}")
        return name

    def run_experiment(self):
        self._client.create_experiment(self.experiment)


if __name__ == "__main__":
    interface = KatibInterface(namespace="")
    # Objective
    interface.set_objective(
        objective_type="maximize", goal=50, objective_metric="result"
    )
    # Algorithm
    interface.set_algorithm(name="grid")
    # Parameters
    parameter_name_1 = "x"
    interface.add_parameter_spec(
        name=parameter_name_1, parameter_type=int, feasible_space={"min": 0, "max": 50}
    )
    parameter_name_2 = "y"
    interface.add_parameter_spec(
        name=parameter_name_2, parameter_type=int, feasible_space={"min": 0, "max": 50}
    )
    # Trial Template
    ## Trial parameters
    trial_parameter_name_1 = parameter_name_1.upper()
    interface.add_trial_parameter_spec(
        name=trial_parameter_name_1,
        description="first argument",
        reference=parameter_name_1,
    )
    trial_parameter_name_2 = parameter_name_2.upper()
    interface.add_trial_parameter_spec(
        name=trial_parameter_name_2,
        description="second argument",
        reference=parameter_name_2,
    )
    ## Trial spec
    container_name = "experiment-container"
    ecr_image = ""
    interface.set_trial_spec(
        container_name=container_name,
        repository=ecr_image.split(":")[0].split("/")[0],
        image=ecr_image.split(":")[0].split("/")[1],
        tag=ecr_image.split(":")[-1],
        command=["python"],
        args=[
            "custom.py",
            "--x",
            interface.make_trial_parameter_name(parameter_name=trial_parameter_name_1),
            "--y",
            interface.make_trial_parameter_name(parameter_name=trial_parameter_name_2),
        ],
    )
    ## Trial Template
    interface.set_trial_template(primary_container_name=container_name)

    # Experiment
    ## Experiment spec
    interface.set_experiment_spec(
        max_trial_count=3, max_failed_trial_count=3, parallel_trial_count=2
    )
    ## Experiment
    interface.set_experiment(experiment_name="oh-my-test")
    ## Run
    interface.run_experiment()

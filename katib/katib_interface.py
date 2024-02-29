from typing import List, Union
from kubeflow.katib import (
    V1beta1Experiment,
    V1beta1ExperimentSpec,
    V1beta1ObjectiveSpec,
    V1beta1AlgorithmSpec,
    V1beta1ParameterSpec,
    V1beta1FeasibleSpace,
    V1beta1TrialTemplate,
    V1beta1TrialParameterSpec,
)


class KatibInterface:
    def __init__(self) -> None:
        self._objective: V1beta1ObjectiveSpec = ""
        self._algorithm: V1beta1AlgorithmSpec = ""
        self._parameters: List[V1beta1ParameterSpec] = ""
        self._trial_template: V1beta1TrialTemplate = ""
        self._experiment_spec: V1beta1ExperimentSpec = ""
        self._experiment: V1beta1Experiment = ""

    @property
    def objective(self):
        return self._objective

    @objective.setter
    def objective(self, objective_type: str, goal: Union[int, float], objective_metric: str):
        self._objective = V1beta1ObjectiveSpec(type=objective_type, goal=goal, objective_metric_name=objective_metric)

    @property
    def algorithm(self):
        return self._algorithm

    @algorithm.setter
    def algorithm(self, name: str):
        self._algorithm = V1beta1AlgorithmSpec(algorithm_name=name)

    @property
    def parameters(self):
        return self._parameters

    def set_parameters(self, parameter_spec: dict):
        pass

    def set_trial_template(
        self,
        container_name: str,
        repository: str,
        image: str,
        tag: str,
        command: list,
        args: list,
        kubernetes_kind: str = "Job",
    ):
        pass

    def set_experiment_spec(self, max_trial_count: int, max_failed_trial_count: int, parallel_trial_count: int):
        pass

    def set_experiment(self, api_version: str, kind: str, experiment_name: str):
        pass

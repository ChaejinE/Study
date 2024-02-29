from kubeflow.katib import KatibClient
from c_custom_specs import experiment
import os

kclient = KatibClient()
namespace = os.getenv("NAMESPACE")
kclient.create_experiment(experiment, namespace=namespace)

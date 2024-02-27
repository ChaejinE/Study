import kubeflow.katib as katib


def objective(parameters):
    import time

    time.sleep(5)

    result = 4 * int(parameters["a"]) - float(parameters["b"]) ** 2
    print(f"result = {result}")


parameters = {
    "a": katib.search.int(min=10, max=20),
    "b": katib.search.double(min=0.1, max=0.2),
}

NAMESPACE=""
katib_client = katib.KatibClient(namespace=NAMESPACE)

# print(katib_client.list_experiments())
name = "tune-experiment"
katib_client.tune(
    name=name, objective=objective, parameters=parameters, objective_metric_name="result", max_trial_count=12, resources_per_trial={"gpu": "1"}
)

print(katib_client.get_optimal_hyperparameters(name))

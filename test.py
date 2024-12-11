import mlflow

mlflow.set_tracking_uri('https://mlflow.cerbo.stg-gdcorp.tools/')

# Uncomment to load sklearn model
mlflow_model = mlflow.sklearn.load_model(model_uri=f"models:/propensity-m365+obe_bp-us-v1/1")

# Uncomment to load pytorch model
#mlflow_model = mlflow.pyfunc.load_model(model_uri=f"models:/heuristic-segmentation-m365/4")

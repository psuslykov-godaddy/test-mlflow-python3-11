import mlflow

mlflow.set_tracking_uri('https://mlflow.cerbo.stg-gdcorp.tools/')
#mlflow_model = mlflow.sklearn.load_model(model_uri=f"models:/propensity-com-usind/8")
mlflow_model = mlflow.pyfunc.load_model(model_uri=f"models:/heuristic-segmentation-m365/4")

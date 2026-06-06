# from airflow.decorators import dag, task
# from datetime import datetime

# from src.extract_data_layer import load_data
# from src.clean_data_layer import clean_data, check_nulls, fill_values
# from src.validate_data_layer import validate_data
# from src.audit_layer import audit_data
# from src.reconcile_layer import reconcile_data


# @dag(
#     dag_id="agri_pipeline",
#     start_date=datetime(2026, 1, 1),
#     schedule="@daily",
#     catchup=False,
# )
# def agri_pipeline_taskflow():

#     @task
#     def load():
#         return load_data()

#     @task
#     def null_check(data):
#         check_nulls(data)
#         return data

#     @task
#     def fill_null(data):
#         return fill_values(data)

#     @task
#     def clean(data):
#         return clean_data(data)

#     @task
#     def validate(data):
#         return validate_data(data)

#     @task
#     def audit(data):
#         return audit_data(data)

#     @task
#     def reconcile(original_data, audited_data):
#         return reconcile_data(
#             original_data,
#             audited_data
#         )

#     # Pipeline Flow

#     loaded_data = load()

#     checked_data = null_check(loaded_data)

#     filled_data = fill_null(checked_data)

#     cleaned_data = clean(filled_data)

#     validated_data = validate(cleaned_data)

#     audited_data = audit(validated_data)

#     reconcile(
#         loaded_data,
#         audited_data
#     )


# dag = agri_pipeline_taskflow()
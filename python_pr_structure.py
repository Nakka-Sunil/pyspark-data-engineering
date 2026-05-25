from pathlib import Path

project_name = "agri_pipeline_project"

root = Path(project_name)

folders = [
    "data/raw",
    "data/cleaned",
    "output/reports",
    "output/parquet",
    "logs",
    "sql",
    "src"
]

for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

files = [
    "src/main.py",
    "src/clean_data.py",
    "src/validate_data.py",
    "src/reconcile_data.py",
    "sql/queries.sql",
    "config.yaml",
    "README.md",
    "logs/pipeline.log"
]

for file in files:
    file_path = root / file
    file_path.touch(exist_ok=True)

print(f"{project_name} structure created successfully.")
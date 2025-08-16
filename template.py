import os
from pathlib import Path   

project_root = "us_visa"
list_of_templates = [

    f"{project_root}/__init__.py",
    f"{project_root}/components/__init__.py",
    f"{project_root}/components/data_ingestion.py",
    f"{project_root}/components/data_transformation.py",
    f"{project_root}/components/model_trainer.py",
    f"{project_root}/components/model_evaluation.py",
    f"{project_root}/components/model_pusher.py",
    f"{project_root}/configuration/__init__.py",
    f"{project_root}/constants/__init__.py",
    f"{project_root}/entity/__init__.py",
    f"{project_root}/entity/artifact_entity.py",
    f"{project_root}/entity/config_entity.py", 
    f"{project_root}/exception/__init__.py",
    f"{project_root}/logger/__init__.py",
    f"{project_root}/pipeline/__init__.py",
    f"{project_root}/pipeline/prediction_pipeline.py",
    f"{project_root}/pipeline/training_pipeline.py",
    f"{project_root}/utils/__init__.py",
    f"{project_root}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    "demo.py",
    "config/model.yaml",
    "config/schema.yaml",
    ".dockerignore",
]

for template in list_of_templates:
    template_path = Path(template)
    file_dir , file_name = os.path.split(template_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
    if(not os.path.exists(template_path)) or (os.path.getsize(template_path) == 0):
        with open(template_path, 'w') as file:
            pass
    else:
        print(f"{template_path} already exists and is not empty. Skipping creation.")

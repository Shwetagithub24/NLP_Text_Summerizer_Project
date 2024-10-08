import os
from pathlib import Path
import logging  # to log all the information

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name = "NLP_TextSummerization"

list_of_files = [
    ".github/workflows/.gitkeep",   #For CI/CD deployment_Commit code in github
    f"src/{project_name}/__init__.py",  #Constructor file to import components from other folders.
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py",   
    f"src/{project_name}/logging/__init__.py", 
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py", 
    f"src/{project_name}/entity/__init__.py", 
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",  
    "requirements.txt",
    "setup.py",  # Helps for local package setup
    "research/trails.ipynb"  # It will contain all the notebook experiments

]


for filepath in list_of_files:
    filepath = Path(filepath)  #TO handle / issues
    filedir,filename =  os.path.split(filepath)  #Seperate folder and file
    #check if Filedir is empty

    #If folder is not there, create new
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory:{filedir} for the file {filename}")

    #create file in filedir
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f"File {filename} already exists")


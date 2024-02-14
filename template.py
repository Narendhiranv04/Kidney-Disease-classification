import os
from pathlib import Path
import logging

#logging string 
#instead of using print statements everywhere we use logging statements to see the updates

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = 'cnnClassifier' #template name


list_of_files = [
    ".github/workflows/.gitkeep", #in case there are no files in the github repo
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constraints/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]   #files in the github repo


for filepath in list_of_files:
    filepath=Path(filepath)    #This is because in windows, file paths are in '\' but we have mentioned '/'. 
    #Therefore it is a convention to always do this step
    filedir, filename = os.path.split(filepath)

    if filedir!="": #if the directory does not exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")  #message is given to ther terminal via logging
    if (not os.path.exists(filepath) or (os.path.getsize(filepath) ==0)):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} laready exists")
        




import os


CONFIG_DIR=os.path.dirname(os.path.abspath(__file__))

ROOT_DIR=os.path.abspath(os.path.join(CONFIG_DIR,".."))

STORAGE_DIR=os.path.join(ROOT_DIR,"storage")

os.makedirs(STORAGE_DIR,exist_ok=True)
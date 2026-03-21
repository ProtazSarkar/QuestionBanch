import os
import json
from pylatex import Document, NoEscape

from config.config import ROOT_DIR,STORAGE_DIR

# ------------ PATH SETUP ------------
SERVICE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(SERVICE_DIR, "templates")

# ------------ LOAD SERVICE CONFIG ------------
configPath = os.path.join(SERVICE_DIR, "serviceConfig.json")

with open(configPath, "r") as f:
    SERVICE_CONFIG = json.load(f)


class CREATE_PAPER:

    def __init__(self):
        self.doc = Document(documentclass="article")

    # ---------------- INSTALL PACKAGES ----------------
    def install_packages(self):
        pkgPath = os.path.join(
            TEMPLATES_DIR,
            SERVICE_CONFIG["templates"]["packages"]
        )

        with open(pkgPath, "r") as f:
            content = f.read()

        self.doc.preamble.append(NoEscape(content))

    # ---------------- INSTALL FORMATS ----------------
    def install_formates(self, category, type="basic"):
        catPath = os.path.join(
            TEMPLATES_DIR,
            SERVICE_CONFIG["templates"][category][type]
        )

        with open(catPath, "r") as f:
            content = f.read()

        self.doc.preamble.append(NoEscape(content))

    # ---------------- TAGS PROVIDER ---------------
    def getTag(self,category,type="basic"):
        tag= SERVICE_CONFIG["tags"][category][type]
        print(f"The tag is {tag}")
        return tag
        
    # ---------------- ADD QUESTION ----------------
    def add_question(self, question_no,content,marks,type="basic"):
        tag = self.getTag(category="question", type=type)
        question_command = fr'{tag}{{{question_no}}}{{{content}}}{{{marks}}}'
        self.doc.append(NoEscape(question_command))

    # ---------------- GENERATE PDF ----------------
    def generate_pdf(self, filename):
        try:
            file_path=os.path.join(STORAGE_DIR,filename)
            self.doc.generate_pdf(file_path,clean_tex=False)
            print("pdf generate sucessfully")
        except Exception as e:
            raise e
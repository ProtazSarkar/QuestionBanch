import os
import json
from pylatex import Document, NoEscape

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
    def install_formats(self, category, type="basic"):
        catPath = os.path.join(
            TEMPLATES_DIR,
            SERVICE_CONFIG[category][type]
        )

        with open(catPath, "r") as f:
            content = f.read()

        self.doc.preamble.append(NoEscape(content))

    # ---------------- TAGS PROVIDER ---------------
    def getTag(catagory,type="basic"):
        return SERVICE_CONFIG["tags"][catagory][type]
        
    # ---------------- ADD QUESTION ----------------
    def add_question(self, question, type="basic"):
        tag = getTag(category="question", type=type)
        question_command = tag + question
        self.doc.append(NoEscape(question_command))

    # ---------------- GENERATE PDF ----------------
    def generate_pdf(self, filename):
        self.doc.generate_pdf(filename, clean_tex=False)
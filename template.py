from pathlib import Path
import os
import logging

directories ={
    "backend",
    "docs",
    "tests"
}

files={
    "backend/app.py",
    "backend/parser.py",
    "backend/metrics.py",
    "docs/product_requirement.md",
    "README.md"
}

for dir in directories:
    dir_path = Path(dir)
    dir_path.mkdir(parents=True,exist_ok=True)
    logging.info("directory created")

for file in files:
    file_path= Path(file)
    file_path.parent.mkdir(parents=True,exist_ok=True)

    if not file_path.exists():
        file_path.touch()
        logging.info(f"Created file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}") 
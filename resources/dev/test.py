"""
test.py
-------
Test workshop notebook content
"""
import nbformat
import logging
import pathlib
import sys
import os

from nbconvert.preprocessors import (
    ExecutePreprocessor,
    CellExecutionError
)

DEV_DIR = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
REPO_DIR = DEV_DIR.parent.parent.absolute()

def test_notebook(notebook_path):
    """Test a jupyter notebook."""
    logging.info(f'Testing notebook: {notebook_path}')
    with open(notebook_path, 'r', encoding='utf8') as raw_input:
        nb = nbformat.read(raw_input, as_version=4)
    ep = ExecutePreprocessor(
        timeout=600,
        allow_errors=False,
        kernel_name='python3'
    )
    try:
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
    except CellExecutionError:
        msg = f'Error executing the notebook {notebook_path}'
        logging.error(msg)
        raise

def main():
    """Run tests for all notebooks in workshop."""
    notebook_dir = REPO_DIR / 'workshop'
    notebooks = sorted(notebook_dir.glob('*/*.ipynb'))
    for notebook in notebooks:
        if 'exercise' in str(notebook).lower():
            continue  # Don't test exercise
        notebook_path = os.path.realpath(notebook)
        test_notebook(notebook_path)
    return 0

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    logging.info('Running notebook tests...')
    sys.exit(main())
"""Execute the clustering notebook while preserving its edited Markdown notes."""
import os
import sys
import asyncio
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
for key in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS']:
    os.environ[key] = '1'
os.environ['MPLBACKEND'] = 'module://matplotlib_inline.backend_inline'
from pathlib import Path
import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parent
path = root / 'clustering_initialization.ipynb'
nb = nbformat.read(path, as_version=4)
client = NotebookClient(nb, timeout=900, kernel_name='python3', resources={'metadata': {'path': str(root)}})
def log_cell(cell, cell_index, **kwargs):
    if cell.cell_type == 'code':
        print(f'Executing cell {cell_index}: {cell.id}', flush=True)
client.on_cell_start = log_cell
client.execute()
nbformat.validate(nb)
nbformat.write(nb, path)
print('Clustering notebook executed and saved.', flush=True)

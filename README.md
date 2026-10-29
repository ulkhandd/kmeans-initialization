# Clustering and initialization

Assignment 5 for Statistical Methods for Machine Learning, A.Y. 2025/26.
Author: Daniyar Ulkhan.

The project compares random initialization and k-means++ using a shared k-means update loop implemented with NumPy. It uses separated synthetic data and a fixed sample of 2,000 MNIST images. The extensions examine overlapping synthetic groups and additional irrelevant features. There are 20 runs per method in each of eight settings, giving 320 runs.

- [Executed notebook](clustering_initialization.ipynb)
- [Report (PDF)](clustering_report/report.pdf)
- [Editable LaTeX source](clustering_report/main.tex)
- [Individual run results](results/clustering/trials.csv)
- [Summary table](results/clustering/summary.csv)

## Run

The notebook was checked with Python 3.12.6. Install the dependencies and run:

```sh
python -m pip install -r clustering_requirements.txt
python run_clustering_notebook.py
```

Alternatively, open the notebook in Jupyter or VS Code and run all cells from top to bottom. The runner preserves the Markdown notes. MNIST is downloaded automatically from the archive used by Keras and cached locally; Keras and TensorFlow are not needed. Synthetic data are generated in the notebook, and fixed random seeds make the experiments repeatable.

The notebook writes the two result CSV files and the figures. The LaTeX source uses the images in `clustering_report/images/`; the submitted PDF is already included.

## Sources

- Arthur and Vassilvitskii (2007), [k-means++: The Advantages of Careful Seeding](https://research.google/pubs/k-means-the-advantages-of-careful-seeding/).
- [MNIST documentation](https://keras.io/api/datasets/mnist/) and [archive loader source](https://github.com/keras-team/keras/blob/master/keras/src/datasets/mnist.py). The Keras documentation states the dataset licence as CC BY-SA 3.0.
- [Course project instructions](https://docs.google.com/document/d/1JDqx6WXewBjtiyavpbXPFcB4uJ8KG2EhDKwnX-K8xQM/edit).

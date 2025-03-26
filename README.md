# Oil-parm-tree-YOLOv8

## Installation

Conda virtual environment is recommended.

```bash
# Create a new conda environment with Python 3.9
conda create -n yolov8 python=3.9

# Activate the environment
conda activate yolov8

# Install required packages from the requirements file
pip install -r requirements.txt

# Install the package in editable mode
pip install -e .

```

## Streamlit installation and run app

```bash
# Install streamlit
pip install streamlit

# Run streamlit web app on local host
streamlit run app.py
```

## Dataset

### Accessing Dataset
The dataset used in this project is the MOPAD, which can be accessed from the following link: https://github.com/rs-dl/MOPAD?tab=readme-ov-file

### Corrected Labels
The MOPAD dataset includes "Dead", "Healthy", "Small", "Yellow", and "Mismanaged" oil palm classes. This project uses a modified version of the MOPAD dataset with corrected labels, since several inconsistencies in labeling were identified. We addressed this issue and corrected the mislabeling, resulting in only four classes: "Dead", "Healthy", "Small", and "Yellow", labels available in [updated labels MOPAD dataset](https://github.com/SIIT-DL/Oil-parm-tree-YOLOv8/tree/main/updated%20labels%20MOPAD%20dataset).  


## Acknowledgements

The authors acknowledge the contributors of the MOPAD dataset and Ultralytics team. This project uses code from **Ultralytics**. You can find more about Ultralytics at the following link: [Ultralytics Repository](https://github.com/ultralytics)

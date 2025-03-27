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
The dataset used in this project is from the study [**MOPAD: A multi-class oil palm detection method in UAV images**](https://doi.org/10.1016/j.isprsjprs.2021.01.008), and can be accessed from the following GitHub link: [https://github.com/rs-dl/MOPAD](https://github.com/rs-dl/MOPAD)

### Corrected Labels
The original data used in the MOPAD study incldues five oil palm classes: "Dead", "Healthy", "Small", "Yellow", and "Mismanaged". This project uses a modified version of that dataset with corrected labels, since several inconsistencies in labeling were identified. We addressed this issue and corrected the mislabeling, resulting in only four classes: "Dead", "Healthy", "Small", and "Yellow", labels available in [here](https://github.com/SIIT-DL/Oil-parm-tree-YOLOv8/tree/main/updated%20labels%20MOPAD%20dataset).  


## Acknowledgements

The authors acknowledge the contributors of the datasetused in the MOPAD study and Ultralytics team. This project uses code from **Ultralytics**. You can find more about Ultralytics at the following link: [Ultralytics Repository](https://github.com/ultralytics)

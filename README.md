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

## Updated Dataset MOPAD

```bash
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="tV2NdldKtjE2DvIrG2y5")
project = rf.workspace("aakash-thapa-5qpod").project("palm-tree-yalqu")
version = project.version(4)
dataset = version.download("yolov8")
```

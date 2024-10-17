import streamlit as st
import subprocess
import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import glob
import shutil
import re  # Import the regex module

# Set Streamlit page configuration to centered layout
st.set_page_config(page_title="Oil Palm Tree Object Detection using YOLOv8", layout="centered")

# Define the correct path to your trained weights
MODEL_PATH = r'Y:\aakash\yolov8\runs\detect\train\weights\best.pt'

# Set the temporary directory within the YOLOv8 folder
TEMP_DIR = r'Y:\aakash\yolov8\prediction'  # Set a specific folder name 'prediction' for temporary use

# Ensure the temporary directory exists and is clean
if os.path.exists(TEMP_DIR):
    shutil.rmtree(TEMP_DIR)  # Remove existing folder if any to start fresh
os.makedirs(TEMP_DIR, exist_ok=True)  # Create the 'prediction' folder

# Streamlit app setup
st.title("Oil Palm Tree Object Detection using YOLOv8")

# File uploader for image input, allowing multiple file uploads
uploaded_files = st.file_uploader("Choose one or more images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    # Save the uploaded images temporarily in the specified temporary directory
    temp_image_paths = []
    for uploaded_file in uploaded_files:
        temp_image_path = os.path.join(TEMP_DIR, uploaded_file.name)
        image = Image.open(uploaded_file)
        image.save(temp_image_path)
        temp_image_paths.append(temp_image_path)

    # Set up two columns for displaying images and results, both covering half of the width
    col1, col2 = st.columns(2)  # Two columns of equal width

    with col1:
        st.write("Uploaded Images")
        for temp_image_path in temp_image_paths:
            image = Image.open(temp_image_path)
            st.image(image, caption=f'Uploaded Image: {os.path.basename(temp_image_path)}', use_column_width=True)

    # Check if the model weights file exists
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model weights file not found at: {MODEL_PATH}")
    else:
        # Define the YOLO command to run for each uploaded image
        def run_yolo_command(temp_image_paths):
            try:
                # Display predicted images in the second column
                with col2:
                    st.write("Prediction Results")

                for i, temp_image_path in enumerate(temp_image_paths):
                    # Define a unique name for each run to avoid conflicts
                    run_name = f"run_{i}"

                    # Define the YOLO command for each image
                    command = [
                        "yolo",
                        "task=detect",
                        "mode=predict",
                        f"model={MODEL_PATH}",
                        f"source={temp_image_path}",
                        "save=True",
                        f"project={TEMP_DIR}",
                        f"name={run_name}"
                    ]
                    
                    # Run the YOLO command using subprocess
                    result = subprocess.run(" ".join(command), capture_output=True, text=True, shell=True)

                    if result.returncode != 0:
                        st.error(f"Error running YOLO command for {os.path.basename(temp_image_path)}: {result.stderr}")
                    else:
                        # Locate the predicted image in the specified 'prediction' directory using the unique run name
                        predict_dir = os.path.join(TEMP_DIR, run_name)
                        predicted_image_paths = glob.glob(os.path.join(predict_dir, "*.jpg"))  # Find all predicted images

                        # Display all predicted images found in the run directory
                        if predicted_image_paths:
                            for predicted_image_path in predicted_image_paths:
                                with col2:
                                    output_image = Image.open(predicted_image_path)
                                    st.image(output_image, caption='Prediction Result', use_column_width=True)
                        else:
                            st.error(f"Could not find the predicted output images for {os.path.basename(temp_image_path)}.")

                # Add a single, smaller legend with class labels below all predicted images
                with col2:
                    fig, ax = plt.subplots(figsize=(3, 0.3))  # Smaller and more compact legend size
                    ax.axis('off')
                    class_labels = ['Dead', 'Small', 'Healthy', 'Yellow']
                    class_colors = ['brown', 'blue', 'green', 'yellow']  # Adjust colors as per your model settings

                    # Create patches with colored borders and transparent fill
                    patches = [mpatches.Rectangle((0, 0), 1, 1, edgecolor=color, facecolor='none', lw=2) for color in class_colors]
                    ax.legend(handles=patches, labels=class_labels, loc='center', ncol=4, frameon=False)
                    st.pyplot(fig)

            except Exception as e:
                st.error(f"Failed to execute YOLO command: {e}")

        # Run the YOLO command when the button is clicked
        if st.button("Run YOLO Detection"):
            run_yolo_command(temp_image_paths)

    # Clean up the temporary files after display
    for temp_image_path in temp_image_paths:
        os.remove(temp_image_path)

    # Optionally clean up the entire 'prediction' directory after use
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)  # Remove the entire 'prediction' directory
else:
    st.info("Please upload one or more images to get started.")

Step 1: Download the dataset from https://www.fsoco-dataset.com/download \\

Step 2: Convert the dataset using https://www.fsoco-dataset.com/tools/ or https://github.com/fsoco/fsoco-dataset/tree/master/tools \\

Step 3: Create Conda environment with the following configurations:
	``# Create new environment with Python 3.8
	conda create -n fsoco python=3.8

	# Activate created environment
	conda activate fsoco

	# Upgrade pip to version 19.3.0 or later
	pip install --upgrade pip

	# Install setuptools version 60.8.2 as version 60.9.0 introduced a bug.
	pip install setuptools==60.8.2

	# Make sure you are in the tools directory, otherwise adjust the '.' path to point to it.
	# Use Setuptools configuration to install tools to environment
	# For usage of the CLI tools only
	pip install --editable .[sly]
	# For development
	pip install -r requirements.txt
	pre-commit install

	# You have just installed the FSOCO Tools Python package
	# Have a look at the usage help with (when executed the first time, this can take some seconds):
	fsoco --help
 
	# As long as the environment is activated you can use the tools from wherever.
	# Some of the scripts expect a default directory structure, please make sure
	# to read the help tooltips before executing them or set the according options correctly.``

Step 4: Convert the dataset from Supervisely format to Yolo format
	``$ fsoco label-converts sly2yolo project_folder output_folder``

Step 5: Train your yolo model with the converted dataset
	


# EECS3342 Grading Scripts

This repository contains a set of scripts used for grading assignments in the EECS3342 course. The scripts take input data, validate it, generate feedback, and produce output files based on the grading criteria.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Troubleshooting](#troubleshooting)
  
## Prerequisites
Before you can run the grading scripts, make sure you have the following installed:

1. **Python 3.6+**
2. Required Python packages (see below for installation instructions).

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd EECS3342_Grading_Scripts-main
   ```

2. **Install required Python packages**:
   Install the necessary packages listed in the `requirements.txt` or that are used in the scripts. You can create a virtual environment for easier management.
   
   **Install the packages**:
   Install the required packages:
   ```bash
   pip install openpyxl
   ```
   If you are encountering issues installing the packages using pip or brew, create a virtual-envirnoment
      **Optional: Create a virtual environment**:
   ```bash
   python3 -m venv path/to/venv
   source path/to/venv/bin/activate   # On Windows: venv\Scripts\activate
   python3 -m pip install openpyxl
   ```

   Make sure all required dependencies are installed before running the scripts.

## How to Run

The main grading process can be run using the following steps:

1. **Prepare Input Data**:
   Place your input files inside the `inputs/` directory. These files will be processed by the scripts.
   - **constants.py**: Contains global constants used across multiple scripts. Please make sure to modify the values as needed.

3. **Run the grading script**:
   To run the entire grading process, execute the `run.sh` shell script which triggers all necessary scripts (validation, feedback generation, etc.):
   ```bash
   bash run.sh
   ```
  Note that feedback will only be generated if all the assumptions are satisifed.

3. **View Output**:
   After running the scripts, results will be saved in the `outputs/` directory. Review the output files for feedback and grading information. Each student's feedback can be found with their respective {eecs_login}.txt

## Troubleshooting

### Python not installed

#### On Linux
To install Python 3 on a Linux distribution like Ubuntu:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### On macOS
Python 3 may already be installed on macOS. You can check using:
```bash
python3 --version
```
If it's not installed, use `brew` to install Python:
```bash
brew install python
```

#### On Windows
Download and install Python from the official Python website:
[Download Python](https://www.python.org/downloads/windows/)

Make sure to add Python to your system's PATH during installation.

### Module 'openpyxl' not found

If you encounter a `ModuleNotFoundError: No module named 'openpyxl'` error, you can install the missing module using:
```bash
pip install openpyxl
```
or create a virtual envirnoment as described before

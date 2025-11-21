# SLIMTutorial2025

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB.svg?style=flat&logo=python)](https://www.python.org/)

[![JupyterHub](https://img.shields.io/badge/JupyterHub-Server-brightgreen?style=flat&logo=jupyter)]()

[![Reproducible](https://img.shields.io/badge/Reproducible-Environments-blue.svg)]()

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()

**Tutorials for the 2025 ML4Seismic Meeting**

This repository explains how to access, copy, and run all ML4Seismic 2025 tutorials on the shared JupyterHub server.  

Each tutorial comes with its own `requirements.txt`, ensuring **fully reproducible Python environments**.

---

## Table of Contents

- [1. Accessing JupyterHub](#1-accessing-jupyterhub)

- [2. Copying Tutorials](#2-copying-tutorials)

- [3. Python Environment Setup](#3-python-environment-setup)

- [4. Running a Tutorial](#4-running-a-tutorial)

- [5. Notes for Participants](#5-notes-for-participants)

- [6. Troubleshooting](#6-troubleshooting)

- [7. Directory Layout](#7-directory-layout)

- [8. Contact](#8-contact)

---

## 1. Accessing JupyterHub

Open your browser and visit:

```
http://128.85.36.226/
```

Use the username/password provided by the organizers.  

Your first login will prompt you to set a new password.

---

## 2. Copying Tutorials

All tutorials are stored in a **read-only shared directory**:

```
/opt/ml4seismic_tutorial_2025/
```

Make your own copy:

```bash
cp -r /opt/ml4seismic_tutorial_2025 ~/ml4seismic_tutorial_2025
```

Work **only** inside your personal copy.

---

## 3. Python Environment Setup

Each tutorial has its own Python virtual environment. Choose one of the following methods:

### 3.1 Automated Setup (Recommended)

Most tutorials include a `setup.sh` script for automatic setup:

```bash
cd ~/ml4seismic_tutorial_2025/tutorial_1
chmod +x setup.sh  # Make script executable (first time only)
./setup.sh
```

This will:
- Check Python version (requires Python 3.12+)
- Create a virtual environment (`.venv`)
- Install all dependencies from `requirements.txt`
- Set up the environment for Jupyter
- Register Jupyter kernel automatically

### 3.2 Manual Setup

If a tutorial doesn't have `setup.sh`, set up manually:

#### Option A: Using pip (Standard)

```bash
cd ~/ml4seismic_tutorial_2025/tutorial_1

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

#### Option B: Using uv (Faster, if available)

```bash
cd ~/ml4seismic_tutorial_2025/tutorial_1

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

### 3.3 Register Python Kernel for Jupyter

After setting up the environment, register it as a Jupyter kernel:

```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Install ipykernel if not already installed
pip install ipykernel

# Register the kernel
python -m ipykernel install --user --name tutorial_1 --display-name "Python (tutorial_1)"
```

Then refresh JupyterHub and select:

**Kernel → Change Kernel → Python (tutorial_1)**

---

## 4. Running a Tutorial

### 4.1 Activate the Environment

In the JupyterHub terminal:

```bash
cd ~/ml4seismic_tutorial_2025/tutorial_1
source .venv/bin/activate
```

### 4.2 Launch Jupyter Notebook

If the tutorial includes a `launch.sh` script:

```bash
chmod +x launch.sh  # Make executable (first time only)
./launch.sh
```

Or launch manually:

```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Start Jupyter
jupyter notebook tutorial_notebook.ipynb
```

Or use JupyterLab:

```bash
jupyter lab tutorial_notebook.ipynb
```

### 4.3 Select the Correct Kernel

In your Jupyter notebook, ensure you select the correct kernel:

**Kernel → Change Kernel → Python (tutorial_1)**

---

## 5. Notes for Participants

- The directory `/opt/ml4seismic_tutorial_2025/` is **read-only**.

- Save your work frequently; the JupyterHub server may restart after idle.

- Always activate the correct environment before running any notebook.

- All tutorials require **Python 3.12+**.

- Each tutorial should have its own virtual environment (`.venv` folder).

- If using GPU-enabled examples, ensure you select a GPU runtime (if available).

- For reproducibility, each tutorial includes a `requirements.txt` with pinned package versions.

---

## 6. Troubleshooting

| Issue                           | Solution |
|--------------------------------|----------|
| Python kernel missing        | Run `python -m ipykernel install --user --name tutorial_X --display-name "Python (tutorial_X)"` after activating the environment |
| Permission denied              | You attempted to edit `/opt/...` → switch to `~/ml4seismic_tutorial_2025` |
| Slow `pip install`            | Ask admins to preinstall packages, or use `uv` for faster installs |
| Module not found              | Ensure virtual environment is activated: `source .venv/bin/activate` |
| Kernel won't start             | Restart Jupyter server (Control Panel → Stop → Start), then re-register kernel |
| Import errors                  | Verify all dependencies installed: `pip install -r requirements.txt` |
| Python version mismatch        | Check Python version: `python3 --version` (should be 3.12+) |

---

## 7. Directory Layout

```
~/ml4seismic_tutorial_2025/
├── tutorial_1/
│   ├── requirements.txt
│   ├── setup.sh              # Optional: automated setup script
│   ├── launch.sh             # Optional: launch script
│   ├── .venv/                # Virtual environment (created during setup)
│   └── tutorial_notebook.ipynb
├── tutorial_2/
│   ├── requirements.txt
│   ├── setup.sh
│   ├── launch.sh
│   ├── .venv/
│   └── ...
└── tutorial_N/
```

Each folder is its own Python environment with its own virtual environment and dependencies.

---

## 8. Contact

**Prof. Felix J. Herrmann**  

felix.herrmann@gatech.edu  

**Haoyun Li**  

hli853@gatech.edu  

© 2025 SLIM Group, Georgia Tech — Infrastructure for ML4Seismic 2025


# LabVIEW-Python Project Setup Guide

This repository contains a project that integrates LabVIEW and Python, likely for data processing, automation, or control applications. This guide will help you set up the development environment and get started with the project.

## Prerequisites

Before you begin, ensure you have the following installed:

- **LabVIEW:** Ensure you have a compatible version of National Instruments LabVIEW installed. The specific version might be defined within `repo.toml` or `env_setup.ps1`.
- **Python:** A supported Python distribution (e.g., Python 3.8 or later) is required. Check `repo.toml` or `setup.py` for specific version requirements.
- **pip:** The Python package installer (usually included with Python).
- **Powershell:** A recent version of Powershell.
- **NI-VISA:** The NI-VISA drivers.

## Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Run the Environment Setup Script:**
    Execute the provided PowerShell script (`env_setup.ps1`) to configure your environment. This script may:

    - Create a Python virtual environment.
    - Install Python dependencies.
    - Configure LabVIEW project paths or settings.
    - Install system tools.

    ```powershell
    .\env_setup.ps1
    ```

    **Note**: Run Powershell as administrator.

3.  **Install Python Dependencies (if applicable):**
    If `env_setup.ps1` doesn't install dependencies, or if you need to manage them manually, use the following:

    ```bash
    # If a virtual environment was created, activate it first.
    # source .venv/bin/activate  (Linux/macOS)
    # .venv\Scripts\activate      (Windows)
    pip install -r requirements.txt  #If a requirement.txt is present
    python setup.py install #If no requirements.txt is present
    ```

    Note that requirements.txt might not be present, and setup.py is used instead.

4.  **Open the LabVIEW Project:**
    Locate the main LabVIEW project file (`*.lvproj`) and open it in LabVIEW.

5.  **Documentation:**
    If you need further information, you can find it on the docs/ directory.

6.  **Verification:**
    If needed, some verification steps could be defined on env_setup.ps1.

## Project Structure

The project typically includes the following directories:

- **LabVIEW Code:** Contains the LabVIEW virtual instruments (VIs), classes, libraries, and project files.
- **Python Code:** Python scripts and modules for tasks like data processing, communication, or automation.
- **`repo.toml`:** Project metadata, dependency details, and build instructions.
- **`setup.py`:** Python packaging information.
- **`env_setup.ps1`:** Environment setup script.
- **`docs/`:** Documentation files, like how-tos, API references, etc.
- **`ext/`:** External dependencies, or external software.

## Getting Started

After completing the setup, you can:

- Open and run the main VIs in LabVIEW.
- Run the Python scripts from the command line or your IDE.
- Interact between LabVIEW and Python code, if the project allows.

## Contributing

Please refer to the `CONTRIBUTING.md` file (if present) for contribution guidelines.

## Support

For any issues or questions, contact the project maintainers.

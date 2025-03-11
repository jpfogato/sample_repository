# App Description

LabVIEW project template for developing and compiling code for internal or external usage.

# Project Setup Guide

This repository contains a project that integrates LabVIEW and Python, likely for data processing, automation, or control applications. This guide will help you set up the development environment and get started with the project.

## Prerequisites

Before you begin, ensure you have the following installed:

- **LabVIEW:** Ensure you have a compatible version of National Instruments LabVIEW installed. The specific version might be defined within `repo.toml`.
- **Python:** A supported Python distribution (e.g., Python 3.8 or later) is required. Check `repo.toml` or `setup.py` for specific version requirements.
- **pip:** The Python package installer (usually included with Python).
- **Powershell:** A recent version of Powershell.

## Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Run the Environment Setup Script:**
    Execute the provided PowerShell script (`env_setup.ps1`) to configure your environment. This script will:

    - Install Python dependencies.

    ```powershell
    .\env_setup.ps1
    ```

3.  **Run the Python Dependencies Manager:**
    This script should parse the `repo.toml` file and:

    - download any externals in the configured mode and place them at the `.\ext` folder
    - download relevant documentation and extract them to the `.\docs` folder

    ```bash
    # If a virtual environment was created, activate it first.
    python setup.py
    ```

4.  **Open the LabVIEW Project:**
    Locate the main LabVIEW project file (`*.lvproj`) and open it in LabVIEW.

5.  **Documentation:**
    If you need further information, you can find it on the docs/ directory after the python setup step.

6.  **Verification:**
    If needed, some verification steps could be defined on env_setup.ps1.

## Project Structure

The project typically includes the following directories:

- **LabVIEW Code:** Contains the LabVIEW virtual instruments (VIs), classes, libraries, and project files.
- **Python Code:** Python scripts and modules for tasks like data processing, communication, or automation.
- **`repo.toml`:** Project metadata, dependency details, and build instructions.
- **`setup.py`:** Python repository setup.
- **`env_setup.ps1`:** Environment setup script.
- **`docs/`:** Documentation files, like how-tos, API references, etc.
- **`ext/`:** External dependencies, or external software.

## Getting Started

After completing the setup, you can:

- Open and run the main VIs in LabVIEW.
- Run the build specfication present in the `.\ext` folder

## Contributing

Please refer to the guidelines on the source management page.

## Support

For any issues or questions, contact the project maintainers.

# App Description

LabVIEW project template for developing and compiling code for internal or external usage.

# Project Setup Guide

This repository contains a project that integrates LabVIEW and Python, likely for data processing, automation, or control applications. This guide will help you set up the development environment and get started with the project.

## Prerequisites

Before you begin, ensure you have the following installed:

- **LabVIEW:** Ensure you have a compatible version of National Instruments LabVIEW installed. The specific version might be defined within `repo.json`.
- **Python:** A supported Python distribution (e.g., Python 3.8 or later) is required. Check `repo.json` or `setup.py` for specific version requirements.
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
    This script should parse the `repo.json` file and:

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
- **`repo.json`:** Project metadata, dependency details, and build instructions.
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

---

## Project Configuration (repo.json)

This project utilizes a `repo.json` file to manage its configuration, dependencies, build process, and documentation. Here's a breakdown of the key sections:

### Dependencies

The `dependencies` section specifies the external libraries and tools required by the project:

- **`vcs_interfaces`:**
  - **`version`:** `2.0.1` - The required version of the `vcs_interfaces` library.
  - **`include_source`:** `false` - Indicates that only the compiled version of this dependency is needed, not the source code.
- **`build_controller`:**
  - **`version`:** `>=4.0.0` - Specifies that a version of `build_controller` greater than or equal to 4.0.0 is required.

### Builder

The `builder` section defines how the project is built and managed:

- **`enabled`:** `true` - Indicates that the automatic build process is enabled.
- **`output_dir`:** `build` - Specifies that build artifacts will be stored in the `build` directory.
- **`project`:**
  - **`lv_version`:** `2023` - The LabVIEW version to be used for building the project (LabVIEW 2023).
  - **`project_file`:** `MyProject.lvproj` - The name of the main LabVIEW project file.
  - **`build_spec`:** `MyApplication` - The name of the build specification within the LabVIEW project.
- **`commands`:**
  - **`pre_build`:** Commands to run before the build process.
    - `echo Preparing build...` - Displays a message indicating the start of the pre-build phase.
    - `cd ext/build_controller/target` - Changes the current directory to the build controller target.
    - `g-cli build_controller -- --action pre_build --config "JSON_FILE"` - Executes the `build_controller` G-CLI application with the `pre_build` action. The `JSON_FILE` placeholder should be replaced with the actual path to the configuration file.
  - **`build`:** Commands to run during the build process.
    - `echo Building...` - Displays a message indicating the start of the build phase.
    - `cd ext/build_controller/target` - Changes the current directory to the build controller target.
    - `g-cli build_controller -- --action build --config "JSON_FILE"` - Executes the `build_controller` G-CLI application with the `build` action. The `JSON_FILE` placeholder should be replaced with the actual path to the configuration file.
  - **`post_build`:** Commands to run after the build process.
    - `echo Build completed!` - Displays a message indicating the completion of the build phase.
    - `cd ext/build_controller/target` - Changes the current directory to the build controller target.
    - `g-cli build_controller -- --action post_build --config "JSON_FILE"` - Executes the `build_controller` G-CLI application with the `post_build` action. The `JSON_FILE` placeholder should be replaced with the actual path to the configuration file.
- **`notifications`:**
  - **`email`:** `alerts@example.com` - The email address to receive build failure notifications.
  - **`webhook`:** `https://hooks.example.com/build` - The webhook URL to send notifications to.

### Documentation

The `docs` section defines how documentation is managed:

- **`download`:**
  - `https://example.com/file1.pdf`
  - `https://example.com/file2.pdf`
  - `https://example.com/file3.pdf` - A list of URLs from which documentation files (PDFs in this case) should be downloaded.
- **`destination`:** `doc` - The directory where the downloaded documentation files will be stored.

---

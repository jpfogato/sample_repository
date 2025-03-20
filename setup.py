import json
import subprocess
import os
import requests
import shutil
import zipfile
from pathlib import Path


def download_and_extract_zip(url, destination_folder):
    """Downloads a zip file from a URL and extracts it to the destination folder."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        zip_filename = os.path.join(destination_folder, "temp.zip")
        with open(zip_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)

        os.remove(zip_filename)  # Remove the temporary zip file
        print(f"Downloaded and extracted {url} to {destination_folder}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except zipfile.BadZipFile as e:
        print(f"Error: Invalid zip file downloaded from {url}: {e}")
    except Exception as e:
        print(
            f"An unexpected error occurred while downloading or extracting {url}: {e}")


def download_file(url, destination_folder, filename=None):
    """Downloads a file from a URL to the destination folder."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        if filename is None:
            filename = os.path.basename(url)
        filepath = os.path.join(destination_folder, filename)

        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded {url} to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while downloading {url}: {e}")


def setup_repository(repo_json_path):
    """
    Sets up the local repository based on the settings in the repo.json file.

    Args:
        repo_json_path (str): The path to the repo.json file.
    """

    try:
        with open(repo_json_path, 'r') as f:
            repo_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: repo.json file not found at {repo_json_path}")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {repo_json_path}")
        return

    # Handle dependencies
    if "dependencies" in repo_data:
        print("Setting up dependencies...")
        dependencies = repo_data["dependencies"]

        if isinstance(dependencies, dict):
            # Handle externals
            if "externals" in dependencies:
                externals = dependencies["externals"]
                for external in externals:
                    if "folder" in external and "url" in external:
                        folder_name = external["folder"]
                        url = external["url"]
                        destination_folder = os.path.join("ext", folder_name)

                        if not os.path.exists(destination_folder):
                            os.makedirs(destination_folder)

                        if url.endswith(".zip"):
                            download_and_extract_zip(
                                url, destination_folder)
                        else:
                            download_file(url, destination_folder)
                    else:
                        print(
                            f"Error: Invalid external dependency format: {external}")
            else:
                print("No externals found in dependencies.")
        else:
            print("Error: dependencies is not a dictionary")
            return
    else:
        print("No dependencies found in repo.json.")

    # Handle docs
    if "docs" in repo_data:
        print("Downloading documentation...")
        docs_data = repo_data["docs"]
        if "download" in docs_data and "destination" in docs_data:
            download_urls = docs_data["download"]
            destination_dir = docs_data["destination"]

            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            for url in download_urls:
                download_file(url, destination_dir)
        else:
            print("Error: download or destination not found in docs")
            return
    else:
        print("No docs found in repo.json.")

    print("Repository setup completed.")


if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = Path(__file__).parent
    # Construct the path to repo.json relative to the script
    repo_json_path = script_dir / "repo.json"
    setup_repository(repo_json_path)

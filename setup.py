import toml
import os
import requests
import shutil
import subprocess


def download_file(url, destination_path):
    """Downloads a file from a URL to a destination path."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        with open(destination_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded: {url} -> {destination_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except Exception as e:
        print(f"An error occurred during download: {e}")


def create_dependencies(dependencies, ext_path):
    """Creates folders for dependencies based on repo.toml."""
    for dep_name, dep_info in dependencies.items():
        dep_path = os.path.join(ext_path, dep_name)
        os.makedirs(dep_path, exist_ok=True)
        print(f"Created dependency folder: {dep_path}")

        # This can be improved to consider the source attribute
        # and clone the repo if it is a git repo, for example.
        if isinstance(dep_info, dict) and 'include_source' in dep_info and dep_info['include_source']:
            pass
            # logic to clone a repository.


def create_docs(docs_data, docs_path):
    """Downloads documentation files based on repo.toml."""
    os.makedirs(docs_path, exist_ok=True)
    for url in docs_data:
        file_name = os.path.basename(url)
        destination = os.path.join(docs_path, file_name)
        download_file(url, destination)


def main():
    """Main function to read repo.toml and set up the repository."""
    try:
        config = toml.load("repo.toml")
    except FileNotFoundError:
        print("Error: repo.toml not found.")
        return
    except toml.TomlDecodeError as e:
        print(f"Error parsing repo.toml: {e}")
        return

    ext_path = "ext"
    docs_path = config.get("docs", {}).get("destination", "doc")

    if "dependencies" in config:
        create_dependencies(config["dependencies"], ext_path)

    if "docs" in config and "download" in config["docs"]:
        create_docs(config["docs"]["download"], docs_path)

    print("Repository setup completed.")


if __name__ == "__main__":
    main()

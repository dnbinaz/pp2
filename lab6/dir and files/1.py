import os

def list_directories_and_files(path):
    try:
        all_items = os.listdir(path)

        directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
        files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

        print(f"Directories in {path}:")
        print("\n".join(directories))

        print(f"\nFiles in {path}:")
        print("\n".join(files))

        print(f"\nAll items (directories and files) in {path}:")
        print("\n".join(all_items))
    except FileNotFoundError:
        print(f"The path '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

specified_path = "/path/to/your/directory"
list_directories_and_files(specified_path)

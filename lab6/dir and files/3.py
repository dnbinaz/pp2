import os

def analyze_path(path):
    # Check if the path exists
    if os.path.exists(path):
        print(f"The path '{path}' exists.")

        # Extract filename and directory portions
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{path}' does not exist.")

given_path = "/Users/ihlasova75icloud.com/Desktop/pp2/lab6"
analyze_path(given_path)

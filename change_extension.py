import os
import shutil
import logging
from error_handling import handle_errors

# Configure logging
logging.basicConfig(filename='file_conversion.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_file_in_use(file_path):
    """Check if a file is currently in use."""
    try:
        os.rename(file_path, file_path)
        return False
    except OSError:
        return True

@handle_errors
def convert_file_extension(file_path, new_extension):
    """
    Convert the file to a new file with the provided extension.

    Parameters:
    file_path (str): The path to the file to be converted.
    new_extension (str): The new file extension (e.g., '.txt', '.csv').

    Returns:
    str: The new file path with the converted extension.
    """
    if is_file_in_use(file_path):
        return f"Error: The file '{file_path}' is currently in use by another process."

    # Get the directory and filename without extension
    directory, filename = os.path.split(file_path)
    name_without_ext = os.path.splitext(filename)[0]

    # Create the new file path
    new_file_path = os.path.join(directory, name_without_ext + new_extension)

    # Backup the original file
    backup_path = os.path.join(directory, filename + '.bak')
    shutil.copy2(file_path, backup_path)
    logging.info(f"Backup created at: {backup_path}")

    # Copy the file content to the new file, preserving metadata
    shutil.copy2(file_path, new_file_path)
    logging.info(f"File converted from {file_path} to {new_file_path}")

    return new_file_path
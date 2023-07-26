import os

def mass_rename(directory, prefix='', suffix='', start_number=1, step=1):
    """
    Mass rename files in a directory with a given prefix, suffix, and numbering scheme.

    Parameters:
        directory (str): The path to the directory containing the files to be renamed.
        prefix (str, optional): The common prefix to be added to the files. 
        suffix (str, optional): The common suffix to be added to the files. 
        start_number (int, optional): The starting number for the numbering scheme. 
        step (int, optional): The step size for the numbering scheme. 
    Returns:
        None
    """
    file_list = os.listdir(directory)
    file_list.sort()

    for i, filename in enumerate(file_list):
        old_path = os.path.join(directory, filename)
        new_filename = f"{prefix}{start_number + i * step}{suffix}{os.path.splitext(filename)[1]}"
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)

if __name__ == "__main__":
    
    directory_path = r"C:\Users\Elwiz\Desktop\New folder"
    
    mass_rename(directory_path, prefix="file_", suffix="_new", start_number=1, step=1)

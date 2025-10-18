import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    
    if(directory is None):
        directory = "."
    
    abs_directory = os.path.abspath(directory)
    if not abs_directory.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    os.path.join(working_directory, directory)

import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    """
    Permite obtener el contenido del archivo (file_path) apartir de una ruta base (working_directory),
    siendo 'file_path' un archivo valido dentro de 'working_directory'
    """
    try:
        absolute_full_path = __get_absolute_file_path(working_directory, file_path)
        content = __get_content_inside_file(absolute_full_path, file_path, MAX_CHARS)
        
        return content
    except Exception as e:
        return str(e)
    
def __get_absolute_file_path(working_directory: str, file_path: str) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    
    full_path = ""
    if file_path is None or file_path == ".":
        full_path = abs_working_dir
    else:
        abs_full_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
        if not abs_full_path.startswith(abs_working_dir):
            raise Exception(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(abs_full_path):
            raise Exception(f'Error: File not found or is not a regular file: "{file_path}"')
        full_path = abs_full_path
    
    return full_path

def __get_content_inside_file(absolute_full_path: str, file_path: str, max_chars: int) -> str:
    try:
        content = ""
        with open(absolute_full_path, "r") as f:
            file_content = f.read(max_chars + 1)
            if len(file_content) > max_chars:
                content = file_content[:max_chars]
                content += f'[...File "{file_path}" truncated at {max_chars} characters].'
            else:
                content = file_content
        return content
    except Exception as e:
        raise Exception(f"Error: {str(e)}")
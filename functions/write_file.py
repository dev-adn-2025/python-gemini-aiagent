import os

def write_file(working_directory, file_path, content):
    """
    Permite guardar el contenido en el archivo (file_path) apartir de una ruta base (working_directory),
    siendo 'file_path' un archivo valido dentro de 'working_directory'
    """
    try:
        absolute_full_path = __get_absolute_file_path(working_directory, file_path)
        result = __save_content_inside_file(absolute_full_path, file_path, content)
        
        return result
    except Exception as e:
        return str(e)
    
def __get_absolute_file_path(working_directory: str, file_path: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        
        full_path = ""
        if file_path is None or file_path == ".":
            full_path = abs_working_dir
        else:
            abs_full_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
            if not abs_full_path.startswith(abs_working_dir):
                raise Exception(f'Cannot write to "{file_path}" as it is outside the permitted working directory')
            
            if os.path.exists(abs_full_path) and os.path.isdir(abs_full_path):
                raise Exception(f'File path found and is not a regular file: "{file_path}"')
            
            if not os.path.exists(abs_full_path):
                parent_dir = os.path.dirname(abs_full_path)
                os.makedirs(parent_dir, exist_ok=True)

            full_path = abs_full_path
        
        return full_path
    except Exception as e:
        raise Exception(f"Error: {str(e)}")

def __save_content_inside_file(absolute_full_path: str, file_path: str, content: str) -> str:
    try:
        with open(absolute_full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        raise Exception(f"Error: {str(e)}")
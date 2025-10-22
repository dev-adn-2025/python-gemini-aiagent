import os
from google.genai import types

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
    if file_path is None or file_path == '.':
        raise Exception(f'Error: File path value is invalid')
    
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
        
        if not abs_full_path.startswith(abs_working_dir):
            raise Exception(f'Cannot write to "{file_path}" as it is outside the permitted working directory')
        
        if os.path.isdir(abs_full_path):
            raise Exception(f'File path found and is not a regular file: "{file_path}"')
        
        if not os.path.exists(abs_full_path):
            parent_dir = os.path.dirname(abs_full_path)
            os.makedirs(parent_dir, exist_ok=True)
        
        return abs_full_path
    except Exception as e:
        raise Exception(f"Error: {str(e)}")

def __save_content_inside_file(absolute_full_path: str, file_path: str, content: str) -> str:
    try:
        with open(absolute_full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        raise Exception(f"Error: {str(e)}")
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file name",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to save in the file",
            ),
        },
    ),
)
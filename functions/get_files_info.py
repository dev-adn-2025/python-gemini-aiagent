import os
from google.genai import types

def get_files_info(working_directory, directory=".") -> str:
    """
    Permite obtener el contenido (archivos y carpetas) apartir de una ruta base (working_directory),
    siendo 'directory' una ruta valida dentro de 'working_directory'
    """
    try:
        absolute_full_path = __get_absolute_directory_path(working_directory, directory)
        contents_info = __get_info_contents_inside_dir(absolute_full_path)
        
        return "\n".join(contents_info)
    except Exception as e:
        return str(e)

def __get_absolute_directory_path(working_directory: str, directory: str) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    
    full_path = ""
    if directory is None or directory == ".":
        full_path = abs_working_dir
    else:
        abs_full_path = os.path.abspath(os.path.join(abs_working_dir, directory))
        if not abs_full_path.startswith(abs_working_dir):
            raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not os.path.isdir(abs_full_path):
            raise Exception(f'Error: "{directory}" is not a directory')
        full_path = abs_full_path
    
    return full_path

def __get_info_contents_inside_dir(absolute_full_path: str) -> list[str]:
    dirs_info = []
    contents = os.listdir(absolute_full_path)
    for content in contents:
        content_path = os.path.join(absolute_full_path, content)
        is_dir = os.path.isdir(content_path)
        file_size = os.path.getsize(content_path)
        dir_info = f"- {content}: file_size={file_size} bytes, is_dir={is_dir}"
        dirs_info.append(dir_info)
    
    return dirs_info

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    """
    Permite ejecutar codigo python escrito en el archivo (file_path) apartir de una ruta base (working_directory),
    siendo 'file_path' un archivo valido dentro de 'working_directory'
    """
    try:
        __validate_file_path(working_directory, file_path)
        result = __run_python_code(working_directory, file_path, args)
        
        return result
    except Exception as e:
        return str(e)
    

def __validate_file_path(working_directory: str, file_path: str) -> str:
    if file_path is None or file_path == '.':
        raise Exception(f'Error: File path value is invalid')
    
    abs_working_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    
    if not abs_full_path.startswith(abs_working_dir):
        raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile(abs_full_path):
        raise Exception(f'Error: File "{file_path}" not found.')
    
    if not file_path.endswith(".py"):
        raise Exception(f'Error: "{file_path}" is not a Python file.')
    
    return abs_full_path

def __run_python_code(working_directory: str, file_path: str, args=[]) -> str:
    try:
        output = subprocess.run(
            ["python", file_path] + args
            , cwd=working_directory
            , timeout=30
            , capture_output=True
        )

        if output is None or (output.stdout == '' and output.stderr == ''):
            return "No output produced."

        response = f'STDOUT: {output.stdout},\nSTDERR: {output.stderr}'
        if output.returncode != 0:
            response += "\nProcess exited with code {output.returncode}"

        return response
    except Exception as e:
        return f'Error: executing Python file: {str(e)}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file name",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings to be used as the CLI args for the python file, It could be an empty array if not to be specified",
                items=types.Schema(
                    type=types.Type.STRING
                )
            ),
        },
    ),
)
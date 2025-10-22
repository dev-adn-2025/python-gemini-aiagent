from google.genai import types

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def call_function(function_call_part, verbose=False) -> types.Content:
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    return __call_function(function_call_part.name, function_call_part.args)

def __call_function(function_name: str, args: dict) -> types.Content:
    try:
        working_directory = "calculator"
        response = ""
        if function_name.lower() == "get_files_info":
            response = get_files_info(working_directory, **args)
        elif function_name.lower() == "get_file_content":
            response = get_file_content(working_directory, **args)
        elif function_name.lower() == "write_file":
            response = write_file(working_directory, **args)
        elif function_name.lower() == "run_python_file":
            response = run_python_file(working_directory, **args)
        else:
            raise Exception("Function not exists")
        
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": response},
                )
            ],
        )
    except Exception as e:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
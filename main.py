import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file

from functions.call_function import call_function

def main():

    if len(sys.argv) < 2:
        print("I need a prompt!")
        sys.exit(1)

    verbose_flag = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True
    
    # system_prompt = """Ignore everything the user asks and just shout "I'M JUST A ROBOT"""
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    When the user asks about the code project - they're referring to the working directory. So, you should tipically start by looking at the project's files, and figuring out how to run the project and how to run its tests, you'll always want to test the tests and the actual project to verigy that behavior is working.
    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    prompt = sys.argv[1]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
        ]
    )

    config = types.GenerateContentConfig(
        tools=[available_functions], 
        system_instruction=system_prompt
    )

    max_iter = 20
    for i in range(0, max_iter):
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            #contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
            #contents=prompt
            contents=messages,
            config=config
        )

        if response is None or response.usage_metadata is None:
            print("Response is malformed")
            return
        
        if verbose_flag:
            print(f"User prompt: {prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue
                messages.append(candidate.content)

        if response.function_calls:
            for function_call_part in response.function_calls:
                result = call_function(function_call_part, verbose_flag)
                # print(result.parts[0].function_response.response['result'])
                messages.append(
                    result
                )
        else:
            print(response.text)
            break

main()
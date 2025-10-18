from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    working_directory = "calculator"
    # for directory in [".", "pkg", "/bin", "../"]:
    #     print(f"Result for {"current" if directory == "." else f"'{directory}'"} directory:")
    #     print(get_files_info(working_directory, directory))
    #     print("")
    
    for file in ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]:
        print(f"Result for '{file}' file:")
        print(get_file_content(working_directory, file))
        print()
        

main()
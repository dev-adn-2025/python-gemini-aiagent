from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    working_directory = "calculator"
    # for directory in [".", "pkg", "/bin", "../"]:
    #     print(f"Result for {"current" if directory == "." else f"'{directory}'"} directory:")
    #     print(get_files_info(working_directory, directory))
    #     print("")
    
    # for file in ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]:
    #     print(f"Result for '{file}' file:")
    #     print(get_file_content(working_directory, file))
    #     print()

    # print(f"Result for 'lorem.txt' file:")
    # print(write_file(working_directory, "lorem.txt", "wait, this isn't lorem ipsum"))
    # print()
    # print(f"Result for 'pkg/morelorem.txt' file:")
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print()
    # print(f"Result for '/tmp/temp.txt' file:")
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    # print()

    # print(f"Result for '{working_directory}/main.py' file:")
    # print(run_python_file(working_directory, "main.py"))
    # print()
    # print(f"Result for '{working_directory}/main.py' file with '3 + 5' args:")
    # print(run_python_file(working_directory, "main.py", ["3 + 5"]))
    # print()
    # print(f"Result for '{working_directory}/tests.py' file:")
    # print(run_python_file(working_directory, "tests.py"))
    # print()
    # print(f"Result for '{working_directory}/../main.py' file:")
    # print(run_python_file(working_directory, "../main.py"))
    # print()
    # print(f"Result for '{working_directory}/nonexistent.py' file:")
    # print(run_python_file(working_directory, "nonexistent.py"))
    # print()
    # print(f"Result for '{working_directory}/lorem.txt' file:")
    # print(run_python_file(working_directory, "lorem.txt"))
    # print()

main()
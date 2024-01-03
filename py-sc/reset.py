import shutil
import sys

def copy_file(file_choice):
    base_path = '/Users/alimdar/Desktop/Coding/c++/'

    if file_choice == "1":
        source_path = base_path + 'macros/template-macro.cpp'
        destination_path = base_path + 'cpp/macro.cpp'
    elif file_choice == "2":
        source_path = base_path + 'macros/template-main.cpp'
        destination_path = base_path + 'cpp/main.cpp'
    elif file_choice == "3":
        source_path = base_path + 'macros/template-function.cpp'
        destination_path = base_path + 'cpp/function.cpp'
    else:
        print("Invalid choice")
        return

    try:
        shutil.copyfile(source_path, destination_path)
        print(f"{destination_path} copied successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python reset.py [1|2|3]")
        sys.exit(1)

    file_choice = sys.argv[1]
    copy_file(file_choice)

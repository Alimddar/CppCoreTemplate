import subprocess
import sys

def run_commands(run_choice):
    cpp_path = '/Users/alimdar/Desktop/Coding/c++/cpp/'
    txt_path = '/Users/alimdar/Desktop/Coding/c++/txt/'

    if run_choice == "1":
        compile_command = f"g++ -std=c++17 -o {cpp_path}program1 {cpp_path}main.cpp"
        run_command = f"{cpp_path}./program1 > {txt_path}out1.txt"
    elif run_choice == "2":
        compile_command = f"g++ -std=c++17 -o {cpp_path}program2 {cpp_path}macro.cpp"
        run_command = f"{cpp_path}./program2 > {txt_path}out2.txt"
    elif run_choice == "3":
        compile_command = f"g++ -std=c++17 -o {cpp_path}program3 {cpp_path}function.cpp"
        run_command = f"{cpp_path}./program3 > {txt_path}out3.txt"
    else:
        print("Invalid choice")
        return

    process = subprocess.Popen(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print("\033[94mCompilation failed:\033[0m")
        print(stderr.decode())
        return

    process = subprocess.Popen(run_command, shell=True)
    process.wait()

    if process.returncode != 0:
        print("\033[94mExecution failed:\033[0m")
        return

    output_file = f"{txt_path}out1.txt" if run_choice == "1" else f"{txt_path}out2.txt" if run_choice == "2" else f"{txt_path}out3.txt"
    with open(output_file, "r") as file:
        output = file.read()
        print("\033[94mOutput of the program:\033[0m")
        print(output)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py [1|2|3]")
        sys.exit(1)

    run_choice = sys.argv[1]
    run_commands(run_choice)

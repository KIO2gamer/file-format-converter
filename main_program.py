import sys
from change_extension import convert_file_extension

def main():
    if len(sys.argv) != 3:
        print("Usage: python main_program.py <file_path> <new_extension>")
        return

    file_path = sys.argv[1]
    new_extension = sys.argv[2]

    result = convert_file_extension(file_path, new_extension)
    print(result)

if __name__ == "__main__":
    main()
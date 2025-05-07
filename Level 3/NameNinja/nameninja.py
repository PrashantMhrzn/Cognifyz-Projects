import os
import argparse

class Renamer:
    def rename(self, path, naming_convention='file'):
        path = os.path.abspath(path)  # Ensures proper formatting of path

        if not os.path.isdir(path):
            raise FileNotFoundError(f"Path '{path}' is not a valid directory.")

        files = os.listdir(path)
        for count, filename in enumerate(files, 1):
            file_path = os.path.join(path, filename)

            # Skip directories
            if os.path.isdir(file_path):
                continue

            if '.' in filename:
                name, extension = filename.rsplit('.', 1)
                new_name = f"{naming_convention}{count}.{extension}"
            else:
                new_name = f"{naming_convention}{count}"

            new_path = os.path.join(path, new_name)
            os.rename(file_path, new_path)

        print("✅ File Renaming Completed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Renames every file inside the given folder.')
    parser.add_argument('path', help='Absolute path of the folder')
    parser.add_argument('-n', '--naming_convention', metavar='', help='Defaults to "file"', default='file')

    args = parser.parse_args()

    renamer = Renamer()

    try:
        renamer.rename(args.path, args.naming_convention)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)

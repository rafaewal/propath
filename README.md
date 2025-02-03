# ProPath

ProPath is a Python program designed to help you keep your Windows desktop tidy by arranging desktop icons according to user-defined rules. It organizes desktop files into folders based on their file extensions.

## Features

- Define rules to move files with specific extensions into designated folders.
- Automatically organize files on your desktop based on the rules you set.
- Moves folders to a designated "Folders" directory, keeping the desktop clutter-free.

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Make sure the `pywin32` package is installed. You can install it using pip:

   ```bash
   pip install pywin32
   ```

3. Clone this repository or download the `ProPath.py` file.

## Usage

1. Open `ProPath.py` in a text editor.
2. Modify the rules in the `__main__` section to suit your needs. For example:

   ```python
   propath.add_rule('.txt', 'Text Files')
   propath.add_rule('.jpg', 'Images')
   ```

3. Save your changes.
4. Run the script by navigating to its directory in a terminal or command prompt and executing:

   ```bash
   python ProPath.py
   ```

## Customization

- **Adding Rules**: Use the `add_rule(extension, folder_name)` method to specify how files should be organized. The `extension` is the file type (e.g., `.txt`, `.jpg`), and `folder_name` is where you want these files to be moved.
- **Default Folders**: The script moves unclassified folders into a folder named "Folders" on the desktop. You can change this behavior by modifying the `move_folder` method.

## Limitations

- The script is designed for use on Windows and may not function correctly on other operating systems.
- Be cautious when moving files, as this script will alter the location of your files based on the rules you set.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to propose changes or report bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
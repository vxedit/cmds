import os

def save_folder_structure_to_txt(folder_path, output_file, indent=0):
    """
    Save the folder structure inside the specified folder to a text file.

    Args:
    - folder_path (str): The path to the folder.
    - output_file (str): The path to the output text file.
    - indent (int): The level of indentation for saving.
    """
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    with open(output_file, 'w') as file:
        _save_folder_structure_to_txt_recursive(folder_path, file, indent)


def _save_folder_structure_to_txt_recursive(folder_path, file, indent):
    """
    Recursively save the folder structure to the text file.

    Args:
    - folder_path (str): The path to the folder.
    - file (File object): The file object for writing.
    - indent (int): The level of indentation for saving.
    """
    for item in sorted(os.listdir(folder_path)):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            file.write(" | " * indent + "|-- " + item + '\n')
            _save_folder_structure_to_txt_recursive(item_path, file, indent + 1)
        else:
            file.write(" | " * indent + "|-- " + item + '\n')


# Example usage:
folder_path = os.getcwd()
output_file = "folder_structure.txt"
save_folder_structure_to_txt(folder_path, output_file)
print(f"Folder structure saved to {output_file}")

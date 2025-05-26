def is_git_folder(folder_path):
    """
    Check if a folder is a Git repository by looking for the '.git' folder.

    Parameters:
        folder_path (str): Path to the folder to check.

    Returns:
        bool: True if the folder is a Git repository, False otherwise.
    """
    git_path = os.path.join(folder_path, '.git')
    return os.path.isdir(git_path)

def func_organize_folders(_source_dir, _folders_list):
    print("In func_organize_folders")
    print(_folders_list)
    for folder_path in _folders_list:
        print(folder_path)
        if not os.path.exists(folder_path):
            print(f"Error: The folder '{folder_path}' does not exist.")
            continue
        if is_git_folder(folder_path):
            print(f"The folder '{folder_path}' is a Git repository.")
        else:
            print(f"The folder '{folder_path}' is NOT a Git repository.")

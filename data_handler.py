import os

def __start_data_structure(path):
    """
    Creates and initiates file names from all folders and subfolders of path
    
    Keyword arguments
    path -- the folder path containing the files
    """
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for dirname in dirnames:
            for (dirpath, dirnames, filenames) in os.walk(path + dirname):
                files.extend([{'Name':str(file).replace('.txt', ''), 'File Name':file} for file in filenames])
    print(files)
    pass

def __get_all_files_in_dir(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        for dirname in dirnames:
            for (dirpath, dirnames, filenames) in os.walk(folder_path + dirname):
                files.extend([dirpath + '/' + files for files in filenames])

    return files

def __append_folder_info(folder_desc, folder_path):
    pass

def __read_mirflicker_exif_raw(exif_folder_path, file_path_list):
    data = {}

    # for path in file_path_list:
    pass


if __name__ == "__main__":
    __start_data_structure('../datasets/MIRFLICKR-1M/tags_raw/')


def __get_all_files_in_dir(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        for dirname in dirnames:
            for (dirpath, dirnames, filenames) in os.walk(folder_path + dirname):
                files.extend([dirpath + '/' + files for files in filenames])

    return files

def __append_folder_info(folder_desc, folder_path):
    

def __read_mirflicker_exif_raw(exif_folder_path, file_path_list):
    data = {}

    for path in file_path_list:
        
    pass


if __name__ == "__main__":
    pass
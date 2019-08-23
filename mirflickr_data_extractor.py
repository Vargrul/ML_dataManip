import os
import shutil
import argparse

def exif_explorer(folder_path):
    pass

def tag_filter(folder_path, tags_include, tags_exclude):
    # Get list of files
    f = []
    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        f.extend(filenames)
        break
    # Validate included tags
    if len(tags_include) != 0:
        f = __tag_evaluator_any(folder_path, f, tags_include)
    print(len(f))

    # validate excluded tags
    if len(tags_exclude) != 0:
        f = __tag_evaluator_any(folder_path, f, tags_exclude, exclude=True)
    print(len(f))

    # return list of images with given tags
    return f

def __tag_evaluator_any(path, files, tags, exclude=False):
    filtered_files = []
    for f in files:
        with open(path+f) as file:
            contains_tag =  False
            for line in file:
                line = line.strip().lower()
                for t in tags:
                    if line == t:
                        contains_tag = True
                        break
                
                if contains_tag:
                    break

            if contains_tag and not exclude:
                filtered_files.append(f)
            elif not contains_tag and exclude:
                filtered_files.append(f)

    return filtered_files

def __clean_dir(dir):
    if os.path.isdir(dir):
        for the_file in os.listdir(dir):
            file_path = os.path.join(dir, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
        # shutil.rmtree(dir)
    else:
        os.mkdir(dir)

    return

if __name__ == "__main__":
    # Setup Argpasser
    parser = argparse.ArgumentParser(description='Filter data for the MIRFLICKR dataset.')
    parser.add_argument('tagsdir', help='directory of the tags_raw dir.')
    parser.add_argument('inimgdir', help='input directory of images corresponding to the tags.')
    parser.add_argument('outimgdir', help='output directory for filtered images.')

    args = parser.parse_args()

    print(args.tagsdir)

    pass

    # setup variables
    tag_folder_path = 'mirflickr-25k/meta/tags_raw/'
    # tags_inc = ['explore', 'nature', 'geotagged', 'landscape', 'street', 'explored', 'city', ]
    tags_inc = []
    tags_exc = ['sky', 'clouds', 'swirl', 'bw', 'macro', 'blackandwhite', 'abstract', 'reflection']

    exif_folder_path = 'mirflickr-25k/meta/exif_raw/'
    img_folder_path = 'mirflickr-25k/img/'
    output_path = 'test_output/'

    # clean output folder
    __clean_dir(output_path)

    # Filter files
    files = tag_filter(tag_folder_path, tags_inc, tags_exc)

    print('Number of images found: ' + str(len(files)))

    # Copy files
    # for f in files:
    #     # f.replace('tags', 'im')
    #     shutil.copy2(img_folder_path + f.replace('tags', 'im').replace('txt', 'jpg'), output_path)
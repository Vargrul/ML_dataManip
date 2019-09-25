import os
import shutil
import argparse
import collections

def load_data(folder_path):
    pass


def exif_explorer(folder_path):
    pass

def tag_filter(folder_path, tags_include, tags_exclude):
    # Get list of files
    f = []
    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        for dirname in dirnames:
            for (dirpath, dirnames, filenames) in os.walk(folder_path + dirname):
                f.extend([dirpath + '/' + f for f in filenames])
    print(len(f))

    # Validate included tags
    if len(tags_include) != 0:
        f = __tag_evaluator_any(f, tags_include)
    print(len(f))

    # validate excluded tags
    if len(tags_exclude) != 0:
        f = __tag_evaluator_any(f, tags_exclude, exclude=True)
    print(len(f))

    # return list of images with given tags
    return f

def __tag_evaluator_any(files, tags, exclude=False):
    filtered_files = []
    for f in files:
        with open(f) as file:
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

def explorer_tags(folder_path):
    # Get list of files
    files = []
    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        for dirname in dirnames:
            for (dirpath, dirnames, filenames) in os.walk(folder_path + dirname):
                files.extend([dirpath + '/' + files for files in filenames])
    print(len(files))

    # Create lists for
    counter = {}

    # read the tags and count
    for f in files:
        with open(f) as file:
            for line in file:
                line = line.strip().lower()
                if line in counter:
                    counter[line] += 1
                else:
                    counter[line] = 1

    # sort by value
    sorted_x = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)
    counter = collections.OrderedDict(sorted_x)

    # Print tags and counts
    count = 0
    for (t, c) in counter.items():
        print(t + '\t' + str(c))
        count +=1
        if count >= 100:
            break

def explorer_exif(folder_path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        for dirname in dirnames:
            for (dirpath, dirnames, filenames) in os.walk(folder_path + dirname):
                files.extend([dirpath + '/' + files for files in filenames])
    print(len(files))

    # Create lists for
    counter = {}

    # read the tags and count
    for f in files:
        with open(f) as file:
            for line in file:
                line = line.strip().lower()
                if line in counter:
                    counter[line] += 1
                else:
                    counter[line] = 1

    # sort by value
    sorted_x = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)
    counter = collections.OrderedDict(sorted_x)

    # Print tags and counts
    count = 0
    for (t, c) in counter.items():
        print(t + '\t' + str(c))
        count +=1
        if count >= 100:
            break

if __name__ == "__main__":
    # Setup Argpasser
    parser = argparse.ArgumentParser(description='Filter data for the MIRFLICKR dataset.')
    parser.add_argument('-i', '--in', help='input directory of images corresponding to the tags.', required=True)
    parser.add_argument('-o', '--out', help='output directory for filtered images.', required=True)
    parser.add_argument('-t', '--tagdir', help='path to the tags_raw dir.', required=True)
    parser.add_argument('-e', '--exifdir', help='path to the exif_raw dir.')
    parser.add_argument('--explortags', action='store_true', help='exploeres the tags returning all unique tags and the count of each.')


    args = parser.parse_args()

    tag_folder_path = args.tagdir
    img_folder_path = getattr(args,'in')
    output_path = args.out

    if args.explortags:
        explorer_tags(tag_folder_path)
    else:
        # setup variables
        # tag_folder_path = 'mirflickr-25k/meta/tags_raw/'
        # # tags_inc = ['explore', 'nature', 'geotagged', 'landscape', 'street', 'explored', 'city', ]
        tags_inc = ['indoor', 'outdoor']
        # tags_exc = ['sky', 'clouds', 'swirl', 'bw', 'macro', 'blackandwhite', 'abstract', 'reflection']

        # exif_folder_path = 'mirflickr-25k/meta/exif_raw/'
        # img_folder_path = 'mirflickr-25k/img/'
        # output_path = 'test_output/'

        # clean output folder
        __clean_dir(output_path)

        # Filter files
        files = tag_filter(tag_folder_path, tags_inc, tags_exc)

        print('Number of images found: ' + str(len(files)))

        # Copy files
        # for f in files:
        #     # f.replace('tags', 'im')
        #     shutil.copy2(img_folder_path + f.replace('tags', 'im').replace('txt', 'jpg'), output_path)
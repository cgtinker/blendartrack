import os
from os import listdir
from os.path import isfile, join


def is_directory_path(dir_path):
    if os.path.isdir(dir_path):
        return True
    else:
        return False


def is_file_path(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False


def is_abs_path(abs_path):
    if os.path.isabs(abs_path):
        return True
    else:
        return False


def rel_to_abs_path(rel_path):
    abs_path = os.path.abspath(rel_path)
    return abs_path


def get_files_in_dir(dir_path):
    files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    return files


def get_dirs_in_dir(dir_path):
    dirs = [d for d in listdir(dir_path) if not isfile(join(dir_path, d))]
    return dirs


def process_path(path):
    if not is_abs_path(path):
        path = rel_to_abs_path(path)

    if is_directory_path(path):
        file_list = get_files_in_dir(path)
        if len(file_list) > 0:
            files = []
            for file in file_list:
                file = join(path, file)
                if is_abs_path(file):
                    files.append(file)
                else:
                    file = rel_to_abs_path(file)
                    files.append(file)
            return files, True
        else:
            return "", False

    elif is_file_path(path):
        files = []
        if is_abs_path(path):
            files.append(path)
        else:
            file = rel_to_abs_path(path)
            files.append(file)
        return files, True

    else:
        return "", False

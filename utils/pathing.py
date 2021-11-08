import os
import zipfile
from os import listdir
from os.path import isfile, join


# path type
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


def is_movie_path(file_path):
    if file_path.endswith(".mov"):
        return True
    else:
        return False


def is_json_path(file_path):
    if file_path.endswith(".json"):
        return True
    else:
        return False


# zip
def is_zip_file(file_path):
    if file_path.endswith(".zip"):
        return True
    else:
        return False


def unpack_zip(file_path):
    new_dir = os.path.splitext(file_path)[0]
    # return dir if it already exists (importing data multiple times)
    if os.path.exists(new_dir):
        return new_dir

    else:
        # unzip data
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            os.mkdir(new_dir)
            zip_ref.extractall(new_dir)
        return new_dir


# path type / conversion
def is_abs_path(abs_path):
    if os.path.isabs(abs_path):
        return True
    else:
        return False


def rel_to_abs_path(rel_path):
    abs_path = os.path.abspath(rel_path)
    return abs_path


# get files / directories
def get_files_in_dir(dir_path):
    files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    return files


def get_dirs_in_dir(dir_path):
    dirs = [d for d in listdir(dir_path) if not isfile(join(dir_path, d))]
    return dirs


# file management methods
def return_files_from_dir(dir_path):
    print("receiving files from directory")
    file_list = get_files_in_dir(dir_path)
    if len(file_list) > 0:
        files = []
        for file in file_list:
            file = join(dir_path, file)
            if is_abs_path(file):
                files.append(file)
            else:
                file = rel_to_abs_path(file)
                files.append(file)
        return files, True
    else:
        return "", False


def return_files_from_zip(path):
    print("receiving data from zip")
    if is_abs_path(path):
        dir_path = unpack_zip(path)
    else:
        m_path = rel_to_abs_path(path)
        dir_path = unpack_zip(m_path)

    files, valid = return_files_from_dir(dir_path)
    return files, valid


def return_file_from_json(path):
    print("receiving data from file path")
    files = []
    if is_abs_path(path):
        files.append(path)
    else:
        m_path = rel_to_abs_path(path)
        files.append(m_path)
    return files, True


def process_path(path):
    if not is_abs_path(path):
        path = rel_to_abs_path(path)

    if is_directory_path(path):
        files, valid = return_files_from_dir(path)
        return files, valid

    elif is_file_path(path):
        if is_zip_file(path):
            files, valid = return_files_from_zip(path)
            return files, valid

        else:
            files, valid = return_file_from_json(path)
            return files, valid

    else:
        return "", False

# Optimization done according to following points:-
# 1. Separates out the constants from code. They are now written on the top after import statement
# 2. Provided doc strings for making code more intutive.
# 3. Modularize the code so that it becomes generic and more reusable. Before optimization each file required a different function. After optimization same code can be used for a number of files.
# 4. The use of Pattern creation & re was redundant because only key was required to be updated. Before optimization regex is matched for every line, now it would only for specific key.
# 5. Use of context manager (with) has eliminated the close operation.


import os
import re

SOURCE_PATH = os.environ['SourcePath']
BASE_PATH = (SOURCE_PATH, 'develop', 'global', 'src')
BUILD_NUM = os.environ['BuildNum']
DEFAULT_MODE = 0o666



def CreatePath(*args):
    """
    Creates path from the arguments given.

    Returns:
        The complete created path.
    """
    return os.path.join(*args)


def UpdatePermission(file_path, mode=DEFAULT_MODE):
    """
    Updates file permission to given mode.
    If no mode is given then the DEFAULT_MODE will be used.

    Args:
        file_path: The file whose permission is to be updated.
        mode: Permission mode.
    """
    os.chmod(file_path, mode)


def RenameFile(original_file, new_file):
    """
    Renames new file to original file name.

    Args:
        original_file: The original file path.
        new_file: The new created file path.
    """
    os.remove(original_file)
    os.rename(new_file, original_file)


def UpdateVersion(original_file, new_file, pattern_string):
    """
    Updates version in original file by making copy of it.

    Args:
        original_file: The original file path.
        new_file: The new created file path.
        pattern_string: The key which is to be replaced with build
            number.
    """
    # Updating original file permissions.
    UpdatePermission(original_file)

    # Making copy of original file according to pattern string.
    with open(original_file, 'r') as org, open(new_file, 'w') as new:
        for line in org:
            if line.startswith(pattern_string):
                new.write('%s=%d' % (pattern_string, BUILD_NUM))
            else:
                new.write(line)

    # Renaming new file to original file.
    RenameFile(original_file, new_file)


UpdateVersion(CreatePath(BASE_PATH, 'SConstruct'), CreatePath(BASE_PATH, 'SConstruct1'), 'point')
UpdateVersion(CreatePath(BASE_PATH, 'VERSION'), CreatePath(BASE_PATH, 'VERSION1'), 'ADLMSDK_VERSION_POINT')

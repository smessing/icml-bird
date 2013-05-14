"""
files.py - Common file handling routines.
"""
import os

def ensure_file_exists_and_open(filename):
  """
    Returns a file descriptor with write/append permissions for the passed-in
    filename. Handles creating the file if need be.

    filename - The absolute path of the file to be opened.
  """
  if not os.path.exists(filename):
    return open(filename, 'w')
  else:
    return open(filename, 'a')


def ensure_dir_exists(directory):
  """
    Ensures the existence of the passed in directory (and its parents). If they
    don't exist, makes them.

    directory - The absolute path of the directory to be checked.
  """
  if not os.path.exists(directory):
    os.makedirs(directory)

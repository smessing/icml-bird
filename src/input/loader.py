"""
  loader.py - all code related to loading in training / testing data.
"""
import os
import scipy.io as io


TRAIN_NAME_PARTIAL = 'cepst_train_'
ICML_BIRD_DATA_PATH = 'ICML_BIRD_DATA_PATH'
PATH_VARS = [ ICML_BIRD_DATA_PATH ]

def load_training_mfccs(species_list):
  """
    Load a series of MFCCS data for a given species list.

    species_list: an array of species names, e.g. 'anthus_trivialis'.

    Returns a map of species_name -> numpy.ndarray where the ndarray is a D x N
    array, where D = 7734, the MFCC features and N is the number of samples.
  """
  mfcc_map = {}

  _is_valid_environ()

  # scipy.io.loadmat has the annoying property of changing the directory during
  # execution, so we cache the old directory and make sure we return to where
  # we started.
  original_dir = os.getcwd()

  for animal in species_list:
    animal_path = _build_training_mfcc_path(animal)
    mfccs = io.loadmat(animal_path)
    mfcc_map[animal] = mfccs['cepstra']
    pass

  os.chdir(original_dir)

  return mfcc_map


def _build_training_mfcc_path(animal):
  train_path = "%s/train/mfcc" % os.environ[ICML_BIRD_DATA_PATH]
  return "%s/%s%s.mat" % (train_path, TRAIN_NAME_PARTIAL, animal)


def _is_valid_environ():
  """
    Check the required environment variables for this module.

    If any required path variables are not found, an exception is raised. The
    exception includes a message parameter, as well as the specific path
    variable that was missing.
  """
  for path_var in PATH_VARS:
    if not os.environ.has_key(path_var):
      print '%s must be defined. See README.md for more information.' % path_var
      raise Exception('Path variable not found.', path_var)



"""
  loader.py - all code related to loading in training / testing data.
"""
import numpy as np
import os
import scipy.io as io

# env.validator checks:
ICML_BIRD_DATA_PATH = 'ICML_BIRD_DATA_PATH'
PATH_VARS = [ ICML_BIRD_DATA_PATH ]


TRAIN_NAME_PREFIX = 'cepst_train_'


def load_training_mfccs(species_list):
  """
    Load a series of MFCCS data for a given species list.

    species_list: an array of species names, e.g. 'anthus_trivialis'.

    Returns a map of species_name -> numpy.ndarray where the ndarray is a D x N
    array, where D = 16, the MFCC features and N is the number of samples (on
    the order of ~7,000 for at least some species).
  """
  mfcc_map = {}

  # scipy.io.loadmat has the annoying property of changing the directory during
  # execution, so we cache the old directory and make sure we return to where
  # we started.
  original_dir = os.getcwd()

  for animal in species_list:
    animal_path = _build_training_mfcc_path(animal)
    mfccs = io.loadmat(animal_path)
    # Matlab files are stored as N x D matrices. Transpose to D x N.
    mfcc_map[animal] = np.transpose(mfccs['cepstra'])
    pass

  os.chdir(original_dir)

  return mfcc_map


def _build_training_mfcc_path(animal):
  """
    Build the absolute path to the MFCC training file for a given species.

    animal - a string representing a species, e.g. 'anthus_trivialis'.

    Returns a string representing the absolute path (as determined in part
    by the environment variable ICML_BIRD_DATA_PATH) to the training matlab
    file.
  """
  train_path = "%s/train/mfcc" % os.environ[ICML_BIRD_DATA_PATH]
  return "%s/%s%s.mat" % (train_path, TRAIN_NAME_PREFIX, animal)


TEST_NAME_PREFIX = 'cepst_'


def load_testing_mfccs(times, locations):
  """
    Load a series of MFCCS data for give time and location lists.

    times: a list of timestamps, e.g., '20090324_063100'.

    locations: a list of locations, e.g., 'A'.

    Returns a map of time_and_location_string -> numpy.ndarray where the
    ndarray is a D x N array, where D = 16, the MFCC features and N is the
    number of samples.
  """
  mfcc_map = {}

  # scipy.io.loadmat has the annoying property of changing the directory during
  # execution, so we cache the old directory and make sure we return to where
  # we started.
  original_dir = os.getcwd()

  for time in times:
    time_paths = _build_testing_mfcc_paths(time, locations)
    for time_path in time_paths:
      mfccs = io.loadmat(time_path)
      time_and_location = time_path.split('/')[-1].rstrip('.mat')
      # Matlab files are stored as N x D matrices. Transpose to D x N.
      mfcc_map[time_and_location] = np.transpose(mfccs['cepstra'])

  os.chdir(original_dir)

  return mfcc_map


def _build_testing_mfcc_paths(timestamp, locations):
  """
    Build the absolute paths to the MFCC testing files for a give time stamp
    and list of locations.

    timestamp - a timestamp, e.g., '20090324_063100'

    locations - a list of valid locations, e.g. ['A', 'B']
  """
  paths = []

  for location in locations:
    test_path = "%s/test/mfcc" % os.environ[ICML_BIRD_DATA_PATH]
    path = "%s/%s%s_%s.mat" % \
        (test_path, TEST_NAME_PREFIX, location, timestamp)
    paths.append(path)

  return paths

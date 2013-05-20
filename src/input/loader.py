"""
  loader.py - all code related to loading in training / testing data.
"""
from input import names
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

    Returns a map of species_name -> dictionary where the dictionary has two
    keys, 'samples' and 'labels':

        'samples' points to a numpy.ndarray where the ndarray is a N x D array,
        where D = 16, the MFCC features for one sample and N is the number of
        samples.

        'labels' points to a list of integers of length N (number of samples),
        indicating when in the sample a bird is singing vs. when in the sample
        the signal is just noise.
  """
  mfcc_map = {}

  # scipy.io.loadmat has the annoying property of changing the directory during
  # execution, so we cache the old directory and make sure we return to where
  # we started.
  original_dir = os.getcwd()

  for animal in species_list:
    animal_path = _build_training_mfcc_path(animal)
    mfccs = io.loadmat(animal_path)
    mfcc_map[animal] = {}
    # Matlab files are stored as N x D matrices. Transpose to D x N.
    mfcc_map[animal]['samples'] = np.transpose(mfccs['cepstra'])
    num_samples = len(mfcc_map[animal]['samples'])
    mfcc_map[animal]['labels'] = _generate_label_list(animal, num_samples)
    pass

  os.chdir(original_dir)

  return mfcc_map

def load_training_mfccs_without_silent_frames(species_list):
  """
    Load a series of MFCCS data for a given species list, with all the blank
    frames removed.

    species_list: an array of species names, e.g. ['anthus_trivialis']

    Returns a map of species_name -> numpy.ndarray, where the ndarray is a 
    N x D array, where D = 16 and N is the number of samples. 

    Use this instead of load_training_mfccs() if you do not want an frames
    that don't contain the given bird actually singing
  """
  mfcc_no_empty_frames_map = {}
  all_mfcc_map = load_training_mfccs(species_list)
  for species_data in all_mfcc_map.items():
    species = species_data[0]

    # remove labels of NO_SPECIES
    labels = species_data[1]['labels']
    good_labels = [l for l in labels if l != names.NO_SPECIES_KEY]

    # remove samples with label NO_SPECIES
    samples = species_data[1]['samples']
    labels_np = np.array(species_data[1]['labels'])
    good_samples = samples[labels_np != names.NO_SPECIES_KEY]

    mfcc_no_empty_frames_map[species] = {}
    mfcc_no_empty_frames_map[species]['samples'] = good_samples
    mfcc_no_empty_frames_map[species]['labels'] = good_labels
  
  return mfcc_no_empty_frames_map

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


TIMESTAMP_PREFIX = 'train_'


def _build_time_ranges_path(animal):
  """
    Build the absolute path to the label time ranges file for a given species.

    animal - a string representing a species, e.g. 'anthus_trivialis'.

    Returns a string representing the absolute path (as determined in part
    by the environment variable ICML_BIRD_DATA_PATH) to the training matlab
    file.
  """
  label_path = "%s/train/timestamps" % os.environ[ICML_BIRD_DATA_PATH]
  return "%s/%s%s.times" % (label_path, TIMESTAMP_PREFIX, animal)


TRAINING_FILE_LENGTH_IN_SEC = 30


def _generate_label_list(animal, num_samples):
  """
    Generate a list of labels for a given species training file, given its
    time ranges file.

    animal - A string representing the species we're working on.
    num_samples - A string indicating the number of samples in the dataset,
        used to determine how the sample indecies line up to the time ranges.

    Returns a list of labels (ints), all of which exist in names.SPECIES. For
    a given list, only two labels are possible:
    names.get_index_for_species(animal) and names.NO_SPECIES_KEY.
  """
  time_ranges_path = _build_time_ranges_path(animal)
  time_ranges_file = open(time_ranges_path, 'r')
  # Make sure to skip the header.
  time_ranges = time_ranges_file.readlines()[1:]
  time_ranges_file.close()
  # Each line is "start,end\n", transform it into a tuple ('start', 'end')
  time_ranges = map(lambda x: \
      (x.split(',')[0], x.split(',')[1].strip()), time_ranges)
  # Convert each string to a float
  time_ranges = map(lambda x: (float(x[0]), float(x[1])), time_ranges)

  sec_per_sample = TRAINING_FILE_LENGTH_IN_SEC / float(num_samples)

  time_ranges_index = 0
  animal_label = names.get_index_for_species(animal)
  no_label = names.NO_SPECIES_KEY
  labels = []

  # We make a single pass through the timestamps and time ranges to produce a
  # list of labels. First, for each time index, we compute the corresponding
  # timestmap. Then, we check if it resides in the current time range. If it
  # does, we append the animal_label to the labels list for this timestamp.  If
  # it doesn't, we append the no_label to the labels list for this timestamp.
  # Also if it doesn't, we possibly increment current_range, to the first first
  # current_range greater than the current timestamp. Note, this algorithm
  # assumes that time_ranges is in sorted (increasing) order.
  for t in range(0, num_samples):
    current_range = time_ranges[time_ranges_index]
    timestamp = t * sec_per_sample
    in_current_range = _timestamp_in_range(timestamp, current_range)

    if in_current_range:
      labels.append(animal_label)
    else:
      labels.append(no_label)
      # If need be, go to the first current_range that has an end time greater
      # than the current timestamp.
      while(current_range[1] < timestamp and 
          time_ranges_index < len(time_ranges) - 1):
        time_ranges_index += 1
        current_range = time_ranges[time_ranges_index]
        
  return labels


def _timestamp_in_range(timestamp, time_range):
  """
    Test whether the given timestamp is in the given time range (i.e. is
    in between time_range[start] and time_range[end].
  """
  return timestamp >= time_range[0] and timestamp <= time_range[1]


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

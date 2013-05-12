"""
  loader.py - all code related to loading in training / testing data.
"""
import scipy.io


TRAIN_NAME_PARTIAL = 'cepst_train_'
TRAIN_PATH = '/Users/smrz/Dropbox/2013/code/icml_bird/data/train/mfcc'

def load_training_mfccs(species_list):
  """
    Load a series of MFCCS data for a given species list.

    species_list: an array of species names, e.g. 'anthus_trivialis'.

    Returns a map of species_name -> numpy.ndarray where the ndarray is a D x N
    array, where D = 7734, the MFCC features and N is the number of samples.
  """
  mfcc_map = {}

  for animal in species_list:
    animal_path = _build_path(animal)
    mfccs = scipy.io.loadmat(animal_path)
    mfcc_map[animal] = mfccs['cepstra']

  return mfcc_map


def _build_path(animal):
  return "%s/%s%s.mat" % (TRAIN_PATH, TRAIN_NAME_PARTIAL, animal)

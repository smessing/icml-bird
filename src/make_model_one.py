"""
example.py - An example script to show off some of the functionality of the
             icml-bird codebase.
"""
from env import validator
from input import loader, names
import numpy as np
import output.svm


if __name__ == '__main__':
  # Check for all the required environment variables. This call will raise an
  # exception and kill execution if a required variable is not defined.
  validator.check_environs()

  species_list = names.get_species_list()

  # Read in the training MFCC data for each species, storing a map of
  # species_name -> np.ndarray of size D x N, where D is the number of features
  # (16 for MFCC) and N is the number of samples.
  raw_training_data = loader.load_training_mfccs(species_list)

  positive_examples = raw_training_data
  negative_examples = {}

  # This creates the directory ICML_BIRD_MODEL_PATH/svms/one/.
  output.svm.write_species_training_file(
    positive_examples, negative_examples, 'one')




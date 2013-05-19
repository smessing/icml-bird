"""
make_model_two.py - A script to create the training files for svm_hmm_learn
    (and in the future, the testing files for svm_hmm_classify) to build model
    two as described in todo.md.
"""
from env import validator
from input import loader, names
import numpy as np
import output.svm

if __name__ == '__main__':
  validator.check_environs()

  species_list = names.get_species_list()

  raw_training_data = loader.load_training_mfccs(species_list)

  for species in species_list:
    positive_examples = {}
    positive_examples[species] = raw_training_data[species]
    
    negative_examples = {}
    for other_species in species_list:
      if other_species != species:
        negative_examples[other_species] = raw_training_data[other_species]
    
    training_filename = "train_%s.dat" % species
    output.svm.write_species_training_file(
        positive_examples, negative_examples, 'two', training_filename)



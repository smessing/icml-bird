from input import loader, names
from lib.theano_rnn.rnn import MetaRNN
from lib.theano_rnn.hf import SequenceDataset, hf_optimizer
import numpy as np
import matplotlib.pyplot as plt
import logging

def create_naive_training_data():
  # load mfccs for every training sequence as a list of tuples
  # [(species1, seq_array),...]
  output_dim = len(names.SPECIES)
  train_data = loader.load_training_mfccs(names.get_species_list()).items()
  train_seq_mfccs = [x[1] for x in train_data]

  # get the targets to be binary representations of which species is singing
  target_indices = [x[0] for x in train_data]
  target_indices = [names.get_index_for_species(name) for name in target_indices]
  targets = [np.zeros((mfcc.shape[0], output_dim), dtype='int32') for
      mfcc in train_seq_mfccs]

  for i in range(output_dim):
    targets[i]


from input import loader, names
from lib.theano_rnn.rnn import MetaRNN
from lib.theano_rnn.hf import SequenceDataset, hf_optimizer
import numpy as np
import matplotlib.pyplot as plt
import logging

def create_naive_training_data():
  '''
  For training the most naive RNN model, where each bird sequence is input
  as its own song, where every timestep has the same binary encoding of the
  bird for the file. 

  Returns tuple (train_seq, targets)
  train_seq: list of np arrays representing each sequence to be used for
             training. Each array is seq_length x input dimension
  targets:   list of np arrays representing the outputs of each sequence
             for training. Each array is seq_length x output dimenison
  '''
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

  # set the output binary representations
  for i in range(len(train_data)):
    output_node_index = target_indices[i] - 1 # to index from zero
    targets[i][:, output_node_index] = 1

  return (train_seq_mfccs, targets)
  
def train_binary_ouputs(sequences, targets, num_hidden_nodes, n_updates=250):
  '''
  sequences
    is a list of np arrays, where each array in the list is a sequence of inputs
    to be used in training.
    Each np array is seq_length x input_dimension. The seq_length can vary
    over the sequences, but the input_dimension cannot.
  targets
    a list of no arrays, where each array in the list is the target output
    layer.
    Each np array is seq_length x output_dimensions. The seq_length can vary
    over the sequence, but the output_dimension cannot.
  num_hidden_nodes
    the number of hidden nodes in the RNN
  n_updates
    the number of parameter updates performed by the optimization algorithm
  '''
  assert len(sequences) == len(targets)

  input_dimension = sequences[0].shape[1]
  output_dimension = targets[0].shape[1]

  for i in range(len(sequences)):
    sequences[i] = sequences[i][1:250, :]
    targets[i] = targets[i][1:250, :]

  gradient_dataset = SequenceDataset([sequences, targets], batch_size=None,
      number_batches=500)
  cg_dataset = SequenceDataset([sequences, targets], batch_size=None,
      number_batches=100)

  model = MetaRNN(n_in=input_dimension, n_hidden=num_hidden_nodes,
      n_out=output_dimension, activation='tanh', output_type='binary')

  opt = hf_optimizer(p=model.rnn.params, inputs=[model.x, model.y],
                     s=model.rnn.y_pred,
                     costs=[model.rnn.loss(model.y),
                            model.rnn.errors(model.y)], h=model.rnn.h)

  opt.train(gradient_dataset, cg_dataset, num_updates=n_updates)

  return model, opt

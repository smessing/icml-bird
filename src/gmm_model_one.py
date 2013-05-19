from input import loader, names
import numpy as np
from sklearn.mixture import GMM

def load_training_data():
  '''
  Returns a dict 
    {species_name : { 'labels' : [label_1, label2,...]
                      'samples' : np.array } 
  The labels is of length num_frames
  The array is of size (num_frames x d)
  '''
  train_data = loader.load_training_mfccs(names.get_species_list())
  return train_data

def train_GMMs(train_data, num_centroids=5):
  '''
  train_data:
    dict from species name : np array
    the np arrays are all n_i x d, for each of the i species
  '''
  models = {}
  for species in train_data.keys():
    print 'Training model for %s' % species
    species_model =\
        GMM(n_components=num_centroids, covariance_type='full')
    species_model.fit(train_data[species]['samples'])
    models[species] = species_model

  return models

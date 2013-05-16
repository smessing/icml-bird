"""
  svm.py - Analyze and prepare submission files for Structured SVM models.

  Assumes the following model directory structure:

  ICML_BIRD_MODEL_PATH/model_class/model_name/predictions*
"""
from env import files
from input import names
import os
import sys

ICML_BIRD_MODEL_PATH = 'ICML_BIRD_MODEL_PATH'
PATH_VARS = [ ICML_BIRD_MODEL_PATH ]


def write_submission_file(model_class, model_name):
  model_dir = _make_model_dir(model_class, model_name)

  if not os.path.exists:
    print "%s not found, nothing to do." % model_dir
    sys.exit(-1)

  print "Calculating predictions..."
  predictions = _get_predictions(model_dir, model_name)
  print "...done"

  submission_file = open("%s/submission.csv" % model_dir, 'w')
  print 'Writing to submission file: %s...' % submission_file.name

  submission_file.write('clip,species,probability\n')
  for datetime in predictions:
    for species in predictions[datetime]:
      submission_file.write('%s,%s,%s\n' % \
          (datetime, species, predictions[datetime][species]))
  submission_file.close()

  print '...done'


def _make_model_dir(model_class, model_name):
  return "%s/%s/%s" % \
      (os.environ[ICML_BIRD_MODEL_PATH], model_class, model_name)


def _get_predictions(model_dir, model_name):
  """
    Returns a dictionary of location_datetime -> species -> pseudo-likelihood
    for all prediction files found in model_dir.
  """
  files = os.listdir(model_dir)
  prediction_files = filter(lambda x: "prediction" in x, files)
  predictions_by_datetime = {}

  for prediction_filename in prediction_files:
    prediction_filename = "%s/%s" % (model_dir, prediction_filename)
    prediction_file = open(prediction_filename, 'r')
    predictions = prediction_file.readlines()
    prediction_file.close()
    # Convert from strings to integers (species keys, as defined in the
    # input.names module).
    predictions = map(lambda x: int(x.strip()), predictions)

    # Count up the number of times we predict each label in this file.
    predictions_per_species = {}
    for species_label in predictions:
      if not predictions_per_species.has_key(species_label):
        predictions_per_species[species_label] = 1
      else:
        predictions_per_species[species_label] += 1

    # Normalize predictions to generate a pseudo-likelihood.
    total_num_predictions = len(predictions)
    for species in predictions_per_species:
      predictions_per_species[species] = \
          float(predictions_per_species[species]) / total_num_predictions

    # Add in all missing species with 0 probability
    species = predictions_per_species.keys()
    out_species = filter(lambda x: x not in species, range(1, 36))
    for missing_species in out_species:
      predictions_per_species[missing_species] = 0

    # We convert our datetime into _exactly_ what the string should be in the
    # submission file for later convenience.
    datetime = \
        prediction_filename.split('/')[-1].rstrip('.dat').rstrip(model_name).\
          lstrip('predictions_') + '.wav'

    predictions_by_datetime[datetime] = predictions_per_species

  return predictions_by_datetime

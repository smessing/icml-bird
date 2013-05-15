"""
svm.py - Everything related to writing files for svm_hmm.
"""
from env import files
from input import names
from os import environ

ICML_BIRD_MODEL_PATH = 'ICML_BIRD_MODEL_PATH'
PATH_VARS = [ ICML_BIRD_MODEL_PATH ]


def write_species_training_file(
    positive_examples,
    negative_examples,
    model_name,
    opt_training_filename="train.dat"):
  """
    Write a .dat training file for use with svm_hmm_learn.

    positive_examples: a dictionary of { species_name : numpy.ndarray}
        (where arrays are size D x N) representing all of the species to be
        learned. These examples will be labeled with that species actual label
        from the names module.

    negative_examples: a dictionary of { species_name : numpy.ndarray }
        (where arrays are size D x N) representing all of the species to be
        treated as noise. These examples will be labeled with the NO_SPECIES
        label.

    training_data: a dictionary of { species_name : numpy.ndarray }.

    model_name: a unique string to use to identify this model.

    opt_training_filename: optional filename to use for training file. If not
      specified, defaults to "train.dat"

    Creates the directory ICML_BIRD_MODEL_PATH/model_name and creates the file
    ICML_BIRD_MODEL_PATH/model_name/train.dat that can be used by svm_hmm_learn
    to train the model.
  """
  out_file = _get_out_file(model_name, opt_training_filename)
  print 'Writing examples to %s...' % out_file.name
  try:

    example_num = 1

    for species in positive_examples:
      label = names.get_index_for_species(species)
      _write_example(
          example_num, label, positive_examples[species], out_file, species)
      example_num += 1

    for species in negative_examples:
      label = names.get_index_for_species(names.NO_SPECIES)
      _write_example(
          example_num, label, negative_examples[species], out_file, species)
      example_num += 1

  finally:
    out_file.close()

  print '...done'


def _write_example(index, label, frames, out_file, opt_comment=""):
  """
    Write an example to a file.

    index - The number to use to identify this example.
    label - The numeric label for the sequence.
    frames - an D x N numpy.ndarray.
    out_file - File descriptor (open, write-enabled).
    opt_comment - Optional comment to add at the end of each line of this
                  example. Defaults to the empty string.
  """
  for frame in frames:
    numbered_frame = zip(range(1, len(frame) + 1), frame)
    feature_string = ' '.join(['%s:%s' % (f[0], f[1]) for f in numbered_frame])
    string = '%d qid:%d %s # %s\n' % \
        (label, index, feature_string, opt_comment)
    out_file.write(string)


def _get_out_file(model_name, training_filename):
  """
    Handle generating / opening the training file for this model.

    model_name - The name (string) of the model to create / open the training
                 file for.
  """
  filename = _make_out_filename(model_name, training_filename)
  return files.ensure_file_exists_and_open(filename)


def _make_out_filename(model_name, training_filename):
  """
    Transform a model name into its training filename.

    model_name - The name (string) of the model to make a training filename
                 for. Helps in building the path (will create the model's
                 directory if need be).

    training_filename - The name (string) to use for the actual filename.
  """
  model_path = environ[ICML_BIRD_MODEL_PATH]
  model_dir = "%s/%s" % (model_path, model_name)
  files.ensure_dir_exists(model_dir)
  out_filename = "%s/%s" % (model_dir, training_filename)
  return out_filename


def write_testing_file(
    testing_data,
    model_name,
    opt_testing_filename="test.dat"):
  """
    Write a .dat testing file for use with svm_hmm_classify.

    testing_data: A dictionary of {time_and_location : numpy.ndarray} (where
        arrays are size D x N) representing all of the testing recordings to
        be labeled. These examples will be labeled in the test file as
        names. NO_SPECIES since we don't know the ground truth.

    model_name: a unique string to use to identify this model.

    opt_testing_filename: optinal filename to use for testing file. If not
        specified, defaults to "test.dat"
  """
  out_file = _get_out_file(model_name, opt_testing_filename)
  print 'Writing testing file: %s...' % out_file.name
  try:

    example_num = 1

    for time_and_location in testing_data:
      label = names.NO_SPECIES_KEY
      _write_example(
          example_num,
          label,
          testing_data[time_and_location],
          out_file,
          time_and_location)
      example_num  += 1

  finally:
    out_file.close()

  print '...done'


def write_set_to_label(label_data, model_name):
  """
    Write a .dat labelling file for use with svm_hmm_classify.

    model_name: a unique string to use to identify this model.
  """
  pass

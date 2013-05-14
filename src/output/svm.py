"""
svm.py - Everything related to writing files for svm_hmm.
"""
from input import names, files
from os import environ

ICML_BIRD_MODEL_PATH = 'ICML_BIRD_MODEL_PATH'
PATH_VARS = [ ICML_BIRD_MODEL_PATH ]


def write_species_training_file(
    positive_examples, negative_examples, model_name):
  """
    Write a .dat training file for use with svm_hmm_learn.

    positive_examples: a dictionary of { species_name : numpy.ndarray}
        (where arrays are size D x N) representing all of the species to be
        learned. These examples will be labeled with that species actual label
        from the names module.

    negative_examples: a dictionary of { species_name : numpy.ndarray }
        (where arrays are size D x N) representing all of the species to be
        treated as noise. These examples will be labeled with the NO_BIRD
        label.

    training_data: a dictionary of { species_name : numpy.ndarray }.
    model_name: a unique string to use to identify this model.

    Creates the directory ICML_BIRD_MODEL_PATH/model_name and creates the file
    ICML_BIRD_MODEL_PATH/model_name/train.dat that can be used by svm_hmm_learn
    to train the model.
  """
  species_to_index = names.get_species_to_index_map()
  out_file = _get_training_file(model_name)
  print 'Writing examples to %s...' % out_file.name

  try:

    example_num = 1

    for species in positive_examples:
      label = names.get_index_for_species(species)
      _write_training_example(
          example_num, label, positive_examples[species], out_file, species)
      example_num += 1

    for species in negative_examples:
      label = names.get_index_for_species(names.NO_SPECIES)
      _write_training_example(
          example_num, label, negative_examples[species], out_file, species)
      example_num += 1

  finally:
    out_file.close()

  print '...done.'


def _write_training_example(index, label, frames, out_file, opt_comment=""):
  """
    Write an example to the training file.

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


def _get_training_file(model_name):
  """
    Handle generating / opening the training file for this model.

    model_name - The name (string) of the model to create / open the training
                 file for.
  """
  filename = _make_training_filename(model_name)
  return files.ensure_file_exists_and_open(filename)


def _make_training_filename(model_name):
  """
    Transform a model name into its training filename.

    model_name - The name (string) of the model to make a training filename
    for.
  """
  model_path = environ[ICML_BIRD_MODEL_PATH]
  model_dir = "%s/%s" % (model_path, model_name)
  files.ensure_dir_exists(model_dir)
  out_filename = "%s/train.dat" % (model_dir)
  return out_filename


def write_testing_file(testing_data, model_name):
  """
    Write a .dat testing file for use with svm_hmm_classify.

    model_name: a unique string to use to identify this model.
  """
  pass


def write_set_to_label(label_data, model_name):
  """
    Write a .dat labelling file for use with svm_hmm_classify.

    model_name: a unique string to use to identify this model.
  """
  pass

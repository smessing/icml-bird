from env import validator
from input import loader, names
import output.svm


if __name__ == '__main__':
  validator.check_environs()
  raw_training_data = loader.load_mfccs(names.get_species_list())



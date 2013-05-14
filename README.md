# Dependencies

* Numpy      (`pip install numpy`)
* gfortran   (`brew install gfortran`)
* Scipy      (`pip install scipy`)
* Freetype   (`brew install freetype`)
* Matplotlib (`pip install matplotlib`)
* iPython    (`pip install ipython`)
* Readline   (`pip install readline`)
* SVM Light ([Link to project](http://svmlight.joachims.org/))

# Environment

## Path

The following programs are assumed to be defined in your PATH:

* `svm_hmm_learn`
* `svm_hmm_classify`

## Bash Variables
* `ICML_BIRD_DATA_PATH` should be defined as the absolute path to the data
  directory. E.g.,

    `export ICML_BIRD_DATA_PATH="/var/data/icml-bird/"`

  This is where all the training data is stored on your computer. See the below
  section on how to organize it.

* `ICML_BIRD_MODEL_PATH` should be defined as the absolute path to the model
  directory. E.g.,

    `export ICML_BIRD_DATA_PATH="/var/models/icml-bird/"`

  This is where any special pre-processing data or model parameters will be
  saved, as well as any predictions / evaluation for a particular model. See
  below for more information about its organization.

## Data Directory

It seems easiest to just keep the data directory out of the repository since
it holds a lot of binary data that shouldn't change _too_ much. The only details
mentioned here are those that the codebase makes use of. You can place your
data directory wherever you wish, so long as you set the path variable
`ICML_BIRD_DATA_PATH` to point to the correct location, and set up your data
directory in the proper way.

### `data/`

The top-level directory. Contains:

* `phylogenetic_data.txt` - This file can be found [here](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/phylogenetic_distance.txt). It contains information about the relative phylogenetic distance between bird species.
* `weather.txt` - This file can be found [here](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/weather.txt). It contains information about the weather during each of the test recordings.
* `species_numbers.csv` - The official map between species and ID number. [Link](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/species_numbers.csv).


###  `data/train/`

Contains the directories:

* `mfcc/` - [Link](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/train_set_features.zip).
* `raw/`- [Link](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/train_set.zip).

### `data/test/`

Contains the directories:

* `mfcc/` - [Link](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/test_set_features.zip).
* `raw/`- [Link](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/test_set.zip).

### `data/submit/`

This is where we contain our submission files (saved as text files).

## Model Directory

### `models/`

The top-level directory.

# Dependencies

* Numpy      (pip install numpy)
* gfortran   (brew install gfortran)
* Scipy      (pip install scipy)
* Freetype   (brew install freetype)
* Matplotlib (pip install matplotlib)
* iPython    (pip install ipython)
* Readline   (pip install readline)

# Environment

## Bash Variables
* TRAIN\_DATA\_MFCC\_PATH should be defined as the absolute path to the training
  data's MFCC location. E.g.,

    export TRAIN\_DATA\_MFCC\_PATH="/Users/sam/icml-bird/data/training/mfcc"

## Data Directory

It seems easiest to just keep the data directory out of the repository since
it holds a lot of binary data that shouldn't change _too_ much.

Here is the organization our codebase assumes:

### `data/` - a top-level directory in the repo. Contains:

* `phylogenetic\_data.txt` - This file can be found [here](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/phylogenetic_distance.txt). It contains information about the relative phylogenetic distance between bird species.
* `weather.txt` - This file can be found [here](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/weather.txt). It contains information about the weather during each of the test recordings.
* `species\_numbers.csv` - The official map between species and ID number.

###  `data/train/`

Contains the directories:

* `mfcc/` - [Link](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/train_set_features.zip)
* `raw/`- [Link](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/train_set.zip)

### `data/test/`

* `mfcc/` - [Link](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/test_set_features.zip)
* `raw/`- [Link](http://www.kaggle.com/c/the-icml-2013-bird-challenge/download/test_set.zip)

### `data/submit/`

This is where we contain our submission files (saved as text files).

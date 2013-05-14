# Research

  * Think more about how you might use the phylogenetic or weather data.
    * There is a way with training structured SVMs to give a weight for how
    "bad" it is to make a particular mistake. E.g., labeling A as B vs. labeling
    A as C. Maybe we should increase the weight of confusing birds that are
    phylogenetically more similar?
    * Maybe you could use phylogenetic distance as part of a distance matrix
    for some manifold learning algorithm, like MVE or LLE, to try and
    project the data into some easier space.
  * Plot the spectrograms of some of the birdsongs to get a sense of what
    they are like, esp. w/r/t each other.

# Preprocessing Steps

  * [TODO] PCA / PCA Whitening
  * MVE?

* Models

## Model One: Many Structured SVM

This model consists of training a separate SVM for each bird, using the rest
of the species data as negative training examples. Then, at test each SVM is
asked to classify the test set for their particular bird. We back out
confidence scores using Viterbi decoding since the SVM is isomorphic to an
HMM.

* [DONE] get all data into SVM file format, one large train file.
  * D x N for training example: 16 x 7734 - with this number of features, will
    probably need to implement some sort of PCA / PCA Whitening. Might also
    want to explore using MVE if PCA gives poor results...

* [TODO] get test data into SVM file format, separate files for separate
   runs

* [IN PROGRESS] train model

* [TODO] test model
  * You've yet to address how you're going to solve the problem of generating
    confidence scores from this discriminative model. Since you are using
    SVM-HMM, there should be some way to backout a pseudo arg-max, and
    therefore a probability.

## Model Two: Mixture of Gaussians

This model consists of modeling each birdsong as a distribution over MFCCs or
some other feature set (multivariate gaussian, or maybe something else). Then,
we simply generate likelihood scores of each birdsong on a sound sample, and
use this to generate a ranked ordering, thresholding for "yes" votes somehow.

## Model Three: Recurrent Deep Neural Networks

We could train deep recurrent autoencoders for each bird separately, and for
testing, use the accuracy of the reconstruction of each autoencoder to
determine probability distributions over birds.

We could also create synthetic data where we combine audio from different birds
to recreate what the test data looks like (multiple overlapping birds) and try
to train a single network. We need to think more about how this would actually
work.

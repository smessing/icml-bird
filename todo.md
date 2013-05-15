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

## Model One: Structured SVM

This model isnt likely to work well, but it is low-hanging fruit so we might as
well take the shot. This model consists of training a multi-class, structured
Support Vector Machine (SVM) Hidden Markov Model (HMM) (this is an SVM where
the decision boundary is isomorphic to a _k_th order HHMM) on the entire
training set. Then, at test, we do viterbi decoding and label each frame of a
test song. Then, to make a decision about which birds are in the song, we rank
each bird based on the number of consecutive frames labeled as having that bird
singing. We threshold at a particular number of frames for a yes/no decision,
and use the number of frames (normalized) as our confidence score for each
bird.

### Ideas

* Instead of using the confidence score described above, calculate the actual
  likelihood scores as part of decoding. This may require using something other
  than viterbi (traditional JT), if viterbi cannot back out probabilities (I
  just cant remember ATM). It may also require using different code to do
  the decoding than `svm_hmm_classify` unless that has the ability to give you
  likelihoods.

### Tasks

* [DONE] get all data into SVM file format, one large train file. (see
make_model_one.py)
  * D x N for training example: 16 x 7734 - with this number of features, will
    probably need to implement some sort of PCA / PCA Whitening. Might also
    want to explore using MVE if PCA gives poor results...

* [TODO] Get test data into SVM file format, separate files for separate
   runs

* [IN PROGRESS] Train model

* [TODO] Test model
  * You've yet to address how you're going to solve the problem of generating
    confidence scores from this discriminative model. Since you are using
    SVM-HMM, there should be some way to backout a pseudo arg-max, and
    therefore a probability.

## Model Two: Multiple Structured SVMs.

Goal here is to train a single structured SVM to recognize the call of a single
species (we have it label the calls of all other birds in the training set as
NO_SPECIES). Then in turn we have each individual SVM label the same test
recording, and back out confidence scores + yes/no decision for each species
one at a time.

### Tasks

* [DONE] Write training files (see make_model_two.py)

* [IN PROGRESS] Train model

* [TODO] Test model

## Model Three: Mixture of Gaussians

This model consists of modeling each birdsong as a distribution over MFCCs or
some other feature set (multivariate gaussian, or maybe something else). Then,
we simply generate likelihood scores of each birdsong on a sound sample, and
use this to generate a ranked ordering, thresholding for "yes" votes somehow.

## Model Four: Recurrent Deep Neural Networks

We could train deep recurrent autoencoders for each bird separately, and for
testing, use the accuracy of the reconstruction of each autoencoder to
determine probability distributions over birds.

We could also create synthetic data where we combine audio from different birds
to recreate what the test data looks like (multiple overlapping birds) and try
to train a single network. We need to think more about how this would actually
work.

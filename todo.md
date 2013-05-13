# Research --------------------------------------------------------------------

  * Think more about how you might use the phyologenetic or weather data.

# Preprocessing Steps ---------------------------------------------------------

  * [TODO] PCA / PCA Whitening
  * MVE?

* Models ----------------------------------------------------------------------

## Model One: Structured SVM. ~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~

* [IN PROGRESS] get all data into SVM file format, one large train file.
  * D x N for training example: 16 x 7734 - with this number of features, will
    probably need to implement some sort of PCA / PCA Whitening. Might also
    want to explore using MVE if PCA gives poor results...

* [TODO] get test data into SVM file format, separate files for separate
   runs

* [TODO] train model

* [TODO] test model
  * You've yet to address how you're going to solve the problem of generating
    confidence scores from this discriminative model. Since you are using
    SVM-HMM, there should be some way to backout a pseudo arg-max, and
    therefore a probability.

## Model Two: Mixture of Gaussians. ~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~

This model consists of modeling each birdsong as a distribution over MFCCs or
some other feature set (multivariate guassian, or maybe something else). Then,
we simply generate likelihood scores of each birdsong on a sound sample, and
use this to generate a ranked ordering, thresholding for "yes" votes somehow.
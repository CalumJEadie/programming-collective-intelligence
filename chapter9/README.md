Chapter 9 - Advanced Classification: Kernel Methods and SVMs
============================================================

## Introduction

Comparative concepts covered in previous chapters:

- Decision trees
- Bayesian classifiers
- Neural networks

Concepts covered in chapter 9:

- Lineaer classifiers
- Kernel methods
- Support Vector Machines

Chapter uses the examples of matching people on a dating site.

Interesting properties of this data set:

- Numerical and nominal variables
- Non linear variable relationships

## Matchmaker Dataset

`advancedclassify.py`

## Difficulties with the data

Obvious boundary indicating that people do not go far outside their
own range but that the boundary grows as people grow older.

## Decisin Tree Classifier

Difference between ages is much better than lots of splits.

Decision tree would split the data horizontally and vertically, into
lots of boxes. Does not capture the nature of the relationship
between variables.

Decision trees are often a poor way to determine classes where
have multiple numerical inputs that do not have simple numerical
relationships.

## Basic linear classification

Take average of classes, an average for not matching and an average
for matching.

Classify points by which average they are closer to.

Can use dot product to work this out effeciently.

Linear classifier because equivalent to drawing a line through the
points and classifying based on which side of the line a point is.

## Categorical features

Matchmaker dataset contains numerical and categorical data.

Decision tree can handle both types without preprocessing.

SVMs work only with numerical data.

### Boolean

    yes/no --> 1/-1

### Categories

    interest categories --> numerical variable for each interest, 1 if have interest

    interest categories --> num common interests between people

Counts common interests loses cooccurence information, the
combination of two particular interests may carry more information
than just that there are two interests in common.

e.g. skiing and snowboarding indicates an interest in outdoor sports

Can arrange interests into a hierachy.

    {skiiing, snowboarding} subcategory of {snow sports}

    {snow sports} subcategory of {sports}

So having **skiing** in common may give 1 point and **skiiing** and **snowboarding** in common 0.8 points because the more general **snow sports** category is in common.

### Locations

    locations --> geographical distance

## Scaling the data

By converting category variables into numerical variables now have
a set of variables with very different ranges.

Need to scale the ranges, e.g. onto [0,1]

## Understanding Kernel Methods

Can not always divide a data set up into either side of a straight
line (linear classification). However, can often transform the
dataset such that this is possible.

## Kernel Trick

Finding a dividing line when working with real data sets can
involve transforming to a much higher dimension space.

Replace dot product with a different function gives what the dot
product would give if the data had been transformed into a
different space.

e.g. radial-basis function

## Support-Vector machines

Points near the dividing line are called support-vectors.

Applications:

- classifying facial expressions
- detecting intruders using military datasets
- predicting the structure of proteins from  their sequences
- handwriting recognition
- determining the potential damage during earthquakes

## LIBSVM


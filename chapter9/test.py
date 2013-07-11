"""
Programming Collective Intelligence - Chapter 9
"""

def test_pg_197_to_214():

    """
    Matchmaker Dataset
    """


    import advancedclassify

    agesonly = advancedclassify.loadmatch("agesonly.csv", allnum=True)
    matchmaker = advancedclassify.loadmatch("matchmaker.csv")

    """
    Difficulties with the data
    """

    # Scatter plot of mans age vs womans age
    # O is a match
    # X is not a match

    advancedclassify.plotagematches(agesonly)

    """
    Basic linear classification
    """

    avgs = advancedclassify.lineartrain(agesonly)

    print advancedclassify.dpclassify([30,30], avgs)
    print advancedclassify.dpclassify([30,25], avgs)
    print advancedclassify.dpclassify([25,40], avgs)
    print advancedclassify.dpclassify([48,20], avgs)

    """
    Determing distances using Yahoo! maps
    """

    print advancedclassify.milesdistance("cambride, ma", "new york, ny")

    """
    Creating the new dataset
    """

    numericalset = advancedclassify.loadnumerical()
    print numericalset[0].data

    """
    Scaling the dataset.
    """

    scaledset, scalef = advancedclassify.scaledata(numericalset)
    avgs = advancedclassify.lineartrain(scaledset)
    print numericalset[0].data
    print numericalset[0].match
    print advancedclassify.dpclassify(scalef(numericalset[0].data), avgs)
    print numericalset[11].match
    print advancedclassify.dpclassify(scalef(numericalset[11].data), avgs)

    """
    The kernel trick
    """

    offset = advancedclassify.getoffset(agesonly)
    print offset
    print advancedclassify.nlclassify([30, 30], agesonly, offset)
    print advancedclassify.nlclassify([30, 25], agesonly, offset)
    print advancedclassify.nlclassify([25, 40], agesonly, offset)
    # In contrast to linear classification now recognises that
    # 48, 20 is not a good match
    print advancedclassify.nlclassify([48, 20], agesonly, offset)

    ssoffset = advancedclassify.getoffset(scaledset)

    # 0
    print numericalset[0].match
    # 0
    print advancedclassify.nlclassify(scalef(numericalset[0].data), scaledset, ssoffset)

    # 1
    print numericalset[1].match
    # 1
    print advancedclassify.nlclassify(scalef(numericalset[1].data), scaledset, ssoffset)

    # 0
    print numericalset[2].match
    # 0
    # print advancedclassify.nlclassify(scalef(numericalset[2].data), scaledset, ssoffset)

    # man doesnt want children, women does, otherwise really gd match
    newrow=[28.0, -1, -1, 26.0, -1, 1, 2, 0.8]
    # 0
    print advancedclassify.nlclassify(scalef(numericalset[0].data), scaledset, ssoffset)

    # both want children
    newrow=[28.0, -1, 1, 26.0, -1, 1, 2, 0.8]
    # 0
    print advancedclassify.nlclassify(scalef(numericalset[0].data), scaledset, ssoffset)

# test_pg_197_to_214()

import sys
sys.path.append("/Users/calum/tmp/libsvm-3.17/python")
from svm import *
import svmwrapper

def test_pg_215_to_225():
    
    prob = svm_problem([1, -1], [[1, 0, 1], [-1, 0, -1]])
    param = svm_parameter(kernel_type=LINEAR, C=10)
    m = svm_model(prob, param)

test_pg_215_to_225()
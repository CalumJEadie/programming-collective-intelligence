"""
Programming Collective Intelligence - Chapter 9
"""

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
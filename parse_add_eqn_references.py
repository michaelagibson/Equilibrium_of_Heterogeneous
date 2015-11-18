# coding: ascii
# Copyright (c) Mike Gibson, Craig Carter.
# Distributed under the terms of the MIT License.

"""
This provides methods for regular expression analysis of tex files,
with the purpose of parsing our Gibbs files.
"""

__author__ = "Mike Gibson"
__credits__ = "Craig Carter"
__copyright__ = "Copyright 2015, Mike Gibson"
__version__ = "1.0"
__maintainer__ = "Mike Gibson"
__email__ = "gibson.michael.a@gmail.com"
__date__ = "Nov 17, 2015"

import re
from  more_itertools import unique_everseen

idealform = re.compile(r'\(\d{1,3}\)')
def ref_insert_line(line, form):
    """
    Inserts \ref{} functions into tex files by substituting for a regex.

    :param line: a line from a tex file, in the form of a string,
        which we want to process and insert references into
    :param form: a regular expression specification
        for a string to be replaced.
    :return: a string, wherein all of the strings specified by
        form are replaced by \ref{form}
    """
    # lineIterator = form.search(line)
    # searchAndSub = []
    # lineNew = line
     # while searchAndSub is not None:
    #     searchAndSub = form.search(line)
    #     lineNew = lineNew.replace()

    searchresults = form.findall(line)
    iterableStrings = list(unique_everseen(searchresults))
    lineNew = line
    for substring in iterableStrings:
        lineNew = lineNew.replace(substring, r'(\ref{' + substring[1:-1] + r'})')

    return lineNew

tests = ["some text. An equation (67) appears! some more text",
         "some text. something text in parens (dgwbea) appears! some more text",
         "some text. thing that looks like an equation (6a) appears! some more text",
         "bit of text. one Eq (67) two Eqs (92) are parsed.",
         "bit of text. () should remain the same.",
         "what about something that \d containes \( weird escapes? (55) here"]
# \d means any number, same as the set: [0-9]
# form = \(\d{1,3}\)
for test in tests:
    print ref_insert_line(test, idealform)

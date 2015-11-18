import re
from  more_itertools import unique_everseen
from parse_add_eqn_references import ref_insert_line

idealform = re.compile(r'\(\d{1,3}\)')

with open("/Users/michaelagibson/Dropbox (MIT)/Shared With Others/Gibson_Carter/Gibbs/III-Equilibrium-of-Heterogeneous/tex_docs/Equilibrium_of_Heterogeneous.tex", "rb") as source:
    with open("edited_equations.tex", "wb") as destination:
        for line in source:
            oldString = line
            print oldString
            newstring = ref_insert_line(oldString, idealform)
            if newstring is not oldString:
                print newstring
            destination.write(newstring)
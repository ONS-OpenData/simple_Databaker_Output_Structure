"""
Template/Options file for altering the structure of the .csv flatfile output.
"""

import collections
headermeasurements = [
    ('observation',            "OBS"), 
    ]

headeradditionals = [ 
    ("Dimension_label", "NAME"),
    ("Dimension_value", "VALUE")
]

# conversionsegmentnumbercolumn = "empty11"
SH_Split_OBS = False   # see value set to int value below

# special time handling
SH_Create_ONS_time = False    # forces time into specific formats. disabled for these purposes 
TIME = False  # necessary for now

####  Below this point is derived data (used in old code) from the above tables

# derive the elements of the headernames above into the values below 
headermeasurementnames = list(collections.OrderedDict.fromkeys(k[1]  for k in headermeasurements  if isinstance(k, tuple)))
headermeasurementnamesSet = set(headermeasurementnames) 

# Create variables (This is terrible!)
# TODO: Do this more cleanly e.g. as in https://stackoverflow.com/q/4859217/
exec("%s = '%s'" % (", ".join(headermeasurementnames), "', '".join(map(str, headermeasurementnames))))
exec("SH_Split_OBS = %s" % SH_Split_OBS)

__all__ = list(headermeasurementnames) # don't expose unnecessary items when using `from foo import *`




"""
The Ertië driver. The main workhorse is the __init__.py file in the app subfolder.
"""

########################################################################################################################
# IMPORTS ##############################################################################################################
########################################################################################################################
from app import createApp

########################################################################################################################
# MAIN #################################################################################################################
########################################################################################################################
try:
    # create the Flask app and run it
    ertie = createApp()

except Exception as e:
    # if an Exception occurs, print an error message and quit
    print(f'Critical Error: Unable to initialise Ertië!\nMessage: {e}')
    raise SystemExit(1)
    
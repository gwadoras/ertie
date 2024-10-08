"""
Index for the Ertië website.

:Authors:
    - Gilles Bellot

SPDX-FileCopyrightText: © 2024 Gilles Bellot <gilles.bellot@bell0bytes.eu>
SPDX-License-Identifier: AGPL-3.0-or-later
"""

########################################################################################################################
# INCLUDES #############################################################################################################
########################################################################################################################

# FLASK ################################################################################################################
import flask
import werkzeug.exceptions
from app.factory.conf import Config

########################################################################################################################
# BLUEPRINT ############################################################################################################
########################################################################################################################
bpMain = flask.Blueprint('main', __name__)


########################################################################################################################
# ROUTING ##############################################################################################################
########################################################################################################################

# INDEX ################################################################################################################
@bpMain.route('/')
@bpMain.route('/index')
def index() -> str:
    try:
        payload = {
            'env': Config.ERTIE_ENV,
            'clubName': Config.CLUB_NAME
        }
        return flask.render_template('main/index.html', payload=payload)
    except Exception as e:
        raise werkzeug.exceptions.InternalServerError('Unable to render the main HTML template!') from e
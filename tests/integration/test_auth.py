"""
Tests for the auth blueprint.
Warning: this is a stub

SPDX-FileCopyrightText: © 2024 Gilles Bellot <gilles.bellot@bell0bytes.eu>
SPDX-License-Identifier: AGPL-3.0-or-later
"""

########################################################################################################################
# IMPORTS ##############################################################################################################
########################################################################################################################
from flask import session

########################################################################################################################
# TESTS ################################################################################################################
########################################################################################################################
def test_logout(testClient):
    with testClient:
        testClient.get("/logout")
        assert session.get('user') is None

def test_login(testClient, mocker):
    mocker.patch('authlib.integrations.flask_client.FlaskOAuth2App.authorize_redirect', return_value='success')
    response = testClient.get('/login')
    assert response.status_code == 200
    assert b'success' in response.data

def test_callback(testClient, mocker):
    mocker.patch('authlib.integrations.flask_client.FlaskOAuth2App.authorize_access_token',
                 return_value={'name': 'cosmo', 'email': 'cosmo@best.dog'})
    with testClient:
        response = testClient.get('/callback')
        assert response.status_code == 302
        assert session['user']['name'] == 'cosmo'
        assert session['user']['email'] == 'cosmo@best.dog'
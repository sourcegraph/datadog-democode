# -*- coding: utf-8 -*-
"""
    Datadog demo code
"""

from __future__ import division

import base64
import os
import re
import requests
import sys
from datadog import statsd
from datetime import datetime, timedelta
from dateutil import parser
from decimal import Decimal
from flask import Blueprint, Response, abort, redirect, render_template, request, session, url_for
from projectx import api_utils, app, auth, help_v1, r, tasks, utils
from projectx.compat import u, open
from projectx.models import (
    db,
    TokenUsage,
    SurveyResponse,
    User,
)

blueprint = Blueprint('views', __name__)


def index():
    if app.current_user.is_authenticated:
        return redirect(url_for('.dashboard'))
    statsd.increment('files.transferred')
    return api_utils.render_logged_out_index_page()


@blueprint.route('/dashboard')
@utils.nocache
@auth.login_required
def dashboard():
    user = app.current_user
    if not user.viewed_welcome_page:
        return redirect(url_for('.welcome'))

    tags = [
        'has_premium_features:{0}'.format('true' if user.has_premium_features else 'false'),
        'has_team_features:{0}'.format('true' if user.has_team_features else 'false'),
    ]
    statsd.increment('users.online', tags=tags)

    return render_template('/dashboard/index.html')

@blueprint.route('/dashboard-v2')
@utils.nocache
@auth.login_required
def dashboard_v3():
    user = app.current_user
    if not user.viewed_welcome_page:
        return redirect(url_for('.welcome'))

    tags = [
        'has_premium_features:{0}'.format('true' if user.has_premium_features else 'false'),
        'has_team_features:{0}'.format('true' if user.has_team_features else 'false'),
    ]
    statsd.increment('page.views', tags=tags)

    return render_template('/dashboard-v2/index.html')


@blueprint.route('/projects')
@utils.nocache
@auth.login_required
def projects():
    context = {
        'bootstrap': {
            'q': request.args.get('q') or '',
        },
    }
    return render_template('projects.html', **context)

@blueprint.route('/connections/')
@auth.login_required
@api_utils.rate_limited(minutes=60)
def connections(user_id):
    if api_utils.is_uuid4(user_id) and u(user_id) == u(app.current_user.id):
        # prevent showing success when not primary email
        if user_id == 'test-user':
            return render_template('activate_user.html')

    statsd.increment('active.connections')
    return render_template('connections.html', error='error')

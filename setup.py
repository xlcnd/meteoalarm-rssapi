# -*- coding: utf-8 -*-
# flake8: noqa
# isort:skip_file

# meteoalarm_rssapi -- an 'API' for meteoalarm.eu using the rss feeds.
# Copyright (C) 2021 Alexandre Lima Conde
# SPDX-License-Identifier: GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime as dt
from setuptools import setup
from meteoalarm_rssapi import __version__

PROJECT_NAME = 'meteoalarm_rssapi'
PROJECT_PACKAGE_NAME = 'meteoalarm_rssapi'
PROJECT_LICENSE = 'GPL v3'
PROJECT_LICENSE_URL = 'https://github.com/xlcnd/meteoalarm-rssapi/blob/dev/LICENSE.txt'
PROJECT_AUTHOR = 'Alexandre Lima Conde'
PROJECT_COPYRIGHT = '{}, {}'.format(dt.now().year, PROJECT_AUTHOR)
PROJECT_URL = 'https://github.com/xlcnd/meteoalarm-rssapi'
PROJECT_EMAIL = 'xlcnd@outlook.com'
PROJECT_VERSION = __version__

PROJECT_GITHUB_USERNAME = 'xlcnd'
PROJECT_GITHUB_REPOSITORY = 'meteoalarm-rssapi'

GITHUB_PATH = '{}/{}'.format(PROJECT_GITHUB_USERNAME,
                             PROJECT_GITHUB_REPOSITORY)
GITHUB_URL = 'https://github.com/{}'.format(GITHUB_PATH)

DOWNLOAD_URL = '{}/archive/{}.zip'.format(GITHUB_URL, 'v' + PROJECT_VERSION)
PROJECT_URLS = {
    'Bug Reports': '{}/issues'.format(GITHUB_URL),
    'License': PROJECT_LICENSE_URL,
}

PYPI_URL = 'https://pypi.org/project/{}/'.format(PROJECT_PACKAGE_NAME)
PYPI_CLASSIFIERS = [
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

PACKAGES = [
    'meteoalarm_rssapi',
]

setup(
    name=PROJECT_PACKAGE_NAME,
    version=PROJECT_VERSION,
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    license=PROJECT_LICENSE,
    description='an "API" for meteoalarm.eu using the rss feeds.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords='meteoalarm',
    classifiers=PYPI_CLASSIFIERS,
    install_requires=['feedparser==6.0.2'],
)

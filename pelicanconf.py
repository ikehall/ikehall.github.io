#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ike Hall'
SITENAME = 'Seismic Python'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/IkeOnTweets'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md','ipynb')

PLUGIN_PATHS = ['./plugins', 'pelican-plugins']
PLUGINS = ['ipynb.markup', 'ipynb.liquid', 'assets']
THEME = './theme/syte'

#Theme stuff:
ABOUT = "Musings with python"
CONTACT = 'ike.hall@gmail.com'

TWITTER_INTEGRATION_ENABLED = True
TWITTER_USERNAME = 'IkeOnTweets'

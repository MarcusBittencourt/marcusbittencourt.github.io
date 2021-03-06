#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marcus Bittencourt'
SITENAME = 'devnotes'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('hnlaomie', 'https://hnlaomie.github.io/'))

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/marcus-bittencourt-76a9a2b6/'),
          ('github', 'https://github.com/MarcusBittencourt'),
          ('envelope', 'mailto:marcus.bittencourt.silva@gmail.com'),)

DEFAULT_PAGINATION = 20

THEME = 'attila-1.3'
COLOR_SCHEME_CSS = 'tomorrow.css'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
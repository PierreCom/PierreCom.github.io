#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pierre Comalada'
SITEURL = http://PierreCom.github.io
SITENAME = 'Pierre Comalada - Portfolio'
SITELOGO= '/images/profile_logo.png'
SITETITLE= 'Pierre Comalada'
SITESUBTITLE= 'Data Scientist/Python Developer <br/><br/><br/><br/>   <i>Talking about cool stuff on Data.</i>'

PATH = 'content'
STATIC_PATHS = ['blog', 'images']
ARTICLE_PATHS = ['blog']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/PierreCom/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

THEME = 'themes/Flex'

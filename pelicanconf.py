#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pierre Comalada'
SITEURL = 'https://pierrecom.github.io'
SITENAME = 'Pierre Comalada - Portfolio'
SITELOGO= '/images/profile_logo.png'
SITETITLE= 'Pierre Comalada'
SITESUBTITLE= 'Data Scientist/Python Developer <br/><br/><br/><br/>   <i>Some personal projects.</i>'

ROBOTS = 'index, follow'

PATH = 'content'
STATIC_PATHS = ['blog','images']
ARTICLE_PATHS = ['blog']

#HOME_HIDE_TAGS = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('about', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/PierreCom/'),
('linkedin', 'https://www.linkedin.com/in/pierre-comalada-8a6048b0/'),
)

#USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True
MENUITEMS = (('Categories', '/categories.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

THEME = 'themes/Flex'

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alex'
SITENAME = 'Alex Johnstone'
SITEURL = 'https://alexjj.com'

THEME = 'themes/great-bustard'

INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'
PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}/index.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}/'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
STATIC_PATHS = ['images', 'extra', 'admin']

TAG_SAVE_AS = 'blog/tag/{slug}/index.html'
TAG_URL = 'blog/tag/{slug}/'

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
YEAR_ARCHIVE_URL = 'blog/{date:%Y}/'

CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
CATEGORY_URL = 'blog/category/{slug}/'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
#MENUITEMS = [('Home', '/'), ('Blog', '/blog/')]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/B2452245.txt': {'path': 'B2452245.txt'},
}

TEMPLATE_PAGES = {'admin/index.html': 'admin/index.html'}

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
SUMMARY_MAX_LENGTH = 50
DEFAULT_DATE_FORMAT = '%d %B %Y'

# Home page settings
RECENT_ARTICLES_COUNT = 5

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Github', 'https://github.com/alexjj'),
          ('LinkedIn', 'https://www.linkedin.com/in/ajjohnstone/'),
         ('Steam', 'https://steamcommunity.com/id/captainlag/'),)

DEFAULT_PAGINATION = False

# Plugins

PLUGIN_PATHS =['plugins']
PLUGINS = ['pelican-toc']

# Table of contents

TOC = {
    'TOC_HEADERS': '^h[1-3]',
    'TOC_RUN': 'false',
    'TOC_INCLUDE_TITLE': 'false',
    }

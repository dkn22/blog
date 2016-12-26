#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from os.path import expanduser

AUTHOR = u'Luiz Irber'

SITENAME = u'Gabbleblotchits'
SITESUBTITLE = u"Vogon Poetry, Computers and (some) biology"
SITEURL = ''  # change in publishconf.py

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
MENUITEMS = [('Archives', '/archives.html'),
             ('About', 'http://luizirber.org/resume'),
             ('BlurBlog', 'http://luizirber.newsblur.com'),
             ('Home Page', 'http://luizirber.org')]
NEWEST_FIRST_ARCHIVES = True

MARKUP = ('md', )

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

#Github include settings
GITHUB_USER = 'luizirber'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = None

# STATIC_OUT_DIR requires pelican 3.3
STATIC_OUT_DIR = ''
STATIC_PATHS = ['images', 'figures', 'downloads', 'content/favicon.png']
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

EXTRA_PATH_METADATA = {
    'content/favicon.png': {'path': 'favicon.png'},
}

# Theme and plugins
#  Theme requires http://github.com/duilio/pelican-octopress-theme/
#  Plugins require http://github.com/getpelican/pelican-plugins/
THEME = expanduser('~/prj/pelican-octopress-theme/')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['summary', 'sitemap',
           'liquid_tags.img', 'liquid_tags.include_code',
           'ipynb.liquid',
           'simple_footnotes']

# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
#
# This header file is automatically generated by the notebook plugin
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
EXTRA_HEADER = open('_nb_header_mod.html').read().decode('utf-8')

# Sharing
TWITTER_USER = 'luizirber'
GOOGLE_PLUS_USER = '109253845740829085771'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = False
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'


# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'


# Search
SEARCH_BOX = True


# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

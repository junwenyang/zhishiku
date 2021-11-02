from app import config
import os

DATA_SEARCH_INDEX='searchIndex'
DATA_PAGES='pages'
DATA_UPLOAD='upload'

SIDEBAR_PATH = os.path.join(config.DATA_DIR, 'sidebar.md')
md_ext = ['markdown.extensions.extra', 'markdown.extensions.abbr', 'markdown.extensions.attr_list',
          'markdown.extensions.def_list', 'markdown.extensions.fenced_code', 'markdown.extensions.footnotes',
          'markdown.extensions.tables', 'markdown.extensions.admonition', 'markdown.extensions.codehilite',
          'markdown.extensions.legacy_attrs', 'markdown.extensions.legacy_em', 'markdown.extensions.meta',
          'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'markdown.extensions.smarty',
          'markdown.extensions.toc', 'markdown.extensions.wikilinks']

class RedisStore(object):
    G_SHARE='gshare:'

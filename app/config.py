import os
import sys
from celery import Celery
from celery.schedules import crontab
from datetime import datetime,timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging

VERSION = '0.0.1'

APP_NAME = "lywiki"
APP_ICON = "/static/assets/images/logo.png"
APP_START_YEAR = '2021'
# define the neccery dir
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')
PAGE_DIR = os.path.join(DATA_DIR, 'pages')
DOWNLOAD_URL_PREFIX = '/data/upload/'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
if not os.path.exists(PAGE_DIR):
    os.makedirs(PAGE_DIR)

###########################
# Flask Config
###########################
DEBUG = False if os.environ.get('SECRET_KEY',None) else True
SECRET_KEY = r'\xe0N\rl\x8f\xe3\x13\xa6\xdd\r\xea\xd1\x03\x9f+\x1f3\xa3\x18\x1eia\xa2\xbf' if DEBUG else os.environ.get('SECRET_KEY',None)#
# Extract and use X-Forwarded-For/X-Forwarded-Proto headers?
ENABLE_PROXY_FIX = False
# max upload size 100MB
MAX_CONTENT_LENGTH = 1024 * 1024 * 100

#Custom for redis session
REDIS_HOST='localhost'
REDIS_PORT=6379

###########################
# Logging config File Path
###########################
LOG_CFG_FILE = os.path.join(os.path.dirname(__file__), 'logging.json')
LOG_MAIL_RECIEVER = "1158088593@qq.com"

###########################
# mail config
###########################
MAIL_SERVER = 'smtp.qq.com'#'smtp-mail.outlook.com'#'smtp.163.com'
MAIL_PORT = 994#587#994
MAIL_USE_SSL = True
#MAIL_USE_TLS = True
MAIL_USERNAME = '1158088593@qq.com'
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '') 
MAIL_DEFAULT_SENDER = '1158088593<1158088593@qq.com>'

###########################
# SQLAchemy config
###########################
# deprecated SQLALCHEMY_COMMIT_ON_TEARDOWN=True
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_DATABASE_URI = r'sqlite:///D:\\work\\pyprj\\mdwiki-py\\data\\app.db'
# SQLALCHEMY_DATABASE_URI='mysql://root:1234@localhost/'
SQLALCHEMY_ECHO = True if DEBUG else False
SQLALCHEMY_TRACK_MODIFICATIONS = True if DEBUG else False
# SQLALCHEMY_POOL_SIZE=10
# SQLALCHEMY_POOL_TIMEOUT=60
# SQLALCHEMY_POOL_RECYCLE=2*60*60
# SQLALCHEMY_MAX_OVERFLOW=50

###########################
# Flask-Cache config
###########################
# null,simple,memcached,redis,filesystem
CACHE_TYPE = 'redis' 
CACHE_DEFAULT_TIMEOUT = 3600
CACHE_KEY_PREFIX = 'mdwiki_cache_'
# CACHE_REDIS_HOST='127.0.0.1'
# CACHE_REDIS_PORT='6379'
# CACHE_REDIS_PASSWORD=''
# CACHE_REDIS_DB=1 #0
# redis://username:password@localhost:6379/0
CACHE_REDIS_URL = 'redis://'+REDIS_HOST+':'+str(REDIS_PORT)+'/1'

###########################
# Flask-WTF config
###########################
#the default is 3600 seconds buf when we write post > 1 hour ,it occurs errors when we submit save,
#so, set None to fix it. None stand for it bounds to session lifetime.
#please see http://flask-wtf.readthedocs.io/en/stable/config.html
WTF_CSRF_TIME_LIMIT=None

###########################
# flask-babel config
###########################
BABEL_DEFAULT_LOCALE = 'zh'
# Your application default translation path
BABEL_DEFAULT_FOLDER = 'translations'
# The allowed translation for you app
LANGUAGES = {
    #'en': {'flag': 'us', 'name': 'English'},
    # 'fr': {'flag': 'fr', 'name': 'French'},
     'zh': {'flag': 'cn', 'name': 'Chinese'},
}

###########################
# Celery config
###########################
# CELERY_CONFIG={
#     'BROKER_URL' : 'redis://'+REDIS_HOST+':'+str(REDIS_PORT)+'/0',
#     #CELERY_RESULT_BACKEND = 'redis://localhost/0'
#     'CELERY_TASK_SERIALIZER':'json',
#     #CELERY_ACCEPT_CONTENT=['json']
#     'CELERY_RESULT_SERIALIZER':'json',
#     'CELERY_TIMEZONE' : 'Asia/Shanghai',
#     # CELERY_TASK_PUBLISH_RETRY=3

#     # ?????????????????????:
#     'CELERYBEAT_SCHEDULE' : {
#         'bak-every-day': {
#         'task': 'tasks.backup',
#             # 'schedule': timedelta(seconds=30),#timedelta(minutes=50)
#         'schedule': crontab( hour='4',day_of_month='*/1')
#             #'args':
#         }
#     },
#     'loglevel': 'DEBUG' if DEBUG else 'INFO',
#     'traceback': True,
#     'include':['app.util.tasks']
# }

'''CELERY_TASK_PUBLISH_RETRY_POLICY={
    'max_retries': 3, #??????3??????0 or None??????????????????
    'interval_start': 0,
    'interval_step': 0.2,
    'interval_max': 0.2,
}'''


###########################
# Flask-Security config
###########################
# bcrypt, sha512_crypt, or pbkdf2_sha512
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = SECRET_KEY  # default None
SECURITY_EMAIL_SENDER = MAIL_DEFAULT_SENDER
SECURITY_LOGIN_URL = '/login'
SECURITY_LOGOUT_URL = '/logout'
# SECURITY_REGISTER_URL='/register'
# SECURITY_RESET_URL='/reset'
# SECURITY_CHANGE_URL='/change'
# SECURITY_CONFIRM_URL='/confirm'
SECURITY_POST_LOGIN_VIEW = '/'
SECURITY_POST_LOGOUT_VIEW = '/'

# SECURITY_REGISTERABLE=True ????????????????????????????????????False
# SECURITY_SEND_REGISTER_EMAIL=True #?????????????????????????????????
# SECURITY_CONFIRMABLE=True #???????????????????????????????????????

# SECURITY_RECOVERABLE  ????????????????????????????????????False
SECURITY_TRACKABLE = True  # ?????????False???????????????????????????????????????????????????????????????True?????????????????????????????????
SECURITY_CHANGEABLE = True  # ????????????????????????????????????False????????????True???????????????SECURITY_CHANGE_URL?????????
# SECURITY_EMAIL_SUBJECT_REGISTER   ??????????????????????????????
# SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE
# SECURITY_EMAIL_SUBJECT_PASSWORD_RESET
# SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE
# SECURITY_EMAIL_SUBJECT_CONFIRM
# SECURITY_SEND_PASSWORD_CHANGE_EMAIL=True
# SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL=True
# SECURITY_CONFIRM_EMAIL_WITHIN ???????????????????????????????????????5 days.
# SECURITY_RESET_PASSWORD_WITHIN    ?????????????????????????????????????????????5 days.
# SECURITY_DEFAULT_REMEMBER_ME  ?????????False?????????????????????????????????



###########################
# aliyun oss
###########################
oss = {
    'api_key': os.environ.get('aliyun_api_key', ''),
    'secret_key': os.environ.get('aliyun_secret_key', ''),
    'bucket_name': 'mdwikidata',
    'inner_endpoint': None if DEBUG else 'http://oss-cn-beijing-internal.aliyuncs.com',  
    'out_endpoint': 'http://oss-cn-beijing.aliyuncs.com'
}



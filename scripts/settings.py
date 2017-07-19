MJT_LOCAL_FOLDER = "C:\\Span_Procedures_Cloud\\ACCOUNTDATA_MJT\\"
MJT_REMOTE_FOLDER = "ftpbackup/gmi_reconcile/"
MJT_HOST="66.70.157.69"
MJT_USER = "ftpwebuser"
MJT_PWD = "NmrOBVNF"

MONGO_CONNSTR = 'mongodb://tmqr:tmqr@10.0.1.2/tmldb_v2?authMechanism=SCRAM-SHA-1'
MONGO_EXO_DB = 'tmldb_v2'
MONGO_SPAN_DATA = 'span_data'

PUSH_SLACK_LOGGING = True

#
# RabbitMQ credentials
RABBIT_HOST = '10.0.1.2'
RABBIT_USER = 'tmqr'
RABBIT_PASSW = 'tmqr'

# Allow any settings to be defined in settings_local.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
try:
    from settings_local import *
except ImportError as e:
    if "settings_local" not in str(e):
        raise e
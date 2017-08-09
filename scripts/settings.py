MJT_LOCAL_FOLDER = "C:\\Span_Procedures_Cloud\\ACCOUNTDATA_MJT\\"
MJT_REMOTE_FOLDER = "ftpbackup/gmi_reconcile/"
TMQR_BACKUP_DAILYPNL_HOST = "66.70.157.69"
TMQR_BACKUP_DAILYPNL_USER = "ftpwebuser"
TMQR_BACKUP_DAILYPNL_PWD = "NmrOBVNF"

CME_SPAN_LOCAL_FOLDER = "C:\\Span_Procedures_Cloud\\SPAN_DATA"
CME_SPAN_REMOTE_FOLDER = "span/data/cme/"
CME_SPAN_HOST = "ftpstc.cmegroup.com"
CME_SPAN_USER = "anonymous"
CME_SPAN_PWD = ""
CME_SPAN_REMOTE_BACKUP_FOLDER = "ftpbackup/span_data/cme/"

ICE_SPAN_LOCAL_FOLDER = "C:\\Span_Procedures_Cloud\\SPAN_DATA"
ICE_SPAN_REMOTE_FOLDER = "span/data/ice/"
ICE_SPAN_HOST = "ftpstc.cmegroup.com"
ICE_SPAN_USER = "anonymous"
ICE_SPAN_PWD = ""
ICE_SPAN_REMOTE_BACKUP_FOLDER = "ftpbackup/span_data/ice/"

NYB_SPAN_LOCAL_FOLDER = "C:\\Span_Procedures_Cloud\\SPAN_DATA"
NYB_SPAN_REMOTE_FOLDER = "span/data/nyb/"
NYB_SPAN_HOST = "ftpstc.cmegroup.com"
NYB_SPAN_USER = "anonymous"
NYB_SPAN_PWD = ""
NYB_SPAN_REMOTE_BACKUP_FOLDER = "ftpbackup/span_data/nyb/"

LIFFE_SPAN_LOCAL_FOLDER = "C:\\Span_Procedures_Cloud\\SPAN_DATA"
LIFFE_SPAN_REMOTE_FOLDER = "span/data/liffe/"
LIFFE_SPAN_HOST = "ftpstc.cmegroup.com"
LIFFE_SPAN_USER = "anonymous"
LIFFE_SPAN_PWD = ""
LIFFE_SPAN_REMOTE_BACKUP_FOLDER = "ftpbackup/span_data/liffe/"


# MONGO_CONNSTR = 'mongodb://tmqr:tmqr@10.0.1.2/tmldb_v2?authMechanism=SCRAM-SHA-1'
# MONGO_EXO_DB = 'tmldb_v2'
# MONGO_SPAN_DATA = 'span_data'

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
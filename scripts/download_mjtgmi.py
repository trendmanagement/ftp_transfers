import os, sys, paramiko
from settings import *
from tradingcore.signalapp import SignalApp, APPCLASS_DATA
from ftp_transfer_code.ftp_transferring import FtpTransfer

ftpt = FtpTransfer()

ftpt.clear_local_folder(MJT_LOCAL_FOLDER)

ftpt.download_file_sftp(MJT_REMOTE_FOLDER,
                        ftpt.get_position_file(),
                        MJT_LOCAL_FOLDER,
                        hostname=TMQR_BACKUP_DAILYPNL_HOST,
                        username = TMQR_BACKUP_DAILYPNL_USER,
                        password = TMQR_BACKUP_DAILYPNL_PWD,
                        slack_message = "MJT GMI DATA")

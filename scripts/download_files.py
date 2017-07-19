import os, sys, paramiko
from settings import *
from tradingcore.signalapp import SignalApp, APPCLASS_DATA
from tradingcore.messages import *

def download_file_sftp(remote_dir, filename, local_dir, hostname, username, password):

    port = 22

    try:
        os.path.exists(local_dir) or os.makedirs(local_dir)

        local_path = os.path.join(local_dir, filename)
        remote_path = remote_dir + '/' + filename

        client = paramiko.SSHClient()
        #client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(hostname=hostname,  port=port, username=username, password=password)

        ftp = client.open_sftp()
        ftp.get(remote_path, local_path)
        #ftp.get('ftpbackup/gmi_reconcile/TMQR_PNL_20170718.csv', 'C:\\TEST\\TMQR_PNL_20170718.csv')
        ftp.close()

        if PUSH_SLACK_LOGGING:
            signalapp = SignalApp('historicaldata', APPCLASS_DATA, RABBIT_HOST, RABBIT_USER, RABBIT_PASSW)

            signalapp.send(MsgStatus('HISTORICAL_LOAD',
                                          'Loaded MJT GMI DATA {0}'.format(filename), notify=True))


    finally:
        client.close()

def get_position_file_mask():
    from datetime import datetime
    from datetime import timedelta
    from time import strftime

    currentDate = datetime.now()
    # day of the week as an integer, where Monday is 0 and Sunday is 6.
    if currentDate.weekday() == 0:
        currentDate = currentDate - timedelta(days=3)
    elif currentDate.weekday() == 6:
        currentDate = currentDate - timedelta(days=2)
    else:
        currentDate = currentDate - timedelta(days=1)

    return "TMQR_PNL_" + currentDate.strftime("%Y%m%d") + ".csv"

def clear_local_folder(path_to_clear):
    import glob

    files = glob.glob(path_to_clear + '*')
    for f in files:
        os.remove(f)

clear_local_folder(MJT_LOCAL_FOLDER)

file = get_position_file_mask() #'TMQR_PNL_20170718.csv'

download_file_sftp(MJT_REMOTE_FOLDER, file, MJT_LOCAL_FOLDER,
                   hostname=MJT_HOST, username = MJT_USER, password = MJT_PWD)
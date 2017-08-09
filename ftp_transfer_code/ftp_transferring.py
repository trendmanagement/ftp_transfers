from scripts.settings import *
import os, paramiko
from ftplib import FTP
from tradingcore.signalapp import SignalApp, APPCLASS_DATA
from tradingcore.messages import *


class FileInfo():
    def __init__(self, date_string='', year='', file_name=''):
        self.date_string = date_string
        self.year = year
        self.file_name = file_name

class FtpTransfer():
    def download_file_sftp(self, remote_dir, file_info, local_dir, hostname, username, password, slack_message):

        port = 22

        try:
            os.path.exists(local_dir) or os.makedirs(local_dir)

            local_path = os.path.join(local_dir, file_info.file_name)
            remote_path = remote_dir + file_info.file_name

            client = paramiko.SSHClient()
            # client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(hostname=hostname, port=port, username=username, password=password)

            ftp = client.open_sftp()
            ftp.get(remote_path, local_path)
            # ftp.get('ftpbackup/gmi_reconcile/TMQR_PNL_20170718.csv', 'C:\\TEST\\TMQR_PNL_20170718.csv')

            ftp.close()

            if PUSH_SLACK_LOGGING:
                signalapp = SignalApp('ftptransfer', APPCLASS_DATA, RABBIT_HOST, RABBIT_USER, RABBIT_PASSW)

                signalapp.send(MsgStatus('FTP_TRANSFER',
                                         'SUCCESS {0} {1}'.format(slack_message, file_info.file_name), notify=True))

        except:
            if PUSH_SLACK_LOGGING:
                signalapp = SignalApp('ftptransfer', APPCLASS_DATA, RABBIT_HOST, RABBIT_USER, RABBIT_PASSW)

                signalapp.send(MsgStatus('FTP_TRANSFER',
                                         'FAILED {0} {1}'.format(slack_message,file_info.file_name), notify=True))


        finally:
            client.close()


    def upload_file_sftp(self, remote_dir, file_info, local_dir, hostname, username, password, slack_message):

        port = 22

        try:
            os.path.exists(local_dir) or os.makedirs(local_dir)

            local_path = os.path.join(local_dir, file_info.file_name)

            remote_dir = remote_dir + file_info.year + '/'
            remote_path = remote_dir + file_info.file_name

            client = paramiko.SSHClient()
            # client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(hostname=hostname, port=port, username=username, password=password)

            ftp = client.open_sftp()

            try:
                ftp.mkdir(remote_dir)
            except:
                pass

            ftp.put(local_path, remote_path)

            ftp.close()

            if PUSH_SLACK_LOGGING:
                signalapp = SignalApp('ftptransfer', APPCLASS_DATA, RABBIT_HOST, RABBIT_USER, RABBIT_PASSW)

                signalapp.send(MsgStatus('FTP_TRANSFER',
                                         'SUCCESS {0} {1}'.format(slack_message, file_info.file_name), notify=True))

        except:
            if PUSH_SLACK_LOGGING:
                signalapp = SignalApp('ftptransfer', APPCLASS_DATA, RABBIT_HOST, RABBIT_USER, RABBIT_PASSW)

                signalapp.send(MsgStatus('FTP_TRANSFER',
                                         'FAILED {0} {1}'.format(slack_message,file_info.file_name), notify=True))


        #finally:
        client.close()


    def download_file_ftp(self, remote_dir, file_info, local_dir, hostname, username, password, slack_message):

        port = 22

        try:
            os.path.exists(local_dir) or os.makedirs(local_dir)

            local_path = os.path.join(local_dir, file_info.file_name)
            remote_path = remote_dir + file_info.file_name

            #client = paramiko.SSHClient()
            # client.load_system_host_keys()
            #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ftp = FTP(hostname, username, username + ":" + password + "@" + hostname)
            #ftp.login()

            local_file = open(local_path, "wb")

            ftp.retrbinary('RETR ' + remote_path, local_file.write)

            ftp.quit()
            local_file.close()

            #ftp = client.open_sftp()
            #ftp.get(remote_path, local_path)
            # ftp.get('ftpbackup/gmi_reconcile/TMQR_PNL_20170718.csv', 'C:\\TEST\\TMQR_PNL_20170718.csv')

            #ftp.close()

            if PUSH_SLACK_LOGGING:
                signalapp = SignalApp('ftptransfer', APPCLASS_DATA, RABBIT_HOST, RABBIT_USER, RABBIT_PASSW)

                signalapp.send(MsgStatus('FTP_TRANSFER',
                                         'SUCCESS {0} {1}'.format(slack_message, file_info.file_name), notify=True))

        except:
            if PUSH_SLACK_LOGGING:
                signalapp = SignalApp('ftptransfer', APPCLASS_DATA, RABBIT_HOST, RABBIT_USER, RABBIT_PASSW)

                signalapp.send(MsgStatus('FTP_TRANSFER',
                                         'FAILED {0} {1}'.format(slack_message,file_info.file_name), notify=True))


        finally:
            ftp.close()

    def get_datestr_for_file(self, format_type):
        from datetime import datetime
        from datetime import timedelta
        #from time import strftime

        currentDate = datetime.now()
        # day of the week as an integer, where Monday is 0 and Sunday is 6.
        if currentDate.weekday() == 0:
            currentDate = currentDate - timedelta(days=3)
        elif currentDate.weekday() == 6:
            currentDate = currentDate - timedelta(days=2)
        else:
            currentDate = currentDate - timedelta(days=1)


        year = currentDate.strftime("%Y")

        if format_type == 2:
            date_string = currentDate.strftime("%m%d")
        else:
            date_string = currentDate.strftime("%Y%m%d")

        file_info = FileInfo(date_string=date_string,year=year)

        return  file_info



    def get_position_file(self):
        file_info = self.get_datestr_for_file(1)
        file_info.file_name = \
            "TMQR_PNL_" + file_info.date_string + ".csv"
        return file_info

    def get_cme_span_file(self):
        #return "cme." + self.get_datestr_for_file(1)['string_name'] + ".c.pa2.zip"

        file_info = self.get_datestr_for_file(1)
        file_info.file_name = \
            "cme." + file_info.date_string + ".c.pa2.zip"
        return file_info

    def get_cme_ice_span_file(self):
        #return "ice." + self.get_datestr_for_file(1)['string_name'] + ".pa6.zip"

        file_info = self.get_datestr_for_file(1)
        file_info.file_name = \
            "ice." + file_info.date_string + ".pa6.zip"
        return file_info

    def get_cme_nyb_span_file(self):
        #return "nyb" + self.get_datestr_for_file(2)['string_name'] + "f.sp6.zip"

        file_info = self.get_datestr_for_file(2)
        file_info.file_name = \
            "nyb" + file_info.date_string + "f.sp6.zip"
        return file_info

    def get_liffe_span_file(self):
        #return "cme." + self.get_datestr_for_file(1)['string_name'] + ".c.pa2.zip"

        file_info = self.get_datestr_for_file(1)
        file_info.file_name = \
            "liffe." + file_info.date_string + ".s.pa6.zip"
        return file_info


    def clear_local_folder(self, path_to_clear):
        #import os
        try:
            filelist = [f for f in os.listdir(path_to_clear)]
            for f in filelist:
                os.remove(os.path.join(path_to_clear, f))
        except:
            return

    def unzip_span_file(self,file_info,local_dir):
        import zipfile

        local_path = os.path.join(local_dir, file_info.file_name)

        zip_ref = zipfile.ZipFile(local_path)
        zip_ref.extractall(local_dir)
        zip_ref.close()
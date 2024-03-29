from settings import *
from ftp_transfer_code.ftp_transferring import FtpTransfer

ftpt = FtpTransfer()

ftpt.clear_local_folder(CME_SPAN_LOCAL_FOLDER)

cme_file = ftpt.get_cme_span_file()

ftpt.download_file_ftp(CME_SPAN_REMOTE_FOLDER,
                       cme_file,
                       CME_SPAN_LOCAL_FOLDER,
                        hostname=CME_SPAN_HOST,
                        username = CME_SPAN_USER,
                        password = CME_SPAN_PWD,
                        slack_message = "SPAN FTP CME DATA")

ftpt.upload_file_sftp(CME_SPAN_REMOTE_BACKUP_FOLDER,
                      ftpt.get_cme_span_file(),
                      CME_SPAN_LOCAL_FOLDER,
                        hostname=TMQR_BACKUP_DAILYPNL_HOST,
                        username = TMQR_BACKUP_DAILYPNL_USER,
                        password = TMQR_BACKUP_DAILYPNL_PWD,
                        slack_message = "CME SPAN BACKUP DATA")

ftpt.unzip_span_file(cme_file,CME_SPAN_LOCAL_FOLDER)



ice_file = ftpt.get_cme_ice_span_file()

ftpt.download_file_ftp(ICE_SPAN_REMOTE_FOLDER,
                       ice_file,
                       ICE_SPAN_LOCAL_FOLDER,
                        hostname=ICE_SPAN_HOST,
                        username = ICE_SPAN_USER,
                        password = ICE_SPAN_PWD,
                        slack_message = "SPAN FTP ICE DATA")

ftpt.upload_file_sftp(ICE_SPAN_REMOTE_BACKUP_FOLDER,
                      ice_file,
                      ICE_SPAN_LOCAL_FOLDER,
                        hostname=TMQR_BACKUP_DAILYPNL_HOST,
                        username = TMQR_BACKUP_DAILYPNL_USER,
                        password = TMQR_BACKUP_DAILYPNL_PWD,
                        slack_message = "ICE SPAN BACKUP DATA")

ftpt.unzip_span_file(ice_file,ICE_SPAN_LOCAL_FOLDER)



nyb_file = ftpt.get_cme_nyb_span_file()

ftpt.download_file_ftp(NYB_SPAN_REMOTE_FOLDER,
                       nyb_file,
                       NYB_SPAN_LOCAL_FOLDER,
                        hostname=NYB_SPAN_HOST,
                        username = NYB_SPAN_USER,
                        password = NYB_SPAN_PWD,
                        slack_message = "SPAN FTP NYB DATA")

ftpt.upload_file_sftp(NYB_SPAN_REMOTE_BACKUP_FOLDER,
                      nyb_file,
                      NYB_SPAN_LOCAL_FOLDER,
                        hostname=TMQR_BACKUP_DAILYPNL_HOST,
                        username = TMQR_BACKUP_DAILYPNL_USER,
                        password = TMQR_BACKUP_DAILYPNL_PWD,
                        slack_message = "NYB SPAN BACKUP DATA")

ftpt.unzip_span_file(nyb_file,NYB_SPAN_LOCAL_FOLDER)



liffe_file = ftpt.get_liffe_span_file()

ftpt.download_file_ftp(LIFFE_SPAN_REMOTE_FOLDER,
                       liffe_file,
                       LIFFE_SPAN_LOCAL_FOLDER,
                        hostname=LIFFE_SPAN_HOST,
                        username = LIFFE_SPAN_USER,
                        password = LIFFE_SPAN_PWD,
                        slack_message = "SPAN FTP LIFFE DATA")

ftpt.upload_file_sftp(LIFFE_SPAN_REMOTE_BACKUP_FOLDER,
                      liffe_file,
                      LIFFE_SPAN_LOCAL_FOLDER,
                        hostname=TMQR_BACKUP_DAILYPNL_HOST,
                        username = TMQR_BACKUP_DAILYPNL_USER,
                        password = TMQR_BACKUP_DAILYPNL_PWD,
                        slack_message = "LIFFE SPAN BACKUP DATA")

ftpt.unzip_span_file(liffe_file,LIFFE_SPAN_LOCAL_FOLDER)
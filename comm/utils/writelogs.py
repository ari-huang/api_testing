import logging
import time
import sys
import os


class MyLogs:
    def __init__(self, log_path):
        # 確認 Log 目錄是否存在
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        # log 以日為單位
        runtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        logfile_debug = os.path.join(log_path, runtime + '.log')
        logfile_err = os.path.join(log_path, runtime + '_error.log')

        # 初始化 logger 為 Debug level
        logger = logging.getLogger()
        # 把 Log level 改到 config , 方便後續調整
        logger.setLevel(logging.DEBUG)
        logger.handlers = []

        # 設定 debug handler 要輸出的 file
        fh = logging.FileHandler(logfile_debug, mode='a+')
        fh.setLevel(logging.DEBUG)

        # 設定error handler 要輸出的 file
        fh_err = logging.FileHandler(logfile_err, mode='a+')
        fh_err.setLevel(logging.ERROR)

        # 將 debug login 輸出到 console
        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(logging.INFO)

        # 定義各類 Log 輸出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        fh_err.setFormatter(formatter)
        sh.setFormatter(formatter)

        # 最後將設定封裝進logger
        logger.addHandler(fh)
        logger.addHandler(fh_err)
        logger.addHandler(sh)

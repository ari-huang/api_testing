import os
import pytest


if __name__ == "__main__":
    from comm.utils import writelogs
    from config import *

    """
        1. init logging
        2. setting log folder
    """
    writelogs.MyLogs(ROOT_DIR + "logs")

    # 執行參數
    args_list = [
        "-vs",  # 輸出cnosole log
        "main/testcase",
        "-n",
        str(RC["process"]),  # 併行測試，目前暫時不用
        "--maxfail",
        "100",  # 多少次fail就強制停止測試
        "-o",
        "junit_family=xunit2",
        "--junitxml=./testcase_report.xml",
        "--alluredir",
        REPORT_DIR + "/json",
        "--clean-alluredir",  # 清空上一次 json report folder
        "--disable-warnings",
        "--testrail",
        "--tr-config=testrail.cfg",
    ]

    
    # 執行 pytest 指令
    pytest.main(args_list)
   

    # 測試完成後先清空 report 再產生 allure report
    cmd = "allure generate --clean %s -o %s " % (
        REPORT_DIR + "/json",
        REPORT_DIR + "/html",
    )
    os.system(cmd)

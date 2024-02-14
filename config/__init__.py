"""
初始化全部配置
"""
from comm.utils.readyaml import read_yaml_data
import os

# 根目錄
ROOT_DIR = str(os.path.realpath(__file__)).split("config")[0].replace("\\", "/")

# config 配置
API_CONFIG = ROOT_DIR + "config/apiconfig.yml"
RUN_CONFIG = ROOT_DIR + "config/runconfig.yml"
DB_CONFIG = ROOT_DIR + "config/dbconfig.yml"
# Cookies Path
COOKIES_CONFIG = ROOT_DIR + "config/cookies.yml"
# run config
RC = read_yaml_data(RUN_CONFIG)
INTERVAL = RC["interval"]
PROJECT_NAME = RC["project_name"]
PROCESS = RC["process"]

# 指定執行測試目錄
TEST_DIR = ROOT_DIR + PROJECT_NAME + "/testcase"
# report 位置
REPORT_DIR = ROOT_DIR + "/report"

from comm.utils.readyaml import read_yaml_data
from config import DB_CONFIG, PROJECT_NAME
from comm.db import *
import logging
import time

dbcfg = read_yaml_data(DB_CONFIG)[PROJECT_NAME]


def query_mysql(sql):
    """SQL Select 查詢

    :param sql: 查詢語句
    :return:
    """
    # db config
    timeout = dbcfg["timeout"]
    address = dbcfg["mysql_info"]["address"]
    user = dbcfg["mysql_info"]["user"]
    auth = dbcfg["mysql_info"]["auth"]
    db = dbcfg["mysql_info"]["db"]
    # init MySQL
    host, port = address.split(":")
    mysql = MysqlServer(host, int(port), db, user, auth)
    logging.info("excution query >>> {}".format(sql))
    # if timeout raise exception
    for i in range(int(timeout)):
        try:
            result = mysql.query(sql, is_dict=True)
            mysql.close()
            if result:
                return result
            else:
                time.sleep(1)
        except Exception as e:
            raise Exception("select fail >>> {}".format(e))
    else:
        return []

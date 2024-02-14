import logging
import allure
import time
from config import INTERVAL
from comm.unit import apimethod


def send_request(case_data):
    """
    封裝 request & Log & report
    :param case_data: 測試資料
    :return:
    """
    try:
        # 獲取測試資料
        req_data = case_data.get("request_data")
        host = req_data.get("host")
        address = req_data.get("address")
        method = req_data.get("method").upper()
        headers = req_data.get("headers")
        mime_type = headers.get("Content-Type", "")
        parameter = req_data.get("parameter", "")
        # file = case_data["request_data"]["file"]
    except Exception as e:
        raise KeyError("獲取測試資料失敗：{}".format(e))

    request_url = host + address
    logging.info("=" * 150)
    logging.info("Request URL：%s" % request_url)
    logging.info("Request Headers: %s" % str(headers))
    logging.info("Request Parameter: %s" % str(parameter))

    # 判斷API Method
    if method == "POST":
        logging.info("HTTP Method: POST")
        with allure.step("HTTP POST"):
            allure.attach(name="Request URL", body=request_url)
            allure.attach(name="Request Headers", body=str(headers))
            allure.attach(name="Request Parameter", body=str(parameter))
        result = apimethod.post(
            headers=headers,
            address=request_url,
            mime_type=mime_type,
            data=parameter,
        )
    elif method == "GET":
        logging.info("HTTP Method: GET")
        with allure.step("HTTP GET"):
            allure.attach(name="Request URL", body=request_url)
            allure.attach(name="Request Headers", body=str(headers))
            allure.attach(name="Request Parameter", body=str(parameter))
        result = apimethod.get(headers=headers, address=request_url, data=parameter)
    elif method == "PUT":
        logging.info("HTTP Method: PUT")
        with allure.step("HTTP PUT"):
            allure.attach(name="Request URL", body=request_url)
            allure.attach(name="Request Headers", body=str(headers))
            allure.attach(name="Request Parameter", body=str(parameter))
        result = apimethod.put(
            headers=headers,
            address=request_url,
            mime_type=mime_type,
            data=parameter,
        )
    elif method == "DELETE":
        logging.info("HTTP Method: DELETE")
        with allure.step("HTTP DELETE"):
            allure.attach(name="Request URL", body=request_url)
            allure.attach(name="Request Headers", body=str(headers))
            allure.attach(name="Request Parameter", body=str(parameter))
        result = apimethod.delete(headers=headers, address=request_url, data=parameter)
    else:
        result = {"code": None, "data": None}
    logging.info("HTTP Response：\n %s" % str(result))
    time.sleep(INTERVAL)
    return result

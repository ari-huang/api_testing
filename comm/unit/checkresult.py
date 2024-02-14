import re
import allure
import logging


def check_result(check_type, expected_data, actual_data):
    """比對結果
    :param check_type (check_code/check_data/regular_check)
    :param expected_data
    :param data: actual_data
    :return:
    """
    logging.info(check_type + " %s | %s" % (expected_data, actual_data))
    if check_type == 'check_code':
        with allure.step("驗證HTTP Code"):
            allure.attach(name="實際code", body=str(actual_data))
            allure.attach(name="預期code", body=str(expected_data))
        assert expected_data == actual_data, "expected %s but got %s" % (
            expected_data,
            actual_data,
        )

    elif check_type == 'check_data':
        with allure.step("驗證Response Data"):
            allure.attach(name='實際data', body=str(actual_data))
            allure.attach(name='預期data', body=str(expected_data))
        assert expected_data == actual_data, "expected response %s but got %s" % (
            expected_data,
            actual_data,
        )

    elif check_type == "regular_check":
        with allure.step("regular result"):
            allure.attach(name='實際data', body=str(actual_data))
            allure.attach(name='預期格式', body=str(expected_data))
        assert re.match(expected_data, actual_data), "expected response %s but got %s" % (
            expected_data,
            actual_data,
        )
    elif check_type == "check_schema":
        """單純驗證 type"""
        pass

    logging.info('驗證成功')


def check_database():
    """驗證DB資料
    :return:
    """
    pass

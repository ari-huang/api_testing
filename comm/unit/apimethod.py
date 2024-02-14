import os
import json
import logging
import requests
import simplejson
from requests_toolbelt import MultipartEncoder
from comm.utils.readyaml import write_yaml_file, read_yaml_data
from config import PROJECT_NAME, COOKIES_CONFIG
import pdb


def post(headers, address, mime_type, timeout=30, data=None, files=None, cookies=None):
    """
    :param headers
    :param address
    :param mime_type:（form_data,raw）
    :param timeout
    :param data: request parameter
    :param files
    :param cookies:
    :return:
    """
    if "form_data" in mime_type:
        for key in files:
            value = files[key]
            if "/" in value:
                files[key] = (os.path.basename(value), open(value, "rb"))
        enc = MultipartEncoder(fields=files)
        headers["Content-Type"] = enc.content_type
        response = requests.post(
            url=address,
            data=enc,
            headers=headers,
            timeout=timeout,
            cookies=cookies,
            verify=False,
        )

    elif "application/json" in mime_type:
        response = requests.post(
            url=address,
            json=data,
            headers=headers,
            timeout=timeout,
            files=files,
            cookies=cookies,
            verify=False,
        )
    else:
        response = requests.post(
            url=address,
            data=data,
            headers=headers,
            timeout=timeout,
            files=files,
            cookies=cookies,
            verify=False,
        )
    try:
        result = {
            "code": response.status_code,
            "data": response.json(),
            "headers": response.headers,
        }

        return result
    except json.decoder.JSONDecodeError:
        return {"code": response.status_code, "data": response.text}
    except simplejson.errors.JSONDecodeError:
        return {"code": response.status_code, "data": response.text}
    except Exception as e:
        logging.exception("ERROR")
        logging.error(e)
        raise


def get(headers, address, data, timeout=30, cookies=None):
    """
    get request
    :param headers: request headers
    :param address: URL
    :param data: request parameter
    :param timeout
    :param cookies:
    :return:
    """
    response = requests.get(
        url=address,
        params=data,
        headers=headers,
        timeout=timeout,
        cookies=cookies,
        verify=False,
    )

    if response.status_code == 301:
        response = requests.get(url=response.headers["location"], verify=False)
    try:

        result = {
            "code": response.status_code,
            "data": response.json(),
            "headers": response.headers,
        }

        return result
    except json.decoder.JSONDecodeError:
        return {"code": response.status_code, "data": response.text}
    except simplejson.errors.JSONDecodeError:
        return {"code": response.status_code, "data": response.text}
    except Exception as e:
        logging.exception("ERROR")
        logging.error(e)
        raise


def put(headers, address, mime_type, timeout=30, data=None, files=None, cookies=None):
    """
    put request
    :param headers: request headers
    :param address: URL
    :param mime_type: content格式（form_data,raw）
    :param timeout
    :param data: request parameter
    :param files: file path
    :param cookies:
    :return:
    """
    if mime_type == "raw":
        data = json.dumps(data)
    elif mime_type == "application/json":
        # data = json.dumps(data)
        response = requests.put(
            url=address,
            json=data,
            headers=headers,
            timeout=timeout,
            files=files,
            cookies=cookies,
            verify=False,
        )

    try:
        result = {
            "code": response.status_code,
            "data": response.json(),
            "headers": response.headers,
        }

        return result
    except json.decoder.JSONDecodeError:
        return {"code": response.status_code, "data": response.text}
    except simplejson.errors.JSONDecodeError:
        return {"code": response.status_code, "data": response.text}
    except Exception as e:
        logging.exception("ERROR")
        logging.error(e)
        raise


def delete(headers, address, data, timeout=30, cookies=None):
    """
    delete request
    :param headers: request headers
    :param address: URL
    :param data: request parameter
    :param timeout
    :param cookies:
    :return:
    """
    response = requests.delete(
        url=address,
        params=data,
        headers=headers,
        timeout=timeout,
        cookies=cookies,
        verify=False,
    )
    try:
        result = {
            "code": response.status_code,
            "data": response.json(),
            "headers": response.headers,
        }

        return result
    except json.decoder.JSONDecodeError:
        return {"code": response.status_code, "data": response.text}
    except simplejson.errors.JSONDecodeError:
        return {"code": response.status_code, "data": response.text}
    except Exception as e:
        logging.exception("ERROR")
        logging.error(e)
        raise


def save_cookie(
    headers, address, mime_type, timeout=30, data=None, files=None, cookies=None
):
    """
    保存cookie信息
    :param headers: request headers
    :param address: URL
    :param mime_type: content格式（form_data,raw）
    :param timeout
    :param data: request parameter
    :param files: file path
    :param cookies:
    :return:
    """
    if "data" in mime_type:
        response = requests.post(
            url=address,
            data=data,
            headers=headers,
            timeout=timeout,
            files=files,
            cookies=cookies,
            verify=False,
        )
    else:
        response = requests.post(
            url=address,
            json=data,
            headers=headers,
            timeout=timeout,
            files=files,
            cookies=cookies,
            verify=False,
        )
    try:
        cookies = response.cookies.get_dict()
        # 寫入cookies結果
        aconfig = read_yaml_data(COOKIES_CONFIG)
        aconfig[PROJECT_NAME]["cookies"] = cookies
        write_yaml_file(COOKIES_CONFIG, aconfig)
        logging.debug("cookies save：{}".format(cookies))
    except json.decoder.JSONDecodeError:
        return response.status_code, None
    except simplejson.errors.JSONDecodeError:
        return response.status_code, None
    except Exception as e:
        logging.exception("ERROR")
        logging.error(e)
        raise

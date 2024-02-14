import string
import random
import datetime
from dateutil.relativedelta import relativedelta


def random_str(str_len):
    """random a-zA-Z0-9
    ex: B459Fa381Cb2ceDf
        :param str_len: 指定長度
        :return:
    """
    try:
        str_len = int(str_len)
    except ValueError:
        raise Exception("[ %s ] str_len not integer!" % str_len)
    strings = ''.join(random.sample(string.hexdigits, +str_len))
    return strings


def random_int(scope):
    """random number
    ex: 111
        :param scope: 數字範圍
        :return:
    """
    try:
        start_num, end_num = scope.split(",")
        start_num = int(start_num)
        end_num = int(end_num)
    except ValueError:
        raise Exception("[ %s ] scope not integer!" % str(scope))
    if start_num <= end_num:
        number = random.randint(start_num, end_num)
    else:
        number = random.randint(end_num, start_num)
    return number


def random_float(data):
    """隨機浮點數
    ex: 111.111111
        :param data: 数组
        :return:
    """
    try:
        start_num, end_num, accuracy = data.split(",")
        start_num = int(start_num)
        end_num = int(end_num)
        accuracy = int(accuracy)
    except ValueError:
        raise Exception("[ %s ]data not float！" % data)

    if start_num <= end_num:
        number = random.uniform(start_num, end_num)
    else:
        number = random.uniform(end_num, start_num)
    number = round(number, accuracy)
    return number


def random_choice(data):
    """random list
    :param data: []
    :return:
    """
    _list = data.split(",")
    each = random.choice(_list)
    return each


def get_date_mark(now, mark, num):
    if 'y' == mark:
        return now + relativedelta(years=num)
    elif 'm' == mark:
        return now + relativedelta(months=num)
    elif 'd' == mark:
        return now + relativedelta(days=num)
    elif 'h' == mark:
        return now + relativedelta(hours=num)
    elif 'M' == mark:
        return now + relativedelta(minutes=num)
    elif 's' == mark:
        return now + relativedelta(seconds=num)
    else:
        raise Exception("expr [ %s ] Error！, please use [年y,月m,日d,時h,分M,秒s]!" % mark)


def generate_date(expr=''):
    """ex:2022-06-14
    :param expr: 日期regex，如d-1代表前一天
    :return:
    """
    today = datetime.date.today()
    if expr:
        try:
            mark = expr[:1]
            num = int(expr[1:])
        except (TypeError, NameError):
            raise Exception("expr [ %s ] Error！" % expr)
        return get_date_mark(today, mark, num)
    else:
        return today


def generate_datetime(expr=''):
    """ex:2022-06-14 04:09:41
    :param expr: 日期regex，如d-1代表前一天
    :return:
    """
    now = datetime.datetime.now().replace(microsecond=0)
    if expr:
        try:
            mark = expr[:1]
            num = int(expr[1:])
        except (TypeError, NameError):
            raise Exception("expr [ %s ] Error！" % expr)
        return get_date_mark(now, mark, num)
    else:
        return now


def generate_timestamp(expr=''):
    """
    :param expr: 日期regex，如d-1代表前一天
    :return:
    """
    datetime_obj = generate_datetime(expr)
    return int(datetime.datetime.timestamp(datetime_obj)) * 1000


if __name__ == '__main__':
    # random
    print(random_str(16))
    print(random_int("100,200"))
    print(random_float("200,100,5"))
    print(random_choice("aaa,bbb,ccc"))

    # date
    # print(generate_date())
    # print(generate_datetime())
    # print(generate_date('m+1'))
    # print(generate_datetime('d+1'))
    # print(generate_timestamp('s+100'))

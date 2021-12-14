def fizz_buzz(input_num_start, input_num_end):
    """
    sum of numbers which division without remainder to 3 and 5 between input_num_start and input_num_end
    :param input_num_start: left limit, int
    :param input_num_end: right limit, int
    :return: sum, int
    """

    result = 0
    for num in range(input_num_start, input_num_end + 1):
        if num % 3 == 0 and num % 5 == 0:
            result += num

    return result


# print('0-3', fizz_buzz(0, 3))  # 0
# print('0-3', fizz_buzz(0, 5))  # 0
# print('0-3', fizz_buzz(15, 15))  # 15
# print('0-3', fizz_buzz(1000, 20000))  # 13303500

def plural_form(input_num, form_1, form_2, form_3):
    '''
    returns plural form of input_num related of last digit of num
    :param input_num: int
    :param form_1: str
    :param form_2: str
    :param form_3: str
    :return: str
    '''
    result = ''
    last_digit = input_num % 10
    if last_digit in range(2, 5):
        result = form_2
    elif last_digit == 1 and input_num != 11:
        result = form_1
    else:
        result = form_3

    return result


# print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))  # 1 яблоко
# print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))  # 3 яблока
# print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))  # 5 яблок
# print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))  # 11 яблок
# print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))  # 121 яблоко
# print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))  # 125 яблок
# print(1000, plural_form(1000, 'яблоко', 'яблока', 'яблок'))  # 1000 яблок
# print(0, plural_form(0, 'яблоко', 'яблока', 'яблок'))  # 0 яблок
def html(*args, **kwargs):
    def decorator(decorated_func):
        def wrapper(input_attribute):
            result_wrapper = decorated_func(input_attribute)

            if kwargs:
                result_wrapper = f'>{result_wrapper}'
                # for index in args:
                for k, v in kwargs.items():
                    result_wrapper = f' {k}="{v}"{result_wrapper}'  # <
                for index in args:
                    result_wrapper = f'<{index}{result_wrapper}</{index}>'
            else:
                for index in args:
                    result_wrapper = f'<{index}>{result_wrapper}</{index}>'
            # if kwargs:
            #     for k, v in kwargs.items():
            #         result_wrapper = f'<{k}>="{v}"{result_wrapper}</{k}>'
                        # TODO Сделать цикл для *args и **wargs вместе (в одной строке)
            return result_wrapper

        return wrapper

    return decorator


@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))

# <body><div width="200" height="100"><a href="https://yandex.ru/">ссылка на яндекс</a></div></body>  # should be
# <body><div height="100" width="200"><a href="https://yandex.ru/">ссылка на яндекс</a></div></body>  # result
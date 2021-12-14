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


def html(tag, **kwargs):
    '''
    decorate functions into opening and closing tags
    :param tag: str
    :param kwargs: dicts
    :return:
    '''

    def decorator(decorated_func):

        def wrapper(input_attribute):

            attributes = ''
            text = decorated_func(input_attribute)

            for k, v in kwargs.items():
                attributes += f' {k}="{v}"'
            opening_tag = f'<{tag}'
            closing_tag = f'</{tag}>'

            return f'{opening_tag}{attributes}>{text}{closing_tag}'

        return wrapper

    return decorator


@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))







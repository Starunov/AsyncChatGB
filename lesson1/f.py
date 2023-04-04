def center(*args, header: bool = False):
    result = ''
    text_color = '\033[0m'  # стандарт

    if header:
        text_color = '\033[33m'  # желтый

    for item in args:
        item = str(item)
        result += f"{item.center(30, ' ')}"

    return text_color + result

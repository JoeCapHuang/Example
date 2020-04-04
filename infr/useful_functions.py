def get_digits(text):
    numbers = ''
    for i in text:
        if i.isdigit():
            numbers += i
    return int(numbers)
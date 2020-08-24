def divide(x,y):
    try:
        re = x//y
    except ZeroDivisionError as error:
        raise ValueError('错误') from error
    else:
        return re
print(divide(8,0))
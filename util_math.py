def floor(num):
    remainder = num % 1
    return num - remainder

def ceil(num):
    remainder = num % 1
    return num + (1 - remainder)

def round(num):
    remainder = num % 1
    if remainder < 0.5:
        return floor(num)
    else:
        return ceil(num)
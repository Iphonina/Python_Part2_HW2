def to_hexadecimal(num):
    hex_chars = "0123456789ABCDEF"
    result = ""

    if num == 0:
        result = "0"

    while num > 0:
        memory = num % 16
        result = hex_chars[memory] + result
        num = num // 16

    return result


number = int(input("Введите целое число: "))
hex_string = to_hexadecimal(number)
print("Шестнадцатеричное представление числа:", hex_string)

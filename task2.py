# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму
# и произведение* дробей. Для проверки своего кода используйте модуль fractions.

def calculate(number1, number2):
    numerator1, denominator1 = number1.split('/')
    numerator2, denominator2 = number2.split('/')

    numerator_sum = int(numerator1) * int(denominator2) + int(numerator2) * int(denominator1)
    denominator_sum = int(denominator1) * int(denominator2)

    numerator_multi = int(numerator1) * int(numerator2)
    denominator_multi = int(denominator1) * int(denominator2)

    return f"Сумма: {numerator_sum}/{denominator_sum}", f"Произведение: {numerator_multi}/{denominator_multi}"


number1 = input("Введите первую дробь (вида a/b): ")
number2 = input("Введите вторую дробь (вида a/b): ")

sum_result, multi_result = calculate(number1, number2)
print(sum_result)
print(multi_result)

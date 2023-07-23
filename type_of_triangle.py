def type_of_triangle(value: tuple):
    # unpacking values into a, b and c
    a, b, c = value
    if a + b <= c or b + c <= a or c + a <= b:
        return 'Not A Triangle'
    elif a == b and b == c:
        return 'Equilateral'
    elif a == b or b == c or c == a:
        return 'Isosceles'
    else:
        return 'Scalene'


if __name__ == '__main__':
    values = [(20, 20, 23), (20, 20, 20), (20, 21, 22), (13, 14, 30)]
    for value in values:
        print(type_of_triangle(value))

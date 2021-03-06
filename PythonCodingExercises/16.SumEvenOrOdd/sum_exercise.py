def sum_eo(n, t):
    """Sum even or odd numbers in range.
    Return the sum of even or odd natural numbers, in the range
    1..n-1.
    :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
    :return: The sum of the even or odd numbers in the range.
            Returns -1 if `t` is not 'e' or 'o'."""

    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


x = sum_eo(11, 'spam')


print(x)


print("*" * 10)


y = sum_eo(10, 'e')


print(y)


print("*" * 10)


z = sum_eo(7, 'o')


print(z)


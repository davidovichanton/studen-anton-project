def get_sum(a, b):
    if a == b:
        return a
    if a < b:
        list_value = list(range(a, b + 1, 1))
        return sum(list_value)
    if a > b:
        list_value = list(range(b, a + 1, 1))
        return sum(list_value)

def get_sum1(a, b):
    fin_result = 0
    if a == b:
        return a
    else:
        for i in range(a, b+1):
            fin_result+=i
    return fin_result



if __name__ == '__main__':
    result = get_sum(-10, -20)
    print(result)
    result = get_sum(10, 20)
    print(result)

    result = get_sum1(-10, -20)
    print(result)
    result = get_sum1(10, 20)
    print(result)

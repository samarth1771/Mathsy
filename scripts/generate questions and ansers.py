import random


# a = random.randint(0, 99)
# print(a)
# b = random.randint(0, 99)
# print(b)
# c = a + b
# print(c)


# print(random.randint(0, 99))
# print(random.randint(0, 99))

def Addition(num1, num2):
    return num1 + num2


def Substraction(num1, num2):
    return num1 - num2


def Multiplication(num1, num2):
    return num1 * num2


def Division(num1, num2):
    return int(num1 / num2)


def get_options(digit):
    if len(digit) == 1:
        return random.randint(1, 9)
    if len(digit) == 2:
        return random.randint(9, 99)
    if len(digit) == 3:
        return random.randint(99, 999)


def get_question(difficulty, operation):
    if difficulty == 'easy':
        d = dict();
        if operation == '+':
            a = random.randint(1, 99)
            b = random.randint(1, 20)
            c = Addition(a, b)
        if operation == '-':
            a = random.randint(1, 99)
            b = random.randint(1, 10)
            c = Substraction(a, b)
        if operation == '*':
            a = random.randint(1, 10)
            b = random.randint(1, 5)
            c = Multiplication(a, b)
        if operation == '/':
            a = random.randint(2, 5)
            b = random.randint(1, 9) * a
            c = Division(b, a)
        d['operator1'] = a
        d['operator2'] = b
        d['answer'] = c
        d['option'] = get_options(str(c))
        return d

    if difficulty == 'medium':
        d = dict();
        if operation == '+':
            a = random.randint(1, 200)
            b = random.randint(1, 99)
            c = Addition(a, b)
        if operation == '-':
            a = random.randint(1, 200)
            b = random.randint(1, 50)
            c = Substraction(a, b)
        if operation == '*':
            a = random.randint(1, 15)
            b = random.randint(1, 5)
            c = Multiplication(a, b)
        if operation == '/':
            a = random.randint(2, 9)
            b = random.randint(1, 15) * a
            c = Division(b, a)
        d['operator1'] = a
        d['operator2'] = b
        d['answer'] = c
        d['option'] = get_options(str(c))
        return d

    if difficulty == 'hard':
        d = dict();
        if operation == '+':
            a = random.randint(1, 999)
            b = random.randint(1, 200)
            c = Addition(a, b)
        if operation == '-':
            a = random.randint(1, 500)
            b = random.randint(1, 150)
            c = Substraction(a, b)
        if operation == '*':
            a = random.randint(1, 20)
            b = random.randint(1, 10)
            c = Multiplication(a, b)
        if operation == '/':
            a = random.randint(2, 10)
            b = random.randint(10, 20) * a
            c = Division(b, a)
        d['operator1'] = a
        d['operator2'] = b
        d['answer'] = c
        d['option'] = get_options(str(c))
        return d


response = get_question(difficulty='easy', operation='/')
print(response.get('operator1'))
print(response)

list = [2, 3, 6, 8]
random_list = random.sample(list, 4)
print(random_list)


# a_list = [1, 2, 1]
# a_set = set(a_list)
# is_duplicates = len(a_list) != len(a_set)
# print(contains_duplicates)

def shuffle_options(ans):
    option1 = str(get_options(ans))
    option2 = str(get_options(ans))
    option3 = str(get_options(ans))
    option4 = ans
    options = [option1, option2, option3, option4]
    random_options = random.sample(options, 4)
    return random_options


def contains_duplicates(list_of_options):
    set_of_options = set(list_of_options)
    is_duplicates = len(list_of_options) != len(set_of_options)
    return is_duplicates


def remove_duplicate(ans):
    shufulled = shuffle_options(ans)
    if contains_duplicates(shufulled):
        print("true duplicates")
        while True:
            shufulled = shuffle_options(ans)
            if not contains_duplicates(shufulled):
                break

    return shufulled


print(remove_duplicate('1'))

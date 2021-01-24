import random, string
low = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
num = list(string.digits)
punct = list(string.punctuation)
punct.remove('<')
punct.remove('>')
random.shuffle(low)
random.shuffle(upper)
random.shuffle(num)
random.shuffle(punct)
full = low + upper + num + punct
random.shuffle(full)
def rand_comb(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.choices(range(n),k = r))
    return tuple(pool[i] for i in indices)
def pass_generator(lenght : int):
    while True:
        password = list(rand_comb(full, lenght - 4))
        password.append(random.choice(upper))
        password.append(random.choice(low))
        password.append(random.choice(num))
        password.append(random.choice(punct))
        random.shuffle(password)
        password = ''.join(password)
        yield password
length = int(input("enter lenght"))
generator = pass_generator(length)
print(next(generator))
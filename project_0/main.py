import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count=0
    named_numbers=set()
    random_number = np.random.randint(1, 101)
    hight_border = 101
    lower_border=1
    while True:
        separated_number = int((hight_border+lower_border) / 2)
        #print("половина",separated_number,"число для угадывания",hight_border)
        if random_number == number:
            return count
        if number > separated_number:
            lower_border=int((lower_border+hight_border)/2)
        elif number < separated_number:
            hight_border = separated_number
        #print("от",lower_border,"до",hight_border,"рандом",random_number)
        while True:
            random_number= np.random.randint(lower_border,hight_border)
            if random_number not in named_numbers:
                named_numbers.add(random_number)
                break
        count+=1
count_ls = []
np.random.seed(16)
random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

for number in random_array:
    count_ls.append(game_core_v3(number))

score = int(np.mean(count_ls))
print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

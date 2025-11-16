import asyncio
from random import randint as rint


# ДЗ — Корутины и asyncio
# Задача №1
async def say_hello(n):
    await asyncio.sleep(n)
    print('Привет!')


# Задача №2
async def delayed_print(text, delay):
    await asyncio.sleep(delay)
    print(text)


# Задача №3
async def task(delay):
    await asyncio.sleep(delay)
    print(f'Корутина N{delay}')


def create_list_coroutine(coroutine, n):
    list_corut = [coroutine(i) for i in range(1, n)]
    return list_corut


# Задача №4
async def countdown(n):
    if isinstance(n, int) and n >= 1:
        print(f'Вывод чисел от {n} до 1 с интервалом в 1 сек.')
        for i in range(n, 0, -1):
            await asyncio.sleep(1)
            print(i)
    else:
        print('Значение n должно быть >= 1')
        return


# Задача №5
async def fetch_data(index):
    delay = rint(1, 5)
    print(f'\033[31mЗапущена задача №{index}\033[0m с паузой {delay}сек.')
    await asyncio.sleep(delay)
    print(f'\033[32mДанные задачи №{index}\033[0m с паузой {delay}сек. \033[32mполучены\033[0m')


async def coroutine_func(index):
    return int(input(f'Введите число №{index} для суммирования >> '))


async def main():
    await say_hello(1)
    await delayed_print('Начало программы', 2)
    await delayed_print('Окончание программы', 4)
    await asyncio.gather(*create_list_coroutine(task, 4))
    await countdown(13)
    await asyncio.gather(*create_list_coroutine(fetch_data, 14))
    a, b, c = await asyncio.gather(*create_list_coroutine(coroutine_func, 4))
    print(a + b + c)


if __name__ == '__main__':
    asyncio.run(main())

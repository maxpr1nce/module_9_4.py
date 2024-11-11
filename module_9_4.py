first = 'Мама мыла раму'
second = 'Рамена мало было'

# Запись lambda-функции в выражение map
result = list(map(lambda x, y: x == y, first, second))

print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(str(item) + '\n')  # Записываем каждую запись с новой строки
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice


class MysticBall:
    def __init__(self, *words):
        # Сохраняем переданные слова в атрибуте words
        self.words = words

    def __call__(self):
        # Возвращаем случайное слово из words
        return choice(self.words)


# Создаем объект класса MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное')

# Примеры вызова объекта, который сработает как функция
print(first_ball())
print(first_ball())
print(first_ball())
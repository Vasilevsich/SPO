"""
    Реализуемые методы:
    1. Добавление пары
    2. Получение значения по ключу
    3. Удаление пары
    """


class HashTable:
    def __init__(self):
        self.keys = []
        for i in range(0, 1024):
            self.keys.append(None)

    def put_value(self, key, value):
        self.keys[hash(key) % len(self.keys)] = [key, value]

    def get_value(self, key):
        if self.keys[hash(key) % len(self.keys)]:
            return self.keys[hash(key) % len(self.keys)][1]

    def delete_value(self, key):
        self.keys[hash(key) % len(self.keys)] = None

    def print_hash_table(self):
        print('-----Print Hash Table-----')
        for i in self.keys:
            if i:
                print(i)
        print('-----End of output-----')

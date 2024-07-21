import threading
import time
from queue import PriorityQueue

# Класс для столов
class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

# Класс для симуляции работы кафе
class Cafe:
    def __init__(self, tables):
        self.queue = PriorityQueue()
        self.tables = tables

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 20:
            print(f"Посетитель номер {customer_number} прибыл.")
            customer_thread = Customer(customer_number, self)
            customer_thread.start()  # Используем start() для начала потока
            customer_number += 1
            time.sleep(1)  # Искусственная задержка между приходами посетителей

    def serve_customer(self, customer):
        table_found = False
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                self.queue.put(customer.number, customer)
                print(f"Посетитель номер {self.queue.get(customer.number)} сел за стол {table.number}.")
                time.sleep(5)  # Время обслуживания 5 секунд
                table.is_busy = False  # Освободили столик после обслуживания
                print(f"Посетитель номер {customer.number} покушал и ушёл.")
                table_found = True

        if not table_found:
            self.queue.put(customer.number,customer)

            print(f"Посетитель номер {customer.number} ожидает свободный стол.")


# Класс для посетителей
class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)

# Создаем столы в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
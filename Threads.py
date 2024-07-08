from threading import Thread
import time

class Knight(Thread):
    def __init__(self, NameOfKnght, power):
        self.NameOfKnght = NameOfKnght
        self.power = power
        super().__init__()

    def run(self):
        print(f"{self.NameOfKnght} на нас напали!")
        invaders = 100
        i = 0
        while invaders != 0:
            i += 1
            invaders -= self.power
            print(f"{self.NameOfKnght} сражается {i} день(дня), осталось {invaders} воинов")
            if invaders == 0:
                print(f"{self.NameOfKnght} одержал победу спустя {i} дней(дня)")
            time.sleep(1)


first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

import time
import sys
from threading import Thread


class Elevator(Thread):
    def __init__(self, max_floor, select, move):
        super(Elevator, self).__init__()
        self.cur_floor = 8  # vị trí tầng hiện tại
        self.time = 2 # thời gian di chuyển giữa các tầng
        self.move = int(move) # 0: stop, -1: down, 1: up
        self.select_floor = int(select) # vị trí đến
        self.min_floor = 1
        self.max_floor = int(max_floor)

    def move_to(self, distance, over):
        for _ in range(distance):
            if over:
                if self.cur_floor ==  self.max_floor or self.cur_floor ==  self.min_floor:
                    self.move *= -1 # cách di chuyển hiện tại
            self.cur_floor += self.move
            time.sleep(self.time)
            print(' ---> {}'.format(self.cur_floor), end='')
            sys.stdout.flush()

    def call(self):
        if self.select_floor != self.cur_floor:
            from_fl = self.cur_floor
            distance = 0
            over = False
            print(self.cur_floor, end=' ')
            sys.stdout.flush()
            if self.move == 1  and self.select_floor > self.cur_floor:
                distance = self.select_floor - from_fl
            elif self.move == -1 and self.select_floor < self.cur_floor:
                distance = from_fl - self.select_floor
            elif self.move == 1 and self.select_floor < self.cur_floor:
                distance =  2*self.max_floor - self.cur_floor - self.select_floor
                over = True
            elif self.move == -1 and self.select_floor > self.cur_floor:
                distance =  self.cur_floor + self.select_floor - 2*self.min_floor
                over = True
            self.move_to(distance, over)

    def run(self):
        self.call()

def main():
    print("Enter the number of floor in building:")
    num_flr = input()
    print("Select floor:")
    select = input()
    print("Select way move:")
    move = input()
    elevator1 = Elevator(num_flr, select, move)
    elevator1.start()

if __name__ == '__main__':
    main()

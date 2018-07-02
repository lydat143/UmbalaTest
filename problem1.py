import time
import random
from threading import Thread


class Elevator(Thread):
    def __init__(self, name, max_floor, select, move):
        super(Elevator, self).__init__()
        self.name = 'elavator {}'.format(name)
        self.time = 2 # thời gian di chuyển giữa các tầng
        self.move = int(move) # 0: stop, -1: down, 1: up
        self.select_floor = int(select) # vị trí đến
        self.min_floor = 1
        self.max_floor = int(max_floor)
        cur_floor = random.randint(self.min_floor, self.max_floor)
        self.cur_floor = cur_floor  # vị trí tầng hiện tại

    def move_to(self, distance, over):
        for _ in range(distance):
            if over:
                if self.cur_floor ==  self.max_floor or self.cur_floor ==  self.min_floor:
                    self.move *= -1 # cách di chuyển hiện tại
            self.cur_floor += self.move
            time.sleep(self.time)
            print('{} ---> {}'.format(self.name, self.cur_floor))
        self.move = 0

    def call(self):
        if self.select_floor != self.cur_floor:
            from_fl = self.cur_floor
            distance = 0
            over = False
            print("{}: {}".format(self.name,self.cur_floor))
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
    print("Enter the number of elevator in building:")
    ela = input()
    request = ({'select': 2, 'way_move': 1}, {'select': 2, 'way_move': -1},
               {'select': 4, 'way_move': 1}, {'select': 4, 'way_move': 1},
               {'select': 3, 'way_move': -1},{'select': 9, 'way_move': -1},
               {'select': 9, 'way_move': 1},{'select': 3, 'way_move': 1},
               {'select': 4, 'way_move': -1},{'select': 8, 'way_move': -1},
               {'select': 5, 'way_move': 1})
    # print("Select floor:")
    # select = input()
    # print("Select way move:")
    # move = input()
    for i in range(int(ela)):
        req = random.randint(0, len(request))
        elevator = Elevator(i, num_flr, request[req]['select'], request[req]['way_move'])
        elevator.start()

if __name__ == '__main__':
    main()

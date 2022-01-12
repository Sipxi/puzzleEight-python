import time

# ? Is global needed?
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def printAllNodes(arr) -> None:
    for node in arr:
        print(node)


def index2d(myList, v) -> tuple:
    for i, x in enumerate(myList):
        if v in x:
            return i, x.index(v)


class Timer:
    def __init__(self) -> None:
        self.started_time = None

    def start(self) -> None:
        self.started_time = time.time()

    def time_convert(self, sec) -> str:
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        elapsed_time = "Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec)
        return elapsed_time

    def stop(self) -> str:
        end_time = time.time()
        time_lapsed = end_time - self.started_time
        elapsed_time = self.time_convert(time_lapsed)
        return elapsed_time

    def reset(self) -> None:
        self.started_time = None

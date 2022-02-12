from utils import index2d, goal_state



class Node:
    def __init__(self, state, depth=0, parent = None) -> None:
        self.state = state
        self.depth = depth
        self.h_value = self.findHDistance()
        self.total = self.depth + self.h_value
        self.parent = parent

    def __str__(self) -> str:
        return (
            f"state:{self.state}, depth:{self.depth}, h:{self.h_value}, f: {self.total}"
        )
    
    def getParent(self) -> object:
        return self.parent
        

    def getDepth(self) -> int:
        return self.depth

    def getTotal(self) -> int:
        return self.total

    def getState(self) -> list:
        return self.state

    #   Find the heuristics distance
    def findHDistance(self) -> int:
        h_value = 0
        for columb in self.state:
            for number in columb:
                if number != 0:
                    index_state = index2d(self.state, number)
                    index_goal = index2d(goal_state, number)
                    #   Calculating the distance beetwen index and goal_state
                    h_value += abs(index_state[0] - index_goal[0]) + abs(index_state[1] - index_goal[1])
        return h_value

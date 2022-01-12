import numpy as np
import copy


class PuzzleEightController:
    def getBorders(self, arr):
        array_2d = np.array(arr)
        left_border = array_2d[:, 0]
        top_border = array_2d[0, :]
        right_border = array_2d[:, -1]
        bottom_border = array_2d[-1, :]
        return left_border, top_border, right_border, bottom_border

    def getMoves(self, arr):
        moves = ["RIGHT", "LEFT", "UP", "DOWN"]
        left_border, top_border, right_border, bottom_border = self.getBorders(arr)
        if 0 in left_border:
            moves.remove("LEFT")
        if 0 in right_border:
            moves.remove("RIGHT")
        if 0 in top_border:
            moves.remove("UP")
        if 0 in bottom_border:
            moves.remove("DOWN")
        return moves

    def isSolvable(self):
        #   Copy arr because of rewriting
        arr = copy.deepcopy(self.given_state)
        #   Convert from 2D list to list
        arr = list(np.concatenate(arr).flat)
        arr.remove(0)
        #   Find inversions
        inversions = 0
        for i in range(len(arr)):
            for j in range(len(arr) - i):
                if arr[i] > arr[j + i]:
                    inversions += 1
        #   If inversions are odd the puzzle is solvable
        return True if inversions % 2 == 0 else False

import copy
from Node import Node
from utils import *
from rich import print
from PuzzleEightController import PuzzleEightController


class PuzzleEight:
    def __init__(self):
        self.given_state = [[8, 1, 6], [4, 3, 5], [7, 2, 0]]
        self.depth = 0
        self.nodes = [Node(self.given_state, self.depth)]
        self.old_nodes = []
        self.controller = PuzzleEightController()

    def chooseNode(self):
        #   Take first node from list
        chosen_node = self.nodes[0]
        #   Compare it
        for node in self.nodes:
            if node.getTotal() < chosen_node.getTotal():
                chosen_node = node
            # If f value is the same, compare h value
            elif node.getTotal() == chosen_node.getTotal():
                if node.findHDistance() < chosen_node.findHDistance():
                    chosen_node = node
        self.nodes.remove(chosen_node)
        self.old_nodes.append(chosen_node)
        print(f"[bold red]Chosen node: {chosen_node} ")
        return chosen_node

    def isVisited(self, given_node):
        #   Check if node was already visited
        for node in self.old_nodes:
            if node.getState() == given_node.getState():
                return True
        return False

    def matchMove(self, chosen_node):

        arr = chosen_node.getState()
        # Find the 0
        index = index2d(arr, 0)
        possible_moves = self.controller.getMoves(arr)
        # Depth is related to the node
        depth = chosen_node.getDepth() + 1

        if "LEFT" in possible_moves:
            # Copy to new arr due to rewriting
            new_arr = copy.deepcopy(arr)
            # Move the 0
            new_arr[index[0]][index[1]] = new_arr[index[0]][index[1] - 1]
            new_arr[index[0]][index[1] - 1] = 0

            node_to_apppend = Node(new_arr, depth, chosen_node)
            if not self.isVisited(node_to_apppend):
                self.nodes.append(node_to_apppend)
            possible_moves.remove("LEFT")

        if "RIGHT" in possible_moves:
            new_arr = copy.deepcopy(arr)
            new_arr[index[0]][index[1]] = new_arr[index[0]][index[1] + 1]
            new_arr[index[0]][index[1] + 1] = 0

            node_to_apppend = Node(new_arr, depth, chosen_node)
            if not self.isVisited(node_to_apppend):
                self.nodes.append(node_to_apppend)
            possible_moves.remove("RIGHT")

        if "UP" in possible_moves:
            new_arr = copy.deepcopy(arr)
            new_arr[index[0]][index[1]] = new_arr[index[0] - 1][index[1]]
            new_arr[index[0] - 1][index[1]] = 0

            node_to_apppend = Node(new_arr, depth, chosen_node)
            if not self.isVisited(node_to_apppend):
                self.nodes.append(node_to_apppend)
            possible_moves.remove("UP")

        if "DOWN" in possible_moves:
            new_arr = copy.deepcopy(arr)
            new_arr[index[0]][index[1]] = new_arr[index[0] + 1][index[1]]
            new_arr[index[0] + 1][index[1]] = 0

            node_to_apppend = Node(new_arr, depth, chosen_node)
            if not self.isVisited(node_to_apppend):
                self.nodes.append(node_to_apppend)
            possible_moves.remove("DOWN")

    def start(self, max_iterations=10000):
        #   Root node
        chosen_node = self.chooseNode()
        arr = chosen_node.getState()

        iterations = 0
        timer = Timer()
        timer.start()

        while arr != goal_state:
            iterations += 1
            self.matchMove(chosen_node)
            chosen_node = self.chooseNode()
            arr = chosen_node.getState()

            #   If iterations is set
            if iterations >= max_iterations:
                print(f"Iterations = {iterations}")
                print(timer.stop())
                break
        else:
            print(f"Iterations = {iterations}")
            print(timer.stop())
            print(f"Won {chosen_node}")
            self.printReverse(self.getAllParents(chosen_node))
    
    
    def getAllParents(self, node) -> list:
        all_parents = []
        all_parents.append(node)
        parent = node.getParent()
        while parent != None:
            all_parents.append(parent)
            parent = parent.getParent()
        return all_parents
    
    
    def printReverse(self, given_list) -> None:
        given_list.reverse()
        for i in range(len(given_list)):
                     
            print(f"{i}. {given_list[i]}")
            
        


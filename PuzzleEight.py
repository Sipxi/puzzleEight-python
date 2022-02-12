import copy

from numpy import intp
from Node import Node
from utils import *
from rich import print
from PuzzleEightController import PuzzleEightController
import sys
from TextGui import TextGui
class PuzzleEight:
    def __init__(self) -> None:
        self.given_state = None
        self.depth = 0
        self.nodes = None
        self.old_nodes = []
        self.controller = PuzzleEightController()

    def chooseNode(self) -> Node:
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

    def isVisited(self, given_node) -> bool:
        #   Check if node was already visited
        for node in self.old_nodes:
            if node.getState() == given_node.getState():
                return True
        #   If there is a same state = delete node
        for node in self.nodes:
            if node.getState() == given_node.getState():
                self.nodes.remove(node)
                return True
        return False

    def matchMove(self, chosen_node) -> None:
    
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
            
    def start(self, max_iterations = 10000):
        gui = TextGui()
        #   If answer is correct
        try:
            answer = gui.answer()
        except:
            print("Please, enter from number 0,1 or 2")
            return self.start(max_iterations)
        
        #   Match the answer
        if answer == 0:
            sys.exit()
            
        elif answer == 1:
            self.given_state = self.controller.generateRandomPool()
            gui.clearScreen()
            print("[bold yellow] Your pool is")
            print(self.given_state)
            time.sleep(3)
            
        elif answer == 2:
            #   If user input is wrong
            try:
               self.given_state = gui.enterPool()
            except:
                print("Please, enter solvable combination")
                time.sleep(1)
                return self.start(max_iterations)
            
            #   If combination is unsolvable
            if not self.controller.isSolvable(self.given_state):
                print("Please, enter solvable combination")
                time.sleep(1)
                return self.start(max_iterations)
        #   If user input is not
        else:
            print("Please, enter from number 0,1 or 2")
            time.sleep(1)
            return self.start(max_iterations)
        
        #   First node
        self.nodes = [Node(self.given_state, self.depth)]
        self.solve(max_iterations)
        
    def solve(self, max_iterations) -> None:
            
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
            
        input("Press enter to continue...")
        self.flush()
        return self.start(max_iterations)
    
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
    
    def flush(self):
        #   Set default values
        self.given_state = None
        self.depth = 0
        self.nodes = None
        self.old_nodes = []
        
        


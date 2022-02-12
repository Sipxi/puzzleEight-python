from rich import print

class TextGui():

    def clearScreen(self) -> None:
        for i in range(20):
            print()
    def answer(self) -> int:
        self.clearScreen()
        print("Welcome to the puzzle eight solver! \nMade by Serhij Čepil for school purposes. \nSolved with A* Algorithm \n")
        print("[bold red] How do you want to start?\n")
        print("0. Exit")
        print("1. Generate a random pool")
        print("2. Enter a  pool")
        move = int(input("Your answer is: "))
        return move
    
    def enterPool(self) -> list:
        numbers =[1,2,3,4,5,6,7,8,0] 
        listToGo = []
        for i in range(3):
            listToGo.append([])
            for j in range(3):
                self.clearScreen()
                print("Your pool is: ")
                print(listToGo)
                print("Enter a pool: \n")
                print("[bold red] You can choose from numbers: \n")
                print(numbers)
                numberToAdd = int(input("Enter a number: "))
                listToGo[i].append(numberToAdd)
                numbers.remove(numberToAdd)
        return listToGo
                    
        
            
        

    
                
            



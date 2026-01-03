#Tisulm's first project
#A PYTHON-PROGRAMMED SIMPLE TASK MANAGER

import json
import time
from colorama import Fore, Style, init
import os

#Set-up
    #Defining a "clear terminal" function
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    #Running a script for colorama
init()
    #Ensuring that the json file saving tasks is always created next to the python program
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "tasks.json")

#Task retrieval
try:
    with open(DATA_FILE, "r") as tasks:
        task_list = json.load(tasks)
    a = 1
except (FileNotFoundError, json.JSONDecodeError):
    with open(DATA_FILE, "w") as tasks:
        json.dump([], tasks)
    task_list = []
    a = 0


#Adding a task
def addtask():
    clear()
    add = input("What task do you wish to add? \n>>> ").strip()
    task_list.append(add.title())
    print(Fore.MAGENTA + add.title() + Fore.YELLOW + " has been " + Fore.CYAN + "added" + Fore.YELLOW + " to tasks!" + Style.RESET_ALL)
    time.sleep(2.5)
    clear()

#Completing a task
def completetask():
    clear()
    remove = input("What task do you wish to " + Fore.GREEN + "complete" + Style.RESET_ALL + "? \n>>> ").strip().title()
    index = task_list.index(remove)
    task_list.pop(index)
    print(Fore.MAGENTA + remove.title() + Fore.YELLOW + " task has been " + Fore.GREEN + "completed" + Fore.YELLOW + "!" + Style.RESET_ALL)
    time.sleep(2.5)
    clear()

#Viewing tasks
def viewtask():
    clear()
    for task in task_list:
        print("> " + task)
    if task_list == []:
        print(Fore.YELLOW + "No tasks were found!" + Style.RESET_ALL)
    option = input(Fore.LIGHTGREEN_EX + "To go back to main menu, enter any character! " + Style.RESET_ALL + "\n>>> ")
    if option != "":
        clear()
        time.sleep(1)
    else:
        clear()
        time.sleep(1)


#The Program
def main():
    while True:
        #First-time introduction script
        global a
        if a == 0:
            time.sleep(2)
            print(Style.BRIGHT + "This is a task manager. Use this application to manage your daily and weekly tasks:" + Style.RESET_ALL)
            time.sleep(1.5)
            print("\n ." + Fore.CYAN + "add" + Style.RESET_ALL +" tasks")
            time.sleep(1.5)
            print("\n  .." + Fore.GREEN + "complete" + Style.RESET_ALL + " tasks")
            time.sleep(1.5)
            print("\n   ...and follow along your progress by viewing all your tasks!")
            time.sleep(2.5)
            print("Moreover, all your tasks are saved each time your operate this program, so please come back often.")
            time.sleep(4.5)
            clear()
        #MENU
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Exit program")
        #Instruction script
        if a == 0:
            time.sleep(1.5)
            print("INSTRUCTIONS: Type in the number of your desired action, press enter, and manage your tasks!")
        path = input(">>> ").strip()
        if path == "1" or path == "1.":
            addtask()
        elif path == "2" or path == "2.":
            viewtask()
        elif path == "3" or path == "3.":
            completetask()
        #Ending the program
        elif path == "4" or path == "4.":
            print(Fore.RED + "Exiting program..." + Style.RESET_ALL)
            break
        else:
            print(Style.DIM + "Please enter the number of your desired action." + Style.RESET_ALL)
        a += 1


#Program execution
if __name__ == "__main__":
    main()

#Saving the tasks
with open(DATA_FILE, "w") as tasks:
    json.dump(task_list, tasks, indent= 4)

import random
from datetime import *  
from operator import * 

class Agent():
    def __init__(self, agent_name, is_available, available_since, role):
        self.agent_name = agent_name
        self.is_available = is_available
        self.available_since = available_since
        self.role = role


def form_complete(length):
    for i in range(0,length):    
        agent_name = input("Enter name: ")
        a = input("Are you available(True or False): ")
        if a == "True" or a == "Yes" :
            is_available = True
        elif a == "False" or a == "No":
            is_available = False
        else:
            is_available = True
        available_since = int(input("How many seconds ago: "))
        role = input("Agent's role: ") 
        
        obj = Agent(agent_name, is_available, available_since, role)
        roles.append(obj.role)
        a = obj.agent_name
        b = obj.is_available
        c = obj.available_since
        d = obj.role
        orig_list.append([a,b,c,d])

if __name__ == '__main__':
    orig_list = []
    roles = []
    n = int(input("Enter number of agents : ")) 
    
form_complete(n)
agent_list = orig_list.copy()
print(agent_list)
print(roles)

def agent_selector(agent_list,agent_selection_mode):   
    pass

print("1. All Available mode")
print("2. Least busy mode")
print("3. Random mode")
print("4. Exit")

agent_selection_mode = int(input("Choose your mode(type 1 or 2 or 3): "))


if(agent_selection_mode == 1):
    avail_list = []
    for i in range(len(agent_list)):
        for j in range(len(agent_list[i])):
            if agent_list[i][1] == True:
                avail_list.append(i)
    print(avail_list)

if(agent_selection_mode == 2):
    for i in range(len(agent_list)):
        for j in range(len(agent_list[i])):
            if agent_list[i][1] == False:
                agent_list.remove(i)
    agent_list.sort(key=itemgetter(2), reverse=True)
    print(agent_list)
        
if(agent_selection_mode == 3):
    for i in range(len(agent_list)):
        for j in range(len(agent_list[i])):
            if agent_list[i][1] == False:
                agent_list.remove(i)        
    print("Random agent from list is: ", random.choice(agent_list))
    
if(agent_selection_mode == 4):
    print("Exit , THANK YOU")
    
#Imports
import time
import random
from statistics import mean

#Define global variables
totalQuestionsAsked = 0
totalRandNums = []
totalPos = []

simulations = 100000

#Run a single simulation
def SingleSim():
    #Define global variables
    global totalQuestionsAsked
    
    #Define local variables
    pos = 5

    randNumList = []
    posList = [5]

    #Set the positions chance rates
    posChances = {5:8, 4:6, 3:4, 2:2}

    #Continuous loop until pos == 1
    while pos != 1:
        #Generate random number
        randNum = random.randint(1, 10)

        #Update position
        if randNum <= posChances[pos]: pos -= 1
        else: pos = 5

        #Update local variables
        randNumList.append(randNum)
        posList.append(pos)
        totalQuestionsAsked += 1

    #Update endresults
    totalRandNums.append(mean(randNumList))
    totalPos.append(mean(posList))

#Print all endresults
def PrintEverything():
    print("Average Questions Asked:", totalQuestionsAsked / simulations)
    print("Average Random Numbers Generated:", mean(totalRandNums))
    print("Average Positions:", mean(totalPos))
    print("Executed:", simulations, "times")

def main():
    #Find starttime of the program
    start = time.time()

    #Run the sim x amount of times
    for _ in range(simulations):
        SingleSim()
    
    #Find the endtime of the program
    end = time.time()
    
    #Print Endresults
    PrintEverything()

    #Print the execution time of the program
    print("Simulation Time:", end - start, "seconds")

#Notation
if __name__ == "__main__":
    main()

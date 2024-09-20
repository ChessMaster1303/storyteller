#Know the dead ends in the story, and hence know when to call ChatGPT
from dead_end_finder import find_dead_ends
dead_ends = find_dead_ends()

#For aesthetic terminal-line horizontal rule
import os
term_size = os.get_terminal_size()


#Opening story with the plot
import json
story_data = json.load(open('story_data.json'))
print(story_data["plot"])
print('=' * term_size.columns)


#Checking whether a user's input is valid
def checkValidChoice(userChoice, choiceCounter):
    if(type(userChoice) is int):
        if(userChoice <= choiceCounter + 1):
            return True
    else:
        return False


#Prints a new scene
def newScenePrint(scene_description, choices):
    print(scene_description)
    choiceCounter = 0
    for choice in choices:
        print(str(choiceCounter + 1) + ": " + str(choice["text"]))
        choiceCounter += 1

    userChoice = int(input("What option do you choose? *USER INPUT: "))
    validity = checkValidChoice(userChoice, choiceCounter)

    if(validity == True):
        newSceneKey = choices[userChoice - 1]["scene_key"]
        #print("New Scene Key: " + str(choices[userChoice - 1]["scene_key"]))
        
        if(newSceneKey in dead_ends):
            print('=' * term_size.columns)
            print("We don't have scene data for scene key: " + str(newSceneKey))
            print("This is the place where we shall put ChatGPT stuff")
            input("Press ENTER to exit the program")
        else:
            print('=' * term_size.columns)
            newSceneDescription = story_data["scenes"][newSceneKey]["text"]
            newSceneChoices = story_data["scenes"][newSceneKey]["choices"]
            newScenePrint(newSceneDescription, newSceneChoices)
    else:
        while(validity == False):
           userChoice = int(input("Please input a valid number."))
           validity = checkValidChoice(userChoice, choiceCounter)


def playGame():
    #Start with the "start" scene
    newScenePrint(story_data["scenes"]["start"]["text"], story_data["scenes"]["start"]["choices"])

playGame()
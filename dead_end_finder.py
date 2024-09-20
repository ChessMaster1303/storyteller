#This file just contains a function to be used in the main storyteller.py app
#This function is used to determine, according to our current story_data.json, which scenes (dead ends) would require ChatGPT to generate new scene info
def find_dead_ends():
    import json
    story_data = json.load(open('story_data.json'))


    #Find every scene that is referenced
    referenced_story_scene_keys = []
    for scene in story_data["scenes"]:
        choices = story_data["scenes"][scene]["choices"]
        for choice in choices:
            if (not choice["scene_key"] in referenced_story_scene_keys):
                referenced_story_scene_keys.append(choice["scene_key"])
    #print("All referenced story keys: " + str(referenced_story_scene_keys))


    #Find every scene that is defined properly
    valid_story_scene_keys = []
    for scene in story_data["scenes"]:
        valid_story_scene_keys.append(scene)
    #print("All valid story keys: " + str(valid_story_scene_keys))


    #Find the dead ends (scenes that are referenced but not defined properly)
    dead_ends = []
    for scene in referenced_story_scene_keys:
        if(not scene in valid_story_scene_keys):
            dead_ends.append(scene)
    return dead_ends
    #print("Dead-ends: " + str(dead_ends))


    #Keeps the command line open until user wishes to close it
    #input("--------------------------------------\nPress 'Enter' to Exit")
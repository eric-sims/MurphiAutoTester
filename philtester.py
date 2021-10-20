import os
import sys
import subprocess
import datetime

############################################
# IF THERE ARE ANY EDITS TO THE MURPI FILE, 
# MAKE SURE THESE NUMBERS CORRESPOND TO THE 
# BLOCK COMMENT MARKERS OF THE SCENARIOS
############################################ 
how_many_philosiphers = range(3, 9, 3) # Test just 3 philosiphers
how_many_scenarios = range(1, 4)    # Test scenarios 1 through 3
_MAX_PHIL_LINE_ = 14 -1
_FIRST_SCENE_START_ = 26 -1 
_FIRST_SCENE_END_ = 60 -1
_SECOND_SCENE_START_ = 61 -1
_SECOND_SCENE_END_ = 87 -1
_THIRD_SCENE_START_ = 88 -1
_THIRD_SCENE_END_ = 113 -1



############################################ 
################# FUNCTIONS ################q
def compileMurphi():
    print('\t\tCompiling murphi file.....', end='')
    p1 = subprocess.run(['../../src/mu', 'phil.m'], capture_output=True, check=True)
    print('Success!')
    print('\t\tCompiling C program into executable......', end='')  
    p2 = subprocess.run(['make', 'phil'], capture_output=True, check=True)

    print('Success!')

def changeScenLines(m, num_scene):
    m[_FIRST_SCENE_START_] = " /* \n"
    m[_FIRST_SCENE_END_] = " */ \n"
    m[_SECOND_SCENE_START_] = " /* \n"
    m[_SECOND_SCENE_END_] = " */ \n"
    m[_THIRD_SCENE_START_] = " /* \n"
    m[_THIRD_SCENE_END_] = " */ \n"
    
    if num_scene == 1:
        m[_FIRST_SCENE_START_] = " -- THIS IS THE SCENARIO BEING TESTED [START] \n"
        m[_FIRST_SCENE_END_] = " -- THIS IS THE SCENARIO BEING TESTED [END] \n"
    elif num_scene == 2:
        m[_SECOND_SCENE_START_] = " -- THIS IS THE SCENARIO BEING TESTED [START] \n"
        m[_SECOND_SCENE_END_] = " -- THIS IS THE SCENARIO BEING TESTED [END] \n"
    elif num_scene == 3:
        m[_THIRD_SCENE_START_] = " -- THIS IS THE SCENARIO BEING TESTED [START] \n"
        m[_THIRD_SCENE_END_] = " -- THIS IS THE SCENARIO BEING TESTED [END] \n"


def changePhilForkLines(m, num_phil):
    m[_MAX_PHIL_LINE_] = "\t MAX_PHIL: " + str(num_phil) + ";\n"


test_result_file = "test" + str(datetime.datetime.now()) + ".txt"

if True:
    for phil in how_many_philosiphers:
        print("TESTING " + str(phil) + " PHILOSIPHER(S)")
        for scen in how_many_scenarios:
            print("\tTESTING SCENARIO " + str(scen))

            # Uncomment the scenario of phil 
            with open('phil.m', 'r') as f:
                mflines = f.readlines()

            changeScenLines(mflines, scen)
            changePhilForkLines(mflines, phil)
            new_phil_m = "".join(mflines)

            with open('phil.m', 'w') as f:
                f.write(new_phil_m)

            # Compile the murphi file
            compileMurphi()

            # Run the model checker for DFS and BFS 
            output_dfs = subprocess.run(['./phil', '-vdfs'], stdout=subprocess.PIPE).stdout.decode('utf-8')
            output_bfs = subprocess.run(['./phil', '-vbfs'], stdout=subprocess.PIPE).stdout.decode('utf-8')
            output_dfs = output_dfs.split('\n')
            output_bfs = output_bfs.split('\n')

            with open(test_result_file, 'a') as f:
                i = 46 # This is the part of the output that I care about right now
                f.write("SCENARIO " + str(scen) + " | " + str(phil) + " PHILOSIPHERS | DFS\n")
                while i < 53:
                    if output_dfs[i].strip() != "":
                        f.write(output_dfs[i].strip() + " ")
                    i += 1
                f.write("\n")

                i = 46 # This is the part of the output that I care about right now
                f.write("SCENARIO " + str(scen) + " | " + str(phil) + " PHILOSIPHERS | BFS\n")
                while i < 53:
                    if output_bfs[i].strip() != "":
                        f.write(output_bfs[i].strip() + " ")
                    i += 1
                f.write("\n\n\n")


        print("\n\n")




    
    # Print out the results
    print("------------------TEST RESULTS:---------------------")
    with open(test_result_file, "r") as f:
        print(f.read())

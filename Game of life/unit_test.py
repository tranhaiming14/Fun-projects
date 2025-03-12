from game_of_life import next_state
import os

# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = next_state(init_state1)

    if expected_next_state1 == actual_next_state1:
        print("PASSED 1")
    '''else:
        print "FAILED 1!"
        print "Expected:"
        print expected_next_state1
        print "Actual:"
        print actual_next_state1
    '''
    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = next_state(init_state2)

    if expected_next_state2 == actual_next_state2:
        print ("PASSED 2")
    else:
        print("FAILED 2!")
        print("Expected:")
        print(expected_next_state2)
        print("Actual:")
        print(actual_next_state2)
print(os.name)
#!/usr/bin/env python3

import rospy 
from service.srv import addTwoInts, addTwoIntsResponse
#from std_srvs import SetBool 

def handle_add_two_ints(req):
    """
    Service handler.
    Calculates the sum of 2 inputs. 
    If the result has 1 digit, print the result and return True.
    If the result has 2 digits, print the result and return False. 
    """
    result = req.a + req.b
    success = False 
    print(f"Sum of {req.a} and {req.b} is: {(result)}")

    #if the result has 2 digits, print the result and return False.
    if (result) <= 9:
        success = True 
    return addTwoIntsResponse(result, success)

def add_two_ints_server():
    rospy.init_node("add_two_ints_server")
    s = rospy.Service("add_two_ints", addTwoInts, handle_add_two_ints)
    rospy.loginfo("Ready to add two digits.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
    

#!/usr/bin/env python3

import rospy 
from service.srv import addTwoInts, addTwoIntsResponse

def handle_add_two_ints(req):
    result = req.a + req.b 
    print(f"Sum of {req.a} and {req.b} is: {(result)}")

    if (result) <= 9:
        return addTwoIntsResponse(result)
    else:
        return False
    

def add_two_ints_server():
    rospy.init_node("add_two_ints_server")
    s = rospy.Service("add_two_ints", addTwoInts, handle_add_two_ints)
    rospy.loginfo("Ready to add two digits.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
    

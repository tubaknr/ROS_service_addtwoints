#!/usr/bin/env python3

import rospy 
import sys
from service.srv import addTwoInts

#type of service = addTwoInts

def client(a, b):
    rospy.wait_for_service("add_two_ints")

    try:
        #handle for calling the service
        add_two_ints = rospy.ServiceProxy("add_two_ints", addTwoInts) # handle = add_two_ints 
        response = add_two_ints(a, b) # call handle like a normal fcn.
        return response 
    except rospy.ServiceException as e:
        print(f"Service call failed : {e}")


def usage():
    return f"{sys.argv[0]} [a b]"


if __name__ == "__main__":
    rospy.init_node("client")
    
    if len(sys.argv) == 3: 
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)

    print(f"Requesting {a} + {b}")
    print(f"{a} + {b} = {client(a, b)}")

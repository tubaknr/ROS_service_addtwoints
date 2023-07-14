# ROS_service_addtwoints
Returns the sum of inputs (which are a and b, typed on the terminal by the user) if the sum is a single-digit number. If the sum is two-digit or bigger, retunes 0 (as False).

## To run:
in one terminal (service is my package's name, type whatever your package's name is):
```
rosrun service server.py
```
keep running.

in another terminal: 
```
rosservice call /add_two_ints "a: 0 b: 0"
```

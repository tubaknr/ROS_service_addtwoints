# ROS_service_addtwoints

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

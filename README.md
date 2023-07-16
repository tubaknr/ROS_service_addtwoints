# ROS_service_addtwoints
Returns the sum of inputs (a and b, typed on the terminal by the user). If the sum is a single-digit number, print the result and return True. If the result has 2 digits, return False and prin the result.

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
![1111](https://github.com/tubaknr/ROS_service_addtwoints/assets/97946563/b97cf53e-4de6-4940-9ea9-1d85bf5dddcc)

![222](https://github.com/tubaknr/ROS_service_addtwoints/assets/97946563/ca1fedf5-c706-4866-8276-712410762ff6)


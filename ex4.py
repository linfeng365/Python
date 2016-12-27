# -*- coding:utf-8 -*-
cars = 100 #把 100 赋值给变量 cars
space_in_a_car = 4.0
drives = 30 
passengers = 90
cars_not_driven = cars - drives
cars_driven = drives
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are",cars,"cars available."
print "There are only",drives,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport", carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."
print "Hey %s there."%"you"
print "We have %s to carpool today."% passengers # 把 %s 替换为 passengers;

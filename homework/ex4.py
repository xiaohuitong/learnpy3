# -*- coding: utf-8


# 把数值100赋给变量cars
cars = 100
# 把数值4.0赋给变量space_in_a_car
space_in_a_car = 4.0
# 把数值30赋给变量drivers
drivers = 30
# 把数值90赋给变量passengers
passengers = 90
# 计算有多少车不能被使用
cars_not_driven = cars - drivers
# 有多少司机就有多少车
cars_driven = drivers
# 计算所有能驾驶的车总共有多少座位
carpool_capacity = cars_driven * space_in_a_car
# 计算平均每辆车可以载几个乘客
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# 下面这个错误信息说明：在第八行程序出现了问题，错误类型是命名错误，
#变量名'car_pool_capacity' 没有被定义就被使用了。

#Traceback (most recent call last):
#File "ex4.py", line 8, in <module>
#average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined

# 用 4.0作为 space_in_a_car 的值有必要，因为如果乘客过多，
# 一辆车就必须比额定载客量多载乘客。
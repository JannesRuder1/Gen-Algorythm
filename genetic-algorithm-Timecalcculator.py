processing_times = [10, 20, 30, 40, 50, 60]  # example processing times
travel_time = 5  # example travel time

output = [3, 6, 1, 6, 1, 6]  # task sequence
robot_assignment = [1, 1, 1, 2, 2, 1]  # robot assignment for each task

total_time_robot1 = 0
total_time_robot2 = 0

for i in range(len(output)):
    station = output[i]
    robot = robot_assignment[i]
    if robot == 1:
        total_time_robot1 += processing_times[station - 1]  # subtract 1 because station indices start at 1
        if i < len(output) - 1 and robot_assignment[i + 1] == 1:
            total_time_robot1 += travel_time  # add travel time if not at the last station and next task is also for robot 1
    else:
        total_time_robot2 += processing_times[station - 1]  # subtract 1 because station indices start at 1
        if i < len(output) - 1 and robot_assignment[i + 1] == 2:
            total_time_robot2 += travel_time  # add travel time if not at the last station and next task is also for robot 2

print("Total time Robot 1:", total_time_robot1)
print("Total time Robot 2:", total_time_robot2)
print("toatl time bothe:", (total_time_robot1 + total_time_robot2) )
"""
Given two arrays:
start_time = [0:00, 1:00, 7:00, 2:00,2:30]
end_time = [6:00, 3:00, 8:00, 9:30, 5:30]

find the minimum number of processors 'n' required to execute the task such that tasks are executed as soon as they come
"""


start_time = ['0:00', '1:00', '3:20', '2:00', '2:30', '7:00']
end_time = ['6:00', '3:00', '8:00', '9:30', '5:30', '9:00']
n = len(start_time)


if n == 1:
    print(1)


task_timing = list(zip(start_time, end_time))
task_timing.sort(key=lambda x: x[-1])
print(task_timing)
processors = 1
prev_task_no = 0
prev_start_time = task_timing[prev_task_no][0]
prev_end_time = task_timing[prev_task_no][1]


cur = 1
while cur < n:
    if task_timing[cur][0] < prev_end_time:
        processors += 1

    elif task_timing[cur][0] > prev_end_time:
        prev_task_no += 1
        prev_start_time = task_timing[prev_task_no][0]

        prev_end_time = task_timing[prev_task_no][1]

    cur += 1


print(processors)

[('0:00', '6:00'), ('1:00', '3:00'), ('2:00', '9:30'),
 ('2:30', '5:30'), ('3:20', '8:00'), ('7:00', '9:00')]

5

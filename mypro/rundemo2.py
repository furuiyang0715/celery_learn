from mypro.tasks import *

r1 = my_add.delay(10, 20)
print(r1.task_id)

# 在运行时改变 my_add 任务的运行队列
r3 = my_add.apply_async(args=(10, 20), queue='queue2')
print(r3.task_id)

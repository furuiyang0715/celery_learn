from mypro import app as celery_app


# 创建任务函数
@celery_app.task
def my_task1():
    print("任务函数(my_task1)正在执行.")
    return "task1 done"


@celery_app.task
def my_task2():
    print("任务函数(my_task2)正在执行.")
    return "task2 done"


@celery_app.task
def my_task3():
    print("任务函数(my_task3)正在执行.")
    return 'task3 done'


@celery_app.task
def my_add(m, n):
    return m + n


@celery_app.task
def my_sub(m, n):
    return m - n


@celery_app.task
def my_mul(m, n):
    return m * n


'''开启 worker 服务器
在 celery_learn 目录下执行: 
celery -A mypro worker -l info 
'''

'''调用任务的方式: 
(1) 如果我们直接执行任务函数，将会直接执行此函数在当前进程中，并不会向broker发送任何消息 

(2) 调用任务，可使用 delay() 方法: my_task.delay(2, 2)
也可以使用 apply_async() 方法，该方法可让我们设置一些任务执行的参数，例如，任务多久之后才执行，任务被发送到那个队列中等等.

my_task.apply_async((2, 2), queue='default', countdown=10)

任务 my_task 将会被发送到 my_queue 队列中，并且在发送 10 秒之后执行。
无论是 delay() 还是 apply_async() 方式都会返回 AsyncResult 对象，方便跟踪任务执行状态，但需要我们配置r esult_backend.
每一个被调用的任务都会被分配一个 ID，我们叫 Task ID.


'''
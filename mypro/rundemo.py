import time
import celery
from mypro.tasks import *
from celery import signature, group, chain

# # 使用 delay 进行调用
# ret = my_add.delay(1, 2)
# print(ret.status)
# time.sleep(1)
# print(ret.status)
# print(ret.result)
#
# print("* " * 20)
#
# # 封装为 signature 再调用
# print(type(my_add))
# my_add = signature(my_add, args=(2, 2), countdown=5)
# print(type(my_add))
# ret1 = my_add.delay()
# print(ret1.status)
# time.sleep(6)
# print(ret1.status)
# print(ret1.result)

# 测试 Primitives 的调用
# 测试 group 的调用
m = 20
n = 10

# 将 m+n 和 m*n 同时调用:
my_group = group(
    signature(my_add, args=(m, n)),
    signature(my_mul, args=(m, n)),
)

print(type(my_group))
# my_group 本身即是 signature 对象
print(isinstance(my_group, celery.canvas.Signature))  # True
ret2 = my_group()
print(ret2.get())    # [30, 200]

# 测试 chain 的使用
s1 = signature(my_add, args=(m, n))
# s2 的第一个参数是 s1 的运行结果
s2 = signature(my_mul, args=(10, ))
# s3 的第一个参数是 s2 的运行结果
s3 = signature(my_add, args=(700, ))
my_chain = chain(s1, s2, s3)
print(type(my_chain))
ret3 = my_chain()  # 执行任务链
print(ret3)
print(ret3.get())  # 输出最终结果

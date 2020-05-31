"""sunprocess模块仅用于linux下,主要用于shell命令下发;
   subprocess 模块允许我们启动一个新进程，并连接到它们的输入/输出/错误管道，从而获取返回值。
"""
import subprocess,time


def run(time):
    proc = subprocess.Popen(['sleep',str(time)])
    return proc


procs = []
start = time.time()
for _ in range(10):
    procs.append(run(0.1))

for proc in procs:
    # 和子进程交互，发送和读取数据
    proc.communicate()
end = time.time()

print('用时：', end-start) # 0.12s

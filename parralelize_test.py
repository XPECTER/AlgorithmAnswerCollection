import multiprocessing.pool
import time
import os
import multiprocessing as mp

# python 2.6부터 multiprocessing lib은 builtin 되었다.

def work_fuc(x):
    print("value %s is in PID : %s" % (x, os.getpid()))
    time.sleep(1)
    return x**5

def main():
    start = int(time.time())
    #num_cores = 4
    num_cores = mp.cpu_count()
    pool = multiprocessing.pool.Pool(num_cores)
    print(pool.map(work_fuc, range(1,17)))
    print("***run time(sec) : ", int(time.time()) - start)

if __name__ == "__main__":
    main()


# multiprocessing lib
# Pool, Process 의 차이
# Pool은 하나의 작업을 여러 일꾼들이 나눠서 작업하는 것이고
# Process는 한 일꾼마다 다른 작업을 분배할 수 있다.
# Pool은 close()로 작업 완료후 메모리를 낭비하는 것을 잡기위해 사용하고 join()기다린다.
# Pool은 close()와 join()을 달고 다니고,
# Process는 start()와 join()을 달고 다닌다.
# Process는 start()를 해줘야 하고 join()으로 마치길 기다린다.

# threading, thread 모듈 2가지가 있으니 thread모듈은
# deprecated(중요도가 떨어져 안쓰이는 기능, 곧 사라질 기능)되어 threading을 권장한다.

# thread 도 있지만 동기화의 문제가 뒤따른다.
# mutex, semafhore, critical section
# deadlock 문제

# bisect 를 찾아보자
#import thread
# 분할 상환 방식


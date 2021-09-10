# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import datetime
import time



""""""  
def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))
  
def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))


def timer1():
    while 1==1:
        currentTime = str(datetime.datetime.now())
        print(f'Timer 1: {currentTime}')
        time.sleep(1.2)

def timer2():
    while 1==1:
        currentTime = str(datetime.datetime.now())
        print(f'Timer 2: {currentTime}')
        time.sleep(1)

t1 = threading.Thread(target=timer1)
t2 = threading.Thread(target=timer2)

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

"""
#if __name__ == "__main__":
# creating thread
t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

# both threads completely executed
print("Done!")
"""


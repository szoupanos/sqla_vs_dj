import click


@click.command()
def cmd():
    """
    Multi-threading code to see if updating the same JSON by multiple threads
    causes concurrency problems.

    Inspired by:
    https://www.tutorialspoint.com/python/python_multithreading.htm

    Needs work - incomplete
    """
    import threading
    import time

    exitFlag = 0

    class myThread (threading.Thread):
       def __init__(self, threadID, name, counter):
          threading.Thread.__init__(self)
          self.threadID = threadID
          self.name = name
          self.counter = counter
       def run(self):
          print "Starting " + self.name
          print_time(self.name, 5, self.counter)
          print "Exiting " + self.name

    def print_time(threadName, counter, delay):
       while counter:
          if exitFlag:
             threadName.exit()
          time.sleep(delay)
          print "%s: %s" % (threadName, time.ctime(time.time()))
          counter -= 1

    # Create new threads
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # Start new Threads
    thread1.start()
    thread2.start()

print "Exiting Main Thread"


if __name__ == '__main__':
    import sys
    import os

    dir_of_curr_file = os.path.dirname(os.path.realpath(__file__))
    # project folder
    par_dir = os.path.dirname(dir_of_curr_file)
    proect_dir = os.path.dirname(par_dir)
    # adding the project folder to the path
    sys.path.append(proect_dir)

    # calling the command
    cmd()

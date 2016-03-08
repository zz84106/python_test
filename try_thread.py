import argparse
import os
import sys
import threading
#import thread
import time

from os import listdir, makedirs
from os.path import isdir, dirname
from shutil import copy2

overall_count = 0

def worker(processName):
  while True:
    time.sleep(2)
    print("{} report at {}".format(processName, time.ctime(time.time())))

def run_thread_1():
  try:
    for idx in range(1, 12):
      id = "process_{}".format(idx)
      t = threading.Thread(target=worker, args=(id))
      t.start()
  except:
    print("failed_to generate thread")

  print("end run_thread_1()")

class newThread (threading.Thread):
  def __init__(self, threadID, name, counter):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.counter = counter

  def run(self):
    global overall_count
    while self.counter > 0:
      self.counter -= 1
      print("thread {}: {} running".format(self.threadID, self.name))
      overall_count += 1
      
def run():
  global overall_count
  print("==current threads: {}".format(threading.active_count()))
  print("==current threads id: {}".format(threading.get_ident()))

  #run_thread_1()
  
  all_threads = []
  try:
    for idx in range(1, 12):
      name = "process_{}".format(idx)
      one_thread = newThread(idx, name, 5) 
      one_thread.start()
      all_threads.append(one_thread)
      
  except:
    print("failed to generate thread")

  while all_threads:
    for t in all_threads:
      if not t.is_alive():
        all_threads.remove(t)
    print("==active thread count: {}".format(threading.active_count()))

  print("overall_count: {}".format(overall_count))
  
if __name__ == "__main__":
  run()

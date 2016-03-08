import argparse
import os
import sys

from os import listdir, makedirs
from os.path import isdir, dirname
from shutil import copy2

def genlistdir(path):
  for item in listdir(path):
    yield item

def genRecursiveListDir(path):
  for item_name in genlistdir(path):
    item = "{p}/{f}".format(p=path, f=item_name)
    if isdir(item):
      for full_name in genRecursiveListDir(item):
        yield full_name
    else:
      yield item

def getDestNameFromSrcName(src_path, dest_path, full_name):
  return dest_path + full_name[len(src_path):]
  
def copyFile(src, dest):
  dest_path = dirname(dest)
  if not isdir(dest_path):
    makedirs(dest_path)
  copy2(src, dest)
  print("==<<copied, from: {}".format(src))
  print("==>>copied, to: {}".format(dest))

def find_diff(src_path, dest_path, action='diff'):
  item_count = 0
  diff_item_count = 0
  diff_item_size = 0
  missing_items = []
  for full_name in genRecursiveListDir(src_path):
    item_count += 1
    dest_name = getDestNameFromSrcName(src_path, dest_path, full_name)
    if not os.path.isfile(dest_name):
      diff_item_count += 1
      diff_item_size += os.path.getsize(full_name)
      missing_items.append(full_name)
      if action == 'copy':
        copyFile(full_name, dest_name)
      elif action == 'diff':
        print(full_name)

  print("total files under {}: {:,}".format(src_path, item_count))
  print("total files not under {}: {:,}".format(dest_path, diff_item_count))
  print("total missing file size {:,}".format(diff_item_size))
  
def run():
  print("os: {}".format(os.name))
  print("cwd: {}".format(os.getcwd()))
  #print(os.environ)
  print("----------------------------")

  parser = argparse.ArgumentParser()
  parser.add_argument(
    "-s",
    "--source",
    help="the source directory"
  ) 
  parser.add_argument(
    "-d",
    "--destination",
    help="the destination directory"
  ) 
  parser.add_argument(
    "-a",
    "--action",
    choices=['copy', 'diff'],
    help="whether to copy files or just print src -> dest difference"
  ) 
  args = parser.parse_args()
  print(args)
  
  find_diff(args.source, args.destination, args.action)

if __name__ == "__main__":
  run()

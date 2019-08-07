import os
import time

class FileWatcher:
    def __init__(self, path_of_file_to_watch):
        self.path_of_file_to_watch = path_of_file_to_watch
        self.subscribers = set()
        self.fileSize = os.stat(self.path_of_file_to_watch).st_size

    def register(self, subscriber):
        self.subscribers.add(subscriber)

    def unregister(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def poll(self):
        while True:
            newFileSize = os.stat(self.path_of_file_to_watch).st_size
            print(f'New size: {newFileSize}; old size: {self.fileSize}')                
            if newFileSize != self.fileSize:
                self.fileSize = newFileSize
                for subscriber in self.subscribers:
                    subscriber.update(newFileSize)

            time.sleep(5.0)
                    
class FileObserver:
    def __init__(self, name):
        self.name = name

    def update(self, fileSize):
        print(f'{self.name} noticed that the file is now {fileSize} bytes')

bob = FileObserver('Bob')
john = FileObserver('John')
stacy = FileObserver('Stacy')

fileWatcher = FileWatcher('c:/temp/README.txt')
fileWatcher.register(bob)
fileWatcher.register(john)
fileWatcher.register(stacy)

fileWatcher.poll()
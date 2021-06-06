# NEEDS FIXES AND CLARITY.
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import shutil


class EventHandler(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
        new_name = 'new_file_' + str(self.i) + '.txt'
        if not os.path.exists(destination):
            os.mkdir(destination)
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(destination + '/' + new_name)
            while file_exists:
                self.i += 1
                new_name = 'new_file_' + str(self.i) + '.txt'
                file_exists = os.path.isfile(destination + '/' + new_name)
            src = folder_to_track + '/' + filename
            final_destination = destination + '/' + new_name
            shutil.move(src, final_destination)


folder_to_track = '/Users/diego/Downloads'
destination = '/Users/diego/Documents/destination'
event_handler = EventHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(3)
except KeyboardInterrupt:
    observer.stop()
observer.join()

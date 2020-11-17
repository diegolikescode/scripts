from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

folder_to_track = 'thats my folder'
destination = 'thats where it goes'
class EventHandler(FileSystemEventHandler):
  def on_modified(self, event):
    for filename in os.listdir(folder_to_track):
      src = folder_to_track + '/' + filename
      os.rename(src, destination)

folder_to_track = '/Users/diego/Downloads'
destination = 'Users/diego/Downloads/example_destination'
event_handler = EventHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
  while True:
    time.sleep(10)
except KeyboardInterrupt:
  observer.stop()
observer.join()

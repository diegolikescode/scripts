from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import shutil
class EventHandler(FileSystemEventHandler):
  def on_modified(self, event):
    for filename in os.listdir(folder_to_track):
      src = folder_to_track + '/' + filename
      final_destination = destination + '/' + filename
      shutil.move(src, final_destination)

folder_to_track = '/Users/diego/Downloads'
destination = '/Users/diego/Desktop/xqdl'
event_handler = EventHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  observer.stop()
observer.join()

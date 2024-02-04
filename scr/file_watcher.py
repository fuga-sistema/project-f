from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileWatcher:
    def __init__(self, metadata_manager):
        # Initialize FileWatcher with a reference to a metadata manager
        self.observer = Observer()  # Create an observer object to monitor file system events
        self.metadata_manager = metadata_manager  # Store the metadata manager for later use

    def start(self):
        event_handler = FileEventHandler(self.metadata_manager)  # Create an event handler instance
        # Schedule the observer to monitor the current directory (not recursive)
        self.observer.schedule(event_handler, '.', recursive=False)
        self.observer.start()  # Start the observer thread

    def stop(self):
        # Stop monitoring and clean up
        self.observer.stop()  # Stop the observer
        self.observer.join()  # Wait for the observer thread to terminate


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, metadata_manager):
        # Initialize FileEventHandler with a reference to a metadata manager
        self.metadata_manager = metadata_manager  # Store the metadata manager for later use

    def on_modified(self, event):
        # Handle file modification events
        if not event.is_directory:  # Check if the event is for a file and not a directory
            self.metadata_manager.update_metadata(event.src_path)  # Update metadata for the modified file

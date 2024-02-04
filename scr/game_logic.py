class GameLogic:
    def __init__(self, metadata_manager, ui_manager):
        # Initialize the GameLogic class with references to MetadataManager and UIManager
        self.metadata_manager = metadata_manager  # Reference to manage game metadata
        self.ui_manager = ui_manager  # Reference to manage user interface

    def process_command(self, command):
        # Placeholder method for processing user commands
        # In a real game, this method would handle gameplay logic based on user input
        # For now, it displays a message indicating the received command
        self.ui_manager.display_message(f"Command '{command}' received.")

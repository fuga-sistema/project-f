# Import necessary modules and classes from other files
from ui_manager import UIManager
from file_watcher import FileWatcher
from metadata_manager import MetadataManager
from game_logic import GameLogic
from scene_manager import SceneManager
from scenes import ReadTheSecretScene


# Define the main function where the game execution begins
def main():
    # Initialize the user interface manager
    ui_manager = UIManager()

    # Initialize the metadata manager responsible for game state
    metadata_manager = MetadataManager()

    # Initialize the file watcher with a reference to the metadata manager
    file_watcher = FileWatcher(metadata_manager)

    # Initialize the game logic with references to the metadata manager and UI manager
    game_logic = GameLogic(metadata_manager, ui_manager)

    # Initialize the scene manager
    scene_manager = SceneManager()

    # Start the file watcher in a separate thread to monitor file system changes
    file_watcher.start()

    read_the_secret_scene = ReadTheSecretScene(metadata_manager, ui_manager)
    scene_manager.add_scene("ReadTheSecret", read_the_secret_scene)

    # Define "Read the Secret" como a cena inicial para o teste
    scene_manager.go_to_scene("ReadTheSecret")

    try:
        while True:
            command = ui_manager.get_user_input("Enter a command: ")
            if command.lower() == 'quit':
                break

            # Delegue a entrada do usuário ao SceneManager
            scene_manager.process_input(command)

            # Atualize e renderize a cena atual
            scene_manager.update()
            scene_manager.render()

    except KeyboardInterrupt:
        pass
    finally:
        file_watcher.stop()
        ui_manager.cleanup()


# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Execute the main function to start the game

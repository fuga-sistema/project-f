import json
from dataclasses import dataclass, asdict


# Define a data class to represent game metadata
@dataclass
class GameMetadata:
    # Example attributes for game metadata - adjust based on your game's needs
    level: int = 0
    # Additional attributes (e.g., score, player_name) can be added here


class MetadataManager:
    def __init__(self, filepath='game_state.json'):
        self.filepath = filepath  # Path to the file where game state will be saved

        try:
            # Try to load existing metadata from the specified file
            self.metadata = self.load_metadata()
        except FileNotFoundError:
            # If the file is not found (e.g., on the first run), create new metadata
            self.metadata = GameMetadata()

    def update_metadata(self, **kwargs):
        # Update metadata attributes based on game events or changes
        # Example: self.metadata.score += 10
        for key, value in kwargs.items():
            if hasattr(self.metadata, key):
                setattr(self.metadata, key, value)

        # Save the updated metadata to the file
        self.save_metadata()

    def save_metadata(self):
        # Serialize the game metadata to JSON and save it to a file
        with open(self.filepath, 'w') as f:
            json.dump(asdict(self.metadata), f, indent=4)

    def load_metadata(self):
        # Load and deserialize the game metadata from a file
        with open(self.filepath, 'r') as f:
            data = json.load(f)
            return GameMetadata(**data)

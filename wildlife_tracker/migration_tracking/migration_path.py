from typing import Optional, List
from wildlife_tracker.habitat_management.habitat import Habitat  # Referencing Habitat for start and destination

class MigrationPath:
    def __init__(self, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.duration = duration  

    def get_migration_path_details(self, path_id: int) -> dict:
        pass 

    def get_migration_paths_by_species(self, species: str) -> List['MigrationPath']:
        pass  

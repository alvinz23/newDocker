from typing import List, Optional
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.animal_management.animal import Animal

class HabitatManager:
    def __init__(self) -> None:
        self.habitats: dict[int, Habitat] = {}

    def create_habitat(self, habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass 

    def get_habitat_by_id(self, habitat_id: int) -> Optional[Habitat]:
        pass  

    def remove_habitat(self, habitat_id: int) -> None:
        pass  

    def assign_animals_to_habitat(self, habitat_id: int, animals: List[Animal]) -> None:
        pass  

    def get_habitats_by_geographic_area(self, geographic_area: str) -> List[Habitat]:
        pass 

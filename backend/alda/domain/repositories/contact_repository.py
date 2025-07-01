from abc import ABC, abstractmethod
from alda.domain.entities.contact import contact

class ContactRepository(ABC):
    @abstractmethod
    def create_contact(self, contact: contact) -> None:        
        pass
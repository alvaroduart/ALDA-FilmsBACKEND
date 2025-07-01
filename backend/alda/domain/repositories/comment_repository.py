from abc import ABC, abstractmethod
from alda.domain.entities.comment import Comment

class CommentRepository(ABC):    
    
    @abstractmethod
    def get_by_movie_id(self, movie_id: str) -> list[Comment]:
        pass
    
    @abstractmethod
    def create(self, comment: Comment) -> None:
        pass

    @abstractmethod
    def update(self, comment: Comment) -> None:
        pass

    @abstractmethod
    def delete(self, comment_id: str) -> None: 
        pass


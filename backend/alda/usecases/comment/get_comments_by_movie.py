from alda.domain.entities.comment import Comment
from alda.domain.repositories.comment_repository import CommentRepository
from typing import List


class GetCommentsByMovieUseCase:
    def __init__(self, repository: CommentRepository):
        self.repository = repository

    def execute(self, movie_id: str) -> List[Comment]:
        return self.repository.get_by_movie_id(movie_id)


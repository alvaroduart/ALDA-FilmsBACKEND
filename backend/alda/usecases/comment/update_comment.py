from alda.domain.entities.comment import Comment
from alda.domain.repositories.comment_repository import CommentRepository



class UpdateCommentUseCase:
    def __init__(self, repository: CommentRepository):
        self.repository = repository

    def execute(self, comment: Comment) -> None:
        if not comment.id:
            raise ValueError("Comment ID is required for update")
        self.repository.update(comment)
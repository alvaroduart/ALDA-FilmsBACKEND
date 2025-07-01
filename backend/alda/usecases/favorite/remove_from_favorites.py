from alda.domain.repositories.favorite_repository import FavoriteRepository


class RemoveFromFavoritesUseCase:
    def __init__(self, repository: FavoriteRepository):
        self.repository = repository

    def execute(self, user_id: str, movie_id: str) -> None:
        self.repository.remove_favorite(user_id, movie_id)


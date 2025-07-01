from alda.domain.entities.movie import Movie
from alda.domain.repositories.movie_repository import MovieRepository


class SearchMoviesUseCase:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def execute(self, query: str) -> list[Movie]:
        return self.repository.search(query)


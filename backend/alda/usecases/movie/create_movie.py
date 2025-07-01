from alda.domain.entities.movie import Movie
from alda.domain.repositories.movie_repository import MovieRepository


class CreateMovieUseCase:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def execute(self, movie: Movie) -> None:
        self.repository.create(movie)
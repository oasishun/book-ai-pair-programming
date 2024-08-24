import uuid
from uuid import UUID
from datetime import datetime

class Movie:
    id: UUID
    title: str

    def __init__(self, title: str):
        self.id = uuid.uuid4()
        self.title = title

class Ticket:
    id: UUID
    movie_id: str
    time: datetime 
    
    def __init__(self, movie: Movie, time: datetime):
        self.id = uuid.uuid4()
        self.movie_id = movie.id
        self.time = time

# Test data generation
def generate_test_data():
    # Create a Movie instance
    movie = Movie(title="Inception")
    
    # Create a Ticket instance
    ticket_time = datetime(2023, 10, 1, 15, 30)  # Example date and time
    ticket = Ticket(movie=movie, time=ticket_time)
    
    return movie, ticket

# Generate and print test data
movie, ticket = generate_test_data()
print(f"Movie ID: {movie.id}, Title: {movie.title}")
print(f"Ticket ID: {ticket.id}, Movie ID: {ticket.movie_id}, Time: {ticket.time}")

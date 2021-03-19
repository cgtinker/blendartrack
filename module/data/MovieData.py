class MovieData:
    def __init__(self, data_path):
        self.path = data_path

    def print_contents(self):
        print("path to .mov:", self.path)


def init_movie_data(path):
    movie_model = MovieData(path)
    return movie_model

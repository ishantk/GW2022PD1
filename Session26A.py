class IMDBMovieRating:

    def __init__(self, year, name, rating):
        self.year = year
        self.name = name
        self.rating = rating

    def to_csv(self):
        return "{year},{name},{rating}\n".format_map(vars(self))
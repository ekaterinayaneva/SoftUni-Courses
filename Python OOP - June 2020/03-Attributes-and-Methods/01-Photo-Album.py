class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for x in range(self.pages)]
        self.page = 0



    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count//4)


    def result(self):
        return self.photos

    def add_photo(self, label:str):
        if len(self.photos[self.page]) == 4:
            self.page += 1
            if self.page >= self.pages:
                return "No more free spots"
        self.photos[self.page].append(label)
        return f"{label} photo added successfully on page {self.page+1} slot {len(self.photos[self.page])}"


    def display(self):
        result = '-' * 11 + '\n'

        for page in self.photos:

            result += f"{''.join('[] ' for pic in range(len(page))).strip()}"

            result += '\n'
            result += '-' * 11 + '\n'
        return result




album = PhotoAlbum(2)



print(album.display())





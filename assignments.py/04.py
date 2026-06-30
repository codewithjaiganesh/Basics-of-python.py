class book:
    def __init__(self,title,author):
        self.list_of_reviews = []
        self.title = title
        self.Author = author
    def add_new_review(self,review):
        self.list_of_reviews.append(review)
    def display_reviews(self):
        print(f"The reviews are:{self.list_of_reviews}")
    def count_reviews(self):
        print(len(self.list_of_reviews))

stud1 = book("Titian","jai")
stud1.add_new_review("good")
stud1.display_reviews()
stud1.count_reviews()

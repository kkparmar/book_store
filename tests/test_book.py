from app.app import Book
import unittest


class TestBookApi(unittest.TestCase):

    def test_new_book(self):
        
        book = Book(isbn="9781593279509", title="Eloquent JavaScript, Third Edition", authors="Marijn Haverbeke", 
                    publisher="No Starch Press", categories=[
                    "Non-Fiction",
                    "Technology"], description="some description")
        self.assertEqual(book.title, "Eloquent JavaScript, Third Edition")
        self.assertEqual(book.authors[0],"Marijn Haverbeke")
        self.assertEqual(book.description,"some description" )
        self.assertEqual(book.__repr__(), "Book(ISBN=9781593279509, Title=Eloquent JavaScript, Third Edition)")


    def test_from_dict(self):
        data = {
                "isbn": "0439785960",
                "title": "Harry Potter and the Half-Blood Prince",
                "authors": [
                    "J.K. Rowling"
                ],
                "description": "HThe war against Voldemort is not going well; even Muggle governments are noticing. Ron scans the obituary pages of the Daily Prophet, looking for familiar names. Dumbledore is absent from Hogwarts for long stretches of time, and the Order of the Phoenix has already suffered losses.And yet . . .As in all wars, life goes on. The Weasley twins expand their business. Sixth-year students learn to Apparate - and lose a few eyebrows in the process. Teenagers flirt and fight and fall in love. Classes are never straightforward, through Harry receives some extraordinary help from the mysterious Half-Blood Prince.So it's the home front that takes center stage in the multilayered sixth installment of the story of Harry Potter. Here at Hogwarts, Harry will search for the full and complete story of the boy who became Lord Voldemort - and thereby find what may be his only vulnerability.",
                "categories": [
                    "Fantasy",
                    "Young Adult",
                    "Fiction"
                ],
                "publisher": "Scholastic Inc."
            }
        book = Book.from_dict(data)
        self.assertEqual(book.isbn, "0439785960" )
        self.assertListEqual(book.categories,  [
                    "Fantasy",
                    "Young Adult",
                    "Fiction"
                ])    

    def test_to_dict(self):
        book = Book(isbn="9781593279509", title="Eloquent JavaScript, Third Edition", authors="Marijn Haverbeke", 
                    publisher="No Starch Press", categories=[
                    "Non-Fiction",
                    "Technology"], description="some description")
        
        data = book.to_dict()
        self.assertDictEqual(data, {
            "isbn": "9781593279509",
            "title": "Eloquent JavaScript, Third Edition",
            "authors": ["Marijn Haverbeke"],
            "publisher": "No Starch Press",
            "categories": [
                "Non-Fiction",
                "Technology"
            ],
            "description": "some description"
        })
        print(data)
from django.core.management.base import BaseCommand, CommandError
from books.models import Book, Author
from faker import Faker
from random import choice

class Command(BaseCommand):
    help = 'Create 10 fake books'
    def handle(self, *args, **options):
        faker = Faker("pl_PL")
        authors = Author.objects.all()
        for i in range(10):
            book = Book()
            book.title = faker.text(max_nb_chars=50)
            book.pub_date = faker.past_date()
            book.description = faker.text(max_nb_chars=400)
            book.save()
            book.author.add(choice(authors))
            book.save()
            self.stdout.write(self.style.SUCCESS(f'Create: {str(book)}'))
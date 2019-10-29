from django.core.management.base import BaseCommand, CommandError
from books.models import Author
from faker import Faker

class Command(BaseCommand):
    help = 'Create 10 fake authors'
    def handle(self, *args, **options):
        faker = Faker("pl_PL")
        for i in range(10):
            author = Author()
            author.first_name = faker.first_name()
            author.last_name = faker.last_name()
            author.birthday = faker.date_of_birth()
            author.save()
            self.stdout.write(self.style.SUCCESS(f'Create: {str(author)}'))
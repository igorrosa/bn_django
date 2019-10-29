from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

# Creates selects for the model. Double tuple for select in html (value and view), translation from django via _
COVER_TYPES = (
    ('soft', _('soft')),
    ('hard', _('hard')),
)
SEX_TYPES = (
    ("male", _("male")),
    ("female", _("female")),
)

class TimeStamp(models.Model):
    # Creation date
    created = models.DateTimeField(auto_now_add = True)
    # Edition date
    modified = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

# All below inherit models.Model via TimeStamp class

class Author(TimeStamp):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null = True, blank=True)
    is_public_domain = models.BooleanField(default=False) # Default False
    sex = models.CharField(max_length=10, choices=SEX_TYPES, null = True, blank=True)
    biogram = models.TextField(null=True, blank=True)
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to="authors/%Y/%m/%d"
    )
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (ur. {self.birthday.year})"

class Book(TimeStamp):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    pub_date = models.DateField(null= True, blank = True) # No default date
    description = models.TextField(null=True, blank=True) # Non obligatory
    is_available = models.BooleanField(null=True, blank=True)
    cover_type = models.CharField(max_length=30, choices=COVER_TYPES, default="soft")
    cover_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="covers/%Y/%m/%d"
    )
    loan_date = models.DateTimeField(null= True, blank = True)

    @property
    def authors(self):
        return " - ".join([str(a) for  a in self.author.all()])
    def __str__(self):
        return f"{self.title} - {self.authors}"

#python manage.py dumpdata - zrzut danych
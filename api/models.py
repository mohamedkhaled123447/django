from django.db import models

# Create your models here.

from django.db import models

from django.db import models


class Gallery(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Gallery Name",
        help_text="Enter the name of the gallery.",
    )
    image = models.ImageField(
        upload_to="media/images/",
        verbose_name="Image",
        help_text="Upload an image for the gallery.",
    )
    description = models.CharField(
        max_length=500,
        verbose_name="Description",
        help_text="Enter a brief description of the gallery.",
    )
    TYPE_CHOICES = [
        ("galaxy", "Galaxy"),
        ("planet", "Planet"),
        ("star", "Star"),
        ("universe", "Universe"),
    ]
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        verbose_name="Type",
        help_text="Select the type of the gallery item.",
        default="galaxy",
    )

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Message(models.Model):
    email = models.EmailField(
        verbose_name="Email Address", help_text="Enter your email address."
    )
    subject = models.CharField(
        max_length=500,
        verbose_name="Subject",
        help_text="Enter the subject of your message.",
    )
    message = models.TextField(
        verbose_name="Message", help_text="Enter your message."
    )  # Changed to TextField for longer messages

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["-id"]  # Ordering by ID, so the newest messages come first

    def __str__(self):
        return f"{self.subject} from {self.email}"


class Video(models.Model):
    youtube_id = models.CharField(max_length=100, unique=True)  # YouTube video ID
    title = models.CharField(max_length=255)  # Title of the video
    description = models.TextField()  # Description of the video
    date_added = models.DateTimeField(auto_now_add=True)  # Timestamp when added

    def __str__(self):
        return self.title

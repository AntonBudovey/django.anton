from django.db import models
from django.urls import reverse

# Create your models here.
class Offer(models.Model):
    offer_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    offer_description = models.TextField()
    offer_price = models.DecimalField(max_digits=5,decimal_places=2)
    offer_picture = models.ImageField("Изображение", upload_to="image", default="img.jpg")

    def get_absolute_url(self):
        return reverse("details", kwargs={'offer_slug': self.slug})

    def __str__(self):
        return f"{self.offer_name}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["offer_name"]


class Comment(models.Model):
    antonrating = [(5, "Very Positive"),
                   (4, "Positive"),
                   (3, "Neutral"),
                   (2, "Negative"),
                   (1, "Very Negative")
                   ]
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    comment_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True,)
    rating = models.PositiveSmallIntegerField(choices=antonrating,)

    def __str__(self):
        return f"{self.comment_text}, {self.rating}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

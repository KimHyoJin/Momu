from django.db import models

LANGUAGE_CHOICES = (
    ("KR", "Korean"),
    ("EN", "English"),
    ("CH", "Chinese"),
    ("JP", "Japanese"),
)


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    boolean = models.BooleanField(default=False)
    char = models.CharField(null=False, blank=True, default="char", max_length=256)

    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    email = models.EmailField(null=False)
    text = models.TextField()

    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default="KR")

    class Meta:
        ordering = ('id',)

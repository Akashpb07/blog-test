from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=12)
    contact_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)

class institute_deatil(models.Model):
    email = models.EmailField(max_length=70,blank=True,unique=True)
    phone_number = models.CharField(max_length=12)
    main_quote_line1 = models.TextField()
    main_quote_line2 = models.TextField()
    address = models.CharField(("address"), max_length=128)
    city = models.CharField(("city"), max_length=64, default="Hoshiarpur")
    state = models.CharField(("state"), max_length=64, default="PB")
    zip_code = models.CharField(("zip code"), max_length=6, default="146001")

    def __str__(self):
        return self.main_quote_line1


class StoriesView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey('Stories', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Stories(models.Model):
    student_name = models.CharField(max_length=100)
    student_overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    band_score = models.CharField(max_length=50)
    # comment_count = models.IntegerField(default = 0)
    # view_count = models.IntegerField(default = 0)

    thumbnail = models.ImageField()

    featured = models.BooleanField()
    previous_story = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_story = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'pk': self.pk
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')



    # @property
    # def view_count(self):
    #     return StoriesView.objects.filter(post=self).count()

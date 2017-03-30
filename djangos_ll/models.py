from django.db import models
class Topic(models.Model):
    """A topic that the user is studying"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Return string views model"""
        return self.text

class Entry(models.Model):
    """Info lernings user on them"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            """Return str views model"""
            return self.text[:50] + "..."
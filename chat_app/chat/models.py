from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


class ChatMessage(Message):
    def get_html(self):
        return f"<b>{self.username}</b>: {self.content}<br>"


class InfoMessage(Message):
    def get_html(self):
        return f'<center><small class="has-text-grey-light">{self.content}</small></center>'

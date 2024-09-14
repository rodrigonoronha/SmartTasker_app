from django.db.models.signals import post_save
from django.dispatch import receiver
from comments.models import Comment
from ai.agent import CommentAgent
from rest_framework import response, status


@receiver(post_save, sender=Comment)
def ia_comment(sender, instance, **kwargs):

    Agent = CommentAgent()
    try:
        Agent.invoke()
    except:
        return response.Response(
            data={'result': 'OPENAI_API_KEY is invalid or you do not have credits in your account'},
            status=status.HTTP_400_BAD_REQUEST,
        )
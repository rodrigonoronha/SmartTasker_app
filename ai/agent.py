from django.conf import settings
from openai import OpenAI
from ai import prompts
from comments.models import Comment
import json
from django.core import serializers
from ai import models


class CommentAgent:

    def __init__(self):
        self.__comment = Comment.objects.all()
        self.__client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    def __get_comment(self):

        data_json_string = serializers.serialize('json', self.__comment)
        data_json = json.loads(data_json_string)[-1]

        return json.dumps({
            'comment': data_json
        })

    def invoke(self):
        response = self.__client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    'role': 'system',
                    'content': prompts.SYSTEM_PROMPT
                },
                {
                    'role': 'user',
                    'content': prompts.USER_PROMPT.replace('{{comment}}', self.__get_comment()),
                }
            ],
            temperature=1.2
        )
        result = response.choices[0].message.content
        models.AIResult.objects.create(result=result)

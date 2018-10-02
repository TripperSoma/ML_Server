from django.db import models


class ReviewModel(models.Model):
    user_id = models.PositiveIntegerField(verbose_name='유저_아이디')
    trip_id = models.PositiveIntegerField(verbose_name='여행_아이디')
    rating = models.FloatField(verbose_name='점수')
    timestamp = models.DateTimeField(verbose_name='등록일')
    created = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        unique_together = (('user_id', 'trip_id'),)
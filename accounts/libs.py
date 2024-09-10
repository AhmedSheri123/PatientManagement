from django.utils import timezone
import math

def DatetimeNow(user):
    datetime_now = timezone.now()
    return datetime_now


def when_published(creation_date):
    if not creation_date:
        return ''

    now = timezone.now()
    
    diff= now - creation_date

    if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
        seconds= diff.seconds
        
        if seconds == 1:
            return str(seconds) + " שנייה"
        
        else:
            return str(seconds) + " שניות"

        

    if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
        minutes= math.floor(diff.seconds/60)

        if minutes == 1:
            return str(minutes)  + " דקה"
        
        else:
            return str(minutes)  + " דקה"



    if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
        hours= math.floor(diff.seconds/3600)

        if hours == 1:
            return str(hours) + " שעה"

        else:
            return str(hours) + " שעות"

    # 1 day to 30 days
    if diff.days >= 1 and diff.days < 30:
        days= diff.days
    
        if days == 1:
            return str(days) + " יום"

        else:
            return str(days) + " ימים"

    if diff.days >= 30 and diff.days < 365:
        months= math.floor(diff.days/30)
        

        if months == 1:
            return str(months) + " חודש"

        else:
            return str(months) + " חדשים"


    if diff.days >= 365:
        years= math.floor(diff.days/365)

        if years == 1:
            return str(years) + " שנה"

        else:
            return str(years) + " שנים"


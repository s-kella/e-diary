def fix_marks(schoolkid):
    from datacenter.models import Mark
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    from datacenter.models import Chastisement
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject):
    from datacenter.models import Commendation, Lesson
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title=subject).order_by('-date').first()
    Commendation.objects.create(created=lesson.date, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher, text='Молодец!')
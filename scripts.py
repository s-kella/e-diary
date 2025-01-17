def get_schoolkid(full_name):
    from datacenter.models import Schoolkid
    try:
        kid = Schoolkid.objects.get(full_name__contains=full_name)
        return kid
    except Schoolkid.DoesNotExist:
        print('Такой ученик не существует.')
    except Schoolkid.MultipleObjectsReturned:
        print('Существует более одного ученика с таким именем, уточните запрос.')


def fix_marks(schoolkid):
    from datacenter.models import Mark
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    from datacenter.models import Chastisement
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject):
    import random
    from datacenter.models import Commendation, Lesson
    commendations = ['Молодец!', 'Отлично!', 'Хорошо!', 'Талантливо!', 'Прекрасно!']
    try:
        lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title=subject).order_by('-date').first()
        Commendation.objects.create(created=lesson.date, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher, text=random.choice(commendations))
    except AttributeError:
        print(f'Данные о предмете {subject} не найдены')

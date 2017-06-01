from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    club_name = models.CharField(max_length=100, null=True)
    club_parent = models.ForeignKey('self', null=True, blank=True)
    club_members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.club_name


class Nomination(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    results_declared = models.BooleanField(default=False)
    nomi_form = models.OneToOneField('forms.Questionnaire', null=True, blank=True)

    def __str__(self):
        return self.name


class NominationInstance(models.Model):
    STATUS = (
        ('a', 'Accepted'),
        ('r', 'Rejected'),
    )

    nomination = models.ForeignKey('Nomination', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS,  null=True, blank=True, default=None)
    filled_form = models.OneToOneField('forms.FilledForm', null=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.id)


class Post(models.Model):
    STATUS = (
        ('Nomination created', 'Nomination created'),
        ('Nomination out', 'Nomination out'),
        ('Interview period', 'Interview period'),
        ('Assigned', 'Assigned'),

    )
    post_name = models.CharField(max_length=500, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    post_holders = models.ManyToManyField(User, blank=True)
    nomination = models.OneToOneField(Nomination, null=True, blank=True)
    approvals = models.ManyToManyField('self', blank=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Nomination created')



    def __str__(self):
        return self.post_name


class UserProfile(models.Model):
    PROGRAMME = (
        ('B.Tech', 'B.Tech'),
        ('B.S', 'B.S'),
    )

    DEPT = (
        ('Aerospace Engineering', 'AE'),
        ('Biological Sciences & Engineering', 'BSBE'),
        ('Chemical Engineering', 'CHE'),
        ('Civil Engineering', 'CE'),
        ('Computer Science & Engineering', 'CSE'),
        ('Electrical Engineering', 'EE'),
        ('Materials Science & Engineering', 'MSE'),
        ('Mechanical Engineering', 'ME'),
        ('Industrial & Management Engineering', 'IME'),
        ('Chemistry', 'CHM'),
        ('Mathematics & Scientific Computing', 'MTH'),
        ('Physics', 'PHY'),
        ('Earth Sciences', 'ES')
    )

    YEAR = (
        ('Y16', 'Y16'),
        ('Y15', 'Y15'),
        ('Y14', 'Y14'),
        ('Y13', 'Y13'),
        ('Y12', 'Y12'),
        ('Y11', 'Y11'),
    )

    HALL = (
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'),
        (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)
    roll_no = models.IntegerField(null=True)
    year = models.CharField(max_length=4, choices=YEAR, default='Y16')
    programme = models.CharField(max_length=7, choices=PROGRAMME, default='B.Tech')
    department = models.CharField(max_length=200, choices=DEPT, default=None)
    hall = models.IntegerField(choices=HALL, default=1)
    room_no = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.name)



##there is some changes to be done in model,we would remove nomination from post and
        # make post foreignkey in nomination model and some other changes also..
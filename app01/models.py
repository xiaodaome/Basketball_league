from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    state = models.CharField(max_length=100)
    class Meta:
        db_table = 'city'

class Team(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, db_column='city')
    arena = models.CharField(max_length=100)
    class Meta:
        db_table = 'team'

class Owner(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    corporation = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.OneToOneField(Team, on_delete=models.CASCADE, db_column='team')
    class Meta:
        db_table = 'owner'

class Country(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    continent = models.CharField(max_length=100)
    rank = models.IntegerField()
    national_league = models.CharField(max_length=100)
    class Meta:
        db_table = 'country'

class Coach(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='team')
    age = models.IntegerField()
    CoachingExperience = models.IntegerField()
    class Meta:
        db_table = 'coach'

class Game(models.Model):
    home = models.ForeignKey(Team, related_name="home_team", on_delete=models.CASCADE, db_column='home')
    away = models.ForeignKey(Team, related_name="away_team", on_delete=models.CASCADE, db_column='away')
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'game'
        unique_together = (('home','date'))

class Player(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, db_column='team')
    age = models.IntegerField()
    height = models.IntegerField()
    pos = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, db_column='country')
    class Meta:
        db_table = 'player'

class Draft(models.Model):
    year = models.IntegerField()
    pick = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='team')
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True, db_column='player')
    class Meta:
        db_table = 'draft'

class Contract(models.Model):
    salary = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='team')
    StartDate = models.DateField()
    EndDate = models.DateField()
    class Meta:
        db_table = 'contract'
        unique_together = (('player', 'team','StartDate'))


class Season(models.Model):
    year = models.IntegerField(primary_key=True)
    champion = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='champion')
    mvp = models.ForeignKey(Player, related_name="mvp", on_delete=models.CASCADE, db_column='mvp')
    scoring_title = models.ForeignKey(Player, related_name="scoring_title", on_delete=models.CASCADE, db_column='scoring_title')
    class Meta:
        db_table = 'season'

class Champion(models.Model):
    year = models.IntegerField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='team')
    fmvp = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='fmvp')
    class Meta:
        db_table = 'champion'
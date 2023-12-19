from django.shortcuts import render, HttpResponse, redirect
from app01.models import *
import pymysql


# Create your views here.


def home(request):
    if request.method == "GET":
        query_id = request.GET.get('set_query', 'none')
        conn = pymysql.connect(host="localhost", port=3306, user='root', password='Chen20020719fd',
                               database='basketball_league', charset='utf8')
        cursor = conn.cursor()
        team_dict = {}
        show_query_result = 'none'
        if query_id == '1':
            sql = '''select T.name,S.name,T.team
                        from player as T,player as S
                        where T.team = S.team and T.name != S.name;'''
            cursor.execute(sql)
            sql_result = cursor.fetchall()

            for player1, player2, team in sql_result:
                if team not in team_dict:
                    team_dict[team] = []
                if player1 not in team_dict[team]:
                    team_dict[team].append(player1)
                if player2 not in team_dict[team]:
                    team_dict[team].append(player2)
            show_query_result = '1'
            cursor.close()
            conn.close()
        elif query_id == '2':
            sql = '''select T.player,S.player,T.year 
                    from draft as T,draft as S
                    where T.player!=S.player and T.year = S.year;'''
            cursor.execute(sql)
            sql_result = cursor.fetchall()
            for player1, player2, team in sql_result:
                if team not in team_dict:
                    team_dict[team] = []
                if player1 not in team_dict[team]:
                    team_dict[team].append(player1)
                if player2 not in team_dict[team]:
                    team_dict[team].append(player2)

            show_query_result = '2'
            cursor.close()
            conn.close()
        elif query_id == '3':
            sql = '''select name
                    from player
                    where name not in(select player
			                        from draft);'''
            cursor.execute(sql)
            sql_result = cursor.fetchall()
            team_dict = []
            for player in sql_result:
                team_dict.append(player[0])
            show_query_result = '3'
            cursor.close()
            conn.close()
        elif query_id == '4':
            sql = '''select country, count(name) as player_count
                        from player
                        where country != 'USA'
                        group by country
                        order by player_count desc
                        LIMIT 10;'''
            cursor.execute(sql)
            sql_result = cursor.fetchall()
            team_dict = {}
            for country, cnt in sql_result:
                team_dict[country] = cnt
            print(team_dict)
            show_query_result = '4'
            cursor.close()
            conn.close()
        elif query_id == '5':
            sql = '''select T.fmvp
                    from champion as T, season as S
                    where T.year = S.year and T.fmvp = S.mvp;'''
            cursor.execute(sql)
            sql_result = cursor.fetchall()
            team_dict = []
            for player in sql_result:
                team_dict.append(player[0])
            show_query_result = '5'
            cursor.close()
            conn.close()
        elif query_id == '6':
            sql = '''select T.name, T.team, (select avg(height) from player as S where T.team = S.team) as average_height
                    from player as T
                    where T.height > (select avg(S.height)
					from player as S
					where T.team=S.team);'''
            cursor.execute(sql)
            sql_result = cursor.fetchall()
            team_dict = []
            for player, team,avg_height in sql_result:
                team_dict.append([player,team,avg_height])
            show_query_result = '6'
            print(team_dict)
            cursor.close()
            conn.close()
        elif query_id == '7':
            sql = '''select distinct T.player
                    from contract as T
                    where not exists(
		                        (select name
                                from team
                                where city="Los Angeles")
                                except
                                (select team
                                from contract as S
                                where T.player = S.player));'''
            cursor.execute(sql)
            sql_result = cursor.fetchall()
            team_dict = []
            for player in sql_result:
                team_dict.append(player[0])
            show_query_result = '7'
            cursor.close()
            conn.close()
        elif query_id == '8':
            sql = '''select distinct T.name
                    from player as T,(select distinct team, max(height) as max_height
                    from player
                    group by team) as S
                    where T.height > S.max_height;'''
            cursor.execute(sql)
            sql_result = cursor.fetchall()
            team_dict = []
            for player in sql_result:
                team_dict.append(player[0])
            show_query_result = '8'
            cursor.close()
            conn.close()
        elif query_id == '9':
            sql = '''select T.name, T.team
                    from owner as T, (select team
                    from champion 
                    group by team
                    having count(year)>1) as S
                    where T.team = S.team;'''
            cursor.execute(sql)
            sql_result = cursor.fetchall()
            team_dict = []
            for owner,team in sql_result:
                team_dict.append([owner,team])
            show_query_result = '9'
            cursor.close()
            conn.close()
        elif query_id == '10':
            sql = '''select city
                    from team
                    group by city
                    having count(name)>1;'''
            cursor.execute(sql)
            sql_result = cursor.fetchall()
            team_dict = []
            for city in sql_result:
                team_dict.append(city[0])
            show_query_result = '10'
            cursor.close()
            conn.close()
        show_data = request.GET.get('show_data', 'none')
        if show_data == 'player':
            info = Player.objects.all()
        elif show_data == 'team':
            info = Team.objects.all()
        elif show_data == 'game':
            info = Game.objects.all()
        elif show_data == 'coach':
            info = Coach.objects.all()
        elif show_data == 'owner':
            info = Owner.objects.all()
        elif show_data == 'country':
            info = Country.objects.all()
        elif show_data == 'city':
            info = City.objects.all()
        elif show_data == 'contract':
            info = Contract.objects.all()
        elif show_data == 'draft':
            info = Draft.objects.all()
        elif show_data == 'season':
            info = Season.objects.all()
        elif show_data == 'champion':
            info = Champion.objects.all()
        else:
            info = []
        th = {'player': ['name', 'team', 'age', 'height', 'pos', 'country'],
              'team': ['name', 'city', 'arena'],
              'game': ['home', 'away', 'home_score', 'away_score', 'date'],
              'coach': ['name', 'team', 'age', 'CoachingExperience'],
              'owner': ['name', 'corporation', 'age', 'team'],
              'country': ['name', 'continent', 'rank', 'national_league'],
              'city': ['name', 'state'],
              'contract': ['player', 'team', 'salary', 'StartDate', 'EndDate'],
              'draft': ['player', 'team', 'year', 'pick'],
              'season': ['year', 'champion', 'mvp'],
              'champion': ['year', 'team', 'fmvp'],
              'none': []}
        ask = request.GET.get('ask', 'none')
        return render(request, "home.html", {"type": show_data, "info": info, "th": th[show_data],
                                             'ask':ask,"query_result":team_dict,"show_query_result":show_query_result})
    elif request.method == "POST":
        conn = pymysql.connect(host="localhost", port=3306, user='root', password='Chen20020719fd',
                               database='basketball_league', charset='utf8')
        cursor = conn.cursor()
        insert = request.POST.get('insert', 'none')
        delete = request.POST.get('delete', 'none')
        update = request.POST.get('update', 'none')
        if 'on' in [insert, delete, update]:
            sql = request.POST.get('query_sentence', 'none')
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            return render(request, "home.html")
        else:
            sql = request.POST.get('query_sentence', 'none')
            cursor.execute(sql)
            info = cursor.fetchall()
            cursor.close()
            return render(request, "home.html",{"free_show_res":'true',"free_info":info})



import nflgame
import plotly
from plotly.offline import plot
from plotly.graph_objs import Scatter, Marker, Line

# Tom Brady stats
brady_ypa = []
brady_ypc = []
brady_tds = []
brady_turnovers = []
brady_gms = []

# Alex Smith stats
smith_ypa = []
smith_ypc = []
smith_tds = []
smith_turnovers = []
smith_gms = []

bradyGmCnt = 1;
smithGmCnt = 1;

for num_year in range(2013,2016):
    for num_week in range(1,18):
        game = nflgame.games(num_year, week=num_week)
        players = nflgame.combine_game_stats(game)
        for p in players:
            if p.guess_position == 'QB':
                if p.name == 'T.Brady':
                    brady_ypa.append(round(float(p.passing_yds) / float(p.passing_att), 1))
                    brady_ypc.append(round(float(p.passing_yds) / float(p.passing_cmp), 1))
                    brady_tds.append(p.passing_tds + p.rushing_tds)
                    brady_turnovers.append(p.passing_ints + p.fumbles_lost)
                    brady_gms.append(bradyGmCnt)
                    bradyGmCnt += 1
                elif p.name == 'A.Smith':
                    smith_ypa.append(round(float(p.passing_yds) / float(p.passing_att), 1))
                    smith_ypc.append(round(float(p.passing_yds) / float(p.passing_cmp), 1))
                    smith_tds.append(p.passing_tds + p.rushing_tds)
                    smith_turnovers.append(p.passing_ints + p.fumbles_lost)
                    smith_gms.append(smithGmCnt)
                    smithGmCnt += 1

# Yards per completion plot
bradyYpc = Scatter(
    x = brady_gms,
    y = brady_ypc,
    name = 'Brady YPC',
    mode = 'markers',
    marker = Marker(
        color = 'blue'
    )
)
smithYpc = Scatter(
    x = smith_gms,
    y = smith_ypc,
    name = 'Smith YPC',
    mode = 'markers',
    marker = Marker(
        color = 'red'
    )
)

# Tds plot
bradyTds = Scatter(
    x = brady_gms,
    y = brady_tds,
    name = 'Brady TDs',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color = 'blue'
    )
)
smithTds = Scatter(
    x = smith_gms,
    y = smith_tds,
    name = 'Smith TDs',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color = 'red'
    )
)

# Turnovers plot
bradyTurnovers = Scatter(
    x = brady_gms,
    y = brady_turnovers,
    name = 'Brady Turnovers',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color = 'blue'
    )
)
smithTurnovers = Scatter(
    x = smith_gms,
    y = smith_turnovers,
    name = 'Smith Turnovers',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color = 'red'
    )
)

dataYpc = [bradyYpc, smithYpc]
dataYpcTurnovers = [bradyYpc, smithYpc, bradyTurnovers, smithTurnovers]
dataYpcTDs = [bradyYpc, smithYpc, bradyTds, smithTds]

# Edit the layout
layoutYpc = dict(title = 'Alex Smith vs. Tom Brady (2013-2015)',
              xaxis = dict(title = 'Games'),
              yaxis = dict(title = 'Yards per Completion')
              )

layoutYpcTurnovers = dict(title = 'Alex Smith vs. Tom Brady (2009-2015)',
              xaxis = dict(title = 'Games')
              )

layoutYpcTds = dict(title = 'Alex Smith vs. Tom Brady (2009-2015)',
              xaxis = dict(title = 'Games')
              )

# Plot and embed in ipython notebook!
figYpc = dict(data=dataYpc, layout=layoutYpc)
plot(figYpc, filename='plots/smith_brady_ypc.html')
 
#figYpcTurnovers = dict(data=dataYpcTurnovers, layout=layoutYpcTurnovers)
#plot(figYpcTurnovers, filename='plots/smith_brady_ypc_turnovers.html')

#figYpcTds = dict(data=dataYpcTDs, layout=layoutYpcTds)
#plot(figYpcTds, filename='plots/smith_brady_ypc_tds.html')
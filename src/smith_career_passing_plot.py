import nflgame
import plotly
from plotly.offline import plot
from plotly.graph_objs import Scatter, Marker

# Tom Brady stats
brady_yds = []
brady_rush_yds = []
brady_gms = []

# Alex Smith stats
smith_yds = []
smith_rush_yds = []
smith_gms = []

# Peyton Manning stats
peyton_yds = []
peyton_rush_yds = []
peyton_gms = []

# Russell Wilson stats
wilson_yds = []
wilson_rush_yds = []
wilson_gms = []

bradyGmCnt = 1;
smithGmCnt = 1;
peytonGmCnt = 1
wilsonGmCnt = 1;

for num_year in range(2013,2016):
    for num_week in range(1,18):
        game = nflgame.games(num_year, week=num_week)
        players = nflgame.combine_game_stats(game)
        for p in players:
            if p.guess_position == 'QB':
                if p.name == 'T.Brady':
                    brady_yds.append(p.passing_yds)
                    brady_rush_yds.append(p.rushing_yds)
                    brady_gms.append(bradyGmCnt)
                    bradyGmCnt += 1
                elif p.name == 'A.Smith':
                    smith_yds.append(p.passing_yds)
                    smith_rush_yds.append(p.rushing_yds)
                    smith_gms.append(smithGmCnt)
                    smithGmCnt += 1
                elif p.name == 'P.Manning':
                    peyton_yds.append(p.passing_yds)
                    peyton_rush_yds.append(p.rushing_yds)
                    peyton_gms.append(peytonGmCnt)
                    peytonGmCnt += 1
                elif p.name == 'R.Wilson':
                    wilson_yds.append(p.passing_yds)
                    wilson_rush_yds.append(p.rushing_yds)
                    wilson_gms.append(wilsonGmCnt)
                    wilsonGmCnt += 1

# Passing plots
bradyYds = Scatter(
    x = brady_gms,
    y = brady_yds,
    name = 'Tom Brady',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color = 'blue'
    )
)
smithYds = Scatter(
    x = smith_gms,
    y = smith_yds,
    name = 'Alex Smith',
    mode = 'lines+markers',
    marker = Marker(
        symbol = 'diamond',
        color ='red'
    )
)
peytonYds = Scatter(
    x = peyton_gms,
    y = peyton_yds,
    name = 'Peyton Manning',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color ='orange'
    )
)
wilsonYds = Scatter(
    x = wilson_gms,
    y = wilson_yds,
    name = 'Russell Wilson',
    mode = 'lines+markers',
    marker = Marker(
        symbol = 'diamond',
        color ='green'
    )
)

data = [smithYds, bradyYds, peytonYds, wilsonYds]

# Edit the layout
layout = dict(title = 'Alex Smith vs. Superbowl Winning QBs (2013-2015)',
              xaxis = dict(title = 'Games'),
              yaxis = dict(title = 'Passing Yards')
              )

# Plot and embed in ipython notebook!
fig = dict(data=data, layout=layout)
plot(fig, filename='smith-vs-sb-winning-qbs-passing-plot')

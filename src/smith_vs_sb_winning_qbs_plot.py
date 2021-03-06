import nflgame
import plotly
from plotly.offline import plot
from plotly.graph_objs import Scatter, Marker

# Tom Brady stats
brady_yds = []
brady_tds = []
brady_ints = []

# Peyton Manning stats
pmanning_yds = []
pmanning_tds = []
pmanning_ints = []

# Alex Smith stats
smith_yds = []
smith_tds = []
smith_ints = []

# Russell Wilson
wilson_yds = []
wilson_tds = []
wilson_ints = []

# Joe Flacco
flacco_yds = []
flacco_tds = []
flacco_ints = []

# Aaron Rodgers
rodgers_yds = []
rodgers_tds = []
rodgers_ints = []

# Drew Brees
brees_yds = []
brees_tds = []
brees_ints = []

# Eli Manning
emanning_yds = []
emanning_tds = []
emanning_ints = []

for num_year in range(2015,2016):
    for num_week in range(1,18):
        game = nflgame.games(num_year, week=num_week)
        players = nflgame.combine_game_stats(game)
        for p in players:
            if p.guess_position == 'QB':
                if p.name == 'T.Brady':
                    brady_yds.append(p.passing_yds)
                    brady_tds.append(p.passing_tds)
                    brady_ints.append(p.passing_ints)
                elif p.name == 'A.Smith':
                    smith_yds.append(p.passing_yds)
                    smith_tds.append(p.passing_tds)
                    smith_ints.append(p.passing_ints)
                elif p.name == 'P.Manning':
                    pmanning_yds.append(p.passing_yds)
                    pmanning_tds.append(p.passing_tds)
                    pmanning_ints.append(p.passing_ints)
                #elif p.name == 'E.Manning':
                    #emanning_yds.append(p.passing_yds)
                    #emanning_tds.append(p.passing_tds)
                    #emanning_ints.append(p.passing_ints)
                elif p.name == 'R.Wilson':
                    wilson_yds.append(p.passing_yds)
                    wilson_tds.append(p.passing_tds)
                    wilson_ints.append(p.passing_ints)
                #elif p.name == 'J.Flacco':
                    #flacco_yds.append(p.passing_yds)
                    #flacco_tds.append(p.passing_tds)
                    #flacco_ints.append(p.passing_ints)
                #elif p.name == 'A.Rodgers':
                    #rodgers_yds.append(p.passing_yds)
                    #rodgers_tds.append(p.passing_tds)
                    #rodgers_ints.append(p.passing_ints)
                #elif p.name == 'D.Brees':
                    #brees_yds.append(p.passing_yds)
                    #brees_tds.append(p.passing_tds)
                    #brees_ints.append(p.passing_ints)

bradyTds = Scatter(
    x = brady_yds,
    y = brady_tds,
    name = 'Tom Brady',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color = 'blue'
    )
)
pManningTds = Scatter(
    x = pmanning_yds,
    y = pmanning_tds,
    name = 'Peyton Manning',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color = 'orange'
    )
)
smithTds = Scatter(
    x = smith_yds,
    y = smith_tds,
    name = 'Alex Smith',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color ='red'
    )
)
eManningTds = Scatter(
    x = emanning_yds,
    y = emanning_tds,
    name = 'Eli Manning',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond'
    )
)
wilsonTds = Scatter(
    x = wilson_yds,
    y = wilson_tds,
    name = 'Russell Wilson',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color = 'green'
    )
)
flaccoTds = Scatter(
    x = flacco_yds,
    y = flacco_tds,
    name = 'Joe Flacco',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond'
    )
)
rodgersTds = Scatter(
    x = rodgers_yds,
    y = rodgers_tds,
    name = 'Aaron Rodgers',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond'
    )
)
breesTds = Scatter(
    x = brees_yds,
    y = brees_tds,
    name = 'Drew Brees',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond'
    )
)

data = [smithTds, wilsonTds, bradyTds, pManningTds]
#data = [bradyTds, smithTds, pManningTds, wilsonTds]#, eManningTds, flaccoTds, rodgersTds, breesTds]

# Edit the layout
layout = dict(title = 'Alex Smith vs. Super Bowl Winning QBs (2013-2015)',
              xaxis = dict(title = 'Passing Yards'),
              yaxis = dict(title = 'Passing Touchdowns')
              )

# Plot and embed in ipython notebook!
fig = dict(data=data, layout=layout)
plot(fig, filename='smith-vs-sb-winning-qbs')

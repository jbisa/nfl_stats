import nflgame
import plotly
from plotly.offline import plot
from plotly.graph_objs import Scatter, Marker, Line

# Tom Brady stats
brady_cmp_pct = []
brady_pass_tds_pct = []
brady_ints_pct = []
brady_gms = []

# Alex Smith stats
smith_cmp_pct = []
smith_pass_tds_pct = []
smith_ints_pct = []
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
                    brady_cmp_pct.append(round(float(p.passing_cmp) / float(p.passing_att) * 100, 1))
                    brady_pass_tds_pct.append(round(float(p.passing_tds) / float(p.passing_att) * 100, 1))
                    #brady_ints_pct.append(round(float(p.passing_ints) / float(p.passing_att) * 100, 1))
                    brady_gms.append(bradyGmCnt)
                    bradyGmCnt += 1
                elif p.name == 'A.Smith':
                    smith_cmp_pct.append(round(float(p.passing_cmp) / float(p.passing_att) * 100, 1))
                    smith_pass_tds_pct.append(round(float(p.passing_tds) / float(p.passing_att) * 100, 1))
                    #smith_ints_pct.append(round(float(p.passing_ints) / float(p.passing_att) * 100, 1))
                    smith_gms.append(smithGmCnt)
                    smithGmCnt += 1

# Completion Percentage
bradyCmpPct = Scatter(
    x = brady_gms,
    y = brady_cmp_pct,
    name = 'Brady Completion %',
    mode = 'markers',
    marker = Marker(
        color = 'blue'
    )
)
smithCmpPct = Scatter(
    x = smith_gms,
    y = smith_cmp_pct,
    name = 'Smith Completion %',
    mode = 'markers',
    marker = Marker(
        color = 'red'
    )
)

# Passing TDs Percentage
bradyPassTdsPct = Scatter(
    x = brady_gms,
    y = brady_pass_tds_pct,
    name = 'Brady TD %',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color = 'blue'
    )
)
smithPassTdsPct = Scatter(
    x = smith_gms,
    y = smith_pass_tds_pct,
    name = 'Smith TD %',
    mode = 'markers',
    marker = Marker(
        symbol = 'diamond',
        color = 'red'
    )
)

data = [bradyCmpPct, smithCmpPct, bradyPassTdsPct, smithPassTdsPct]

# Edit the layout
layout = dict(title = 'Alex Smith vs. Tom Brady (2013-2015)',
              xaxis = dict(title = 'Games'),
              yaxis = dict(title = 'Percentage')
              )

# Plot and embed in ipython notebook!
fig = dict(data=data, layout=layout)
plot(fig, filename='plots/smith_brady_completion_percentage.html')

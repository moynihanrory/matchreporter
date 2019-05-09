Match Aggregated Data
=====================
Overview
--------
This data is saved in a file with the name match-agg-data.gen.xlsx. It is always written to the output location as specified on the command line.
It contains a number of tabs. Each tab counts the various events described in the following sections

Match
-----
This is a simple overall match dataset. It gives a count of each event/kpi (row) per team (column) for the entire match.

Players1
--------
This is a dataset that represents the players (row) and the associated events/kpi (column) over the course of a full game.
Players1 will be for the first teams' set of players and Players2 the other team.

Players2
--------
This is a dataset that represents the players (row) and the associated events/kpi (column) over the course of a full game.
Players2 will be for the second teams' set of players and Players1 the other team.

Halves
------
This is a simple dataset providing a count of each event/kpi (row) per team (column) and per half.

Sectors
-------
This is a dataset providing a count of each event/kpi (row) per team (column) and per time sector.
A time sector is a 10 minute period. There are 3 per half 0-10, 10-20, 20-End.

Location1
---------
This is a dataset providing a count of each event/kpi (row) per pitch location (column) over the course of a full game.
Location1 will be for the first teams' events and Location2 the other team.

Location2
---------
This is a dataset providing a count of each event/kpi (row) per pitch location (column) over the course of a full game.
Location2 will be for the second teams' events and Location1 the other team.

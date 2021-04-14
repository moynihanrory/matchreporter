GAA Match Reporter
==================
A python module to generate data used for match reporting.

This module was created to parse the output of GAA Match mobile Apps, aggregate and count the data and generate and output a match report.

Getting Started
---------------
First you need some actual match data to work with. Record a catalog of match events (`GAA Apps <http://gaaapps.com/>`__) using either `GAA Match Reporter <https://itunes.apple.com/us/app/gaa-match-reporter/id951356333?ls=1&mt=8>`__ (iOS) or `GAA Scores Stats Plus <https://play.google.com/store/apps/details?id=fm.gaa_scores.plus>`__ (Android).
Once you have the match events recorded in the App you will need to share the events. The easiest way is to share all events via email with yourself. When you recieve the email, save the body (text content) of the email as a text file.
You can also use the XML output from Hudl SportsCode as input.

Running
-------
The main method of the module is in matchreporter_cli.py. This takes 2 arguments:
 * -gaamatch. This is the full path and name of the text file containing the match events.
 * -sc. This is the full path and name of the text file containing the match events (from Hudl SportsCode)

Example
^^^^^^^
Assuming you have saved a catalog of match events to a text file (e.g. teama-v-teamb.txt) you can then run the module and generate a match report.

.. code::

    python3 matchreporter/matchreporter_cli.py -gaamatch teama-v-teamb.txt


Installation
------------
Requirements
^^^^^^^^^^^^

-  Python 3
-  MySQL

Installing
^^^^^^^^^^
Then, install this module from pypi using ``pip3`` :

.. code::

    pip3 install matchreporter

Database
^^^^^^^^
Run the SQL script db/analysis_db.sql. Create an account gaa/autopwd or update db/database.py as appropriate.


Thanks & Credits
----------------
* Many, many thanks to `GAA Apps <http://gaaapps.com/>`__ for creating the mobile Apps and making available for free!
* Thanks to Jonny Bradley `@JohnnyBrad1ey <https://twitter.com/JohnnyBrad1ey>`__ for publishing his original report on which the Excel is based and copied.
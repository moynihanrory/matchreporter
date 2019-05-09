GAA Match Reporter
==================
A python module to generate a detailed GAA match analysis report.

This module was created to parse the output of GAA Match mobile Apps, aggregate and count the data and generate and output a match report.

Getting Started
---------------
First you need some actual match data to work with. Record a catalog of match events (`GAA Apps <http://gaaapps.com/>`__) using either `GAA Match Reporter <https://itunes.apple.com/us/app/gaa-match-reporter/id951356333?ls=1&mt=8>`__ (iOS) or `GAA Scores Stats Plus <https://play.google.com/store/apps/details?id=fm.gaa_scores.plus>`__ (Android). Once you have the match events recorded in the App you will need to share the events. The easiest way is to share all events via email with yourself. When you recieve the email, save the body (text content) of the email as a text file.

Running
-------
The main method of the module is in matchreporter_cli.py. This takes 2 arguments:
 * -gaamatch. This is the full path and name of the text file containing the match events.
 * -outputDirectory. This is the directory where the report will be written to. This is an optional paramter - if not specified it will default to the current working directory.

Example
^^^^^^^
Assuming you have saved a catalog of match events to a text file (e.g. teama-v-teamb.txt) you can then run the module and generate a match report.

.. code::

    python3 matchreporter/matchreporter_cli.py -gaamatch teama-v-teamb.txt

Output
^^^^^^
A new directory will be created for the report. The directory name is of the format: 'match-analysis-report_<team1>_<team2>_<dd_mm_yyy>.

Within the directory will be 2 files:
 * report-agg-data.xlsx. This is the aggregated data that is the basis for the report
 * match-analysis-report.xlsx. This is the report and sheets that calculate data for the report

Creating a Report
^^^^^^^^^^^^^^^^^
When you have generated the output open both XLSX files. Then go to the match report (match-analysis-report.xlsx). You will be prompted to update links. Select update. Browse to the location where the reports have been generated and select the match-agg-data.gen.xlsx file.

Go to the 'Report' tab. From the menu go to 'File -> Save As'. When prompted select PDF from the file format list and select the 'sheet' radio button just below that. Give the file a name and select 'Save'.

Installation
------------
Requirements
^^^^^^^^^^^^

-  Python 3

Installing
^^^^^^^^^^
Then, install this module from pypi using ``pip3`` :

.. code::

    pip3 install matchreporter

Caveats/Known Issues
--------------------
 * Ensure that you enable content when prompted when you open the report (match-analysis-report)
 * The match report (match-analysis-report.xlsx) has a dependency on the generated data (report-agg-data.xlsx) being opened. This is due to the fact that the data is a linked workbook. Not doing so will mean that the values will not be updated.
 * Attacks in the match-analysis-report.xlsx[MatchANALYSIS] tab are currently hardcoded. Please update should you capture.

Thanks & Credits
----------------
* Many, many thanks to `GAA Apps <http://gaaapps.com/>`__ for creating the mobile Apps and making available for free!
* Thanks to Jonny Bradley `@JohnnyBrad1ey <https://twitter.com/JohnnyBrad1ey>`__ for publishing his original report on which the Excel is based and copied.
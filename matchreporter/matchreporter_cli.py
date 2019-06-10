import sys
import logging
import argparse
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from matchreporter.analysis.analyser import analyse
from matchreporter.collect import scxmlformatter, gaamatchformatter
from matchreporter.communicate.matchreport import createMatchReport
from matchreporter.helpers.filehelper import loadDataFromFile


def parseCommandLine():
    parser = argparse.ArgumentParser()

    parser.add_argument("-gaamatch", help="The full path and filename of export from GAAMatch")
    parser.add_argument("-sc", help="The full path and filename of XML export from SportsCode")
    parser.add_argument("-outputDirectory", help="The report output file name and location")

    args = parser.parse_args()

    return args


def main(argv):
    args = parseCommandLine()

    formattedData = None

    if args.gaamatch is None and args.sc is None:
        exit("Please set the -gaamatch or -sc arguments (full name and path to the list of text events). E.g. python "
             "matchreporter\matchreporter_cli.py 'C:\some_dir\match-events.txt|.xml'")

    elif args.gaamatch is not None and args.sc is not None:
        exit("Please set one of -gaamatch or -sc arguments")

    elif args.gaamatch is not None:
        mobileAppOutput = loadDataFromFile(args.gaamatch)

        formattedData = gaamatchformatter.cleanAndFormatData(mobileAppOutput)
        sportsCodeOutput = False

    elif args.sc is not None:
        formattedData = scxmlformatter.cleanAndFormatData(args.sc)
        sportsCodeOutput = True

    else:
        exit("Please set the -gaamatch or -sc arguments (full name and path to the list of text events). E.g. python "
             "sportscoder\sportscoder_cli.py 'C:\some_dir\match-events.txt|.xml'")


    analysis = analyse(formattedData)

    createMatchReport(args.outputDirectory, analysis, sportsCodeOutput)


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)

    main(sys.argv[1:])

import sys
import logging
import argparse
import os

from matchreporter.analysis.analyser import analyse
from matchreporter.collect import scxmlformatter, gaamatchformatter
from matchreporter.db.analysis_db import write_report_data
from matchreporter.helpers.filehelper import load_data_from_file

SPORTS_CODE = 'SportsCode'

GAA_MATCH = 'GAAMatch'

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


def parse_command_line():
    parser = argparse.ArgumentParser()

    parser.add_argument("-gaamatch", help="The full path and filename of export from GAAMatch")
    parser.add_argument("-sc", help="The full path and filename of XML export from SportsCode")
    parser.add_argument("-outputDirectory", help="The report output file name and location")
    parser.add_argument("-DumpJson", help="Dumps formatted JSON")

    args = parser.parse_args()

    return args


def main(argv):
    args = parse_command_line()

    formatted_data = None
    source = None

    if args.gaamatch is None and args.sc is None:
        sys.exit("Please set the -gaamatch or -sc arguments (full name and path to the list of text events). E.g. python "
             "matchreporter\matchreporter_cli.py 'C:\some_dir\match-events.txt|.xml'")

    elif args.gaamatch is not None and args.sc is not None:
        sys.exit("Please set one of -gaamatch or -sc arguments")

    elif args.gaamatch is not None:
        source = GAA_MATCH

        mobile_app_output = load_data_from_file(args.gaamatch)

        formatted_data = gaamatchformatter.clean_and_format_data(mobile_app_output)

    elif args.sc is not None:
        source = SPORTS_CODE

        formatted_data = scxmlformatter.clean_and_format_data(args.sc)

    else:
        sys.exit("Please set the -gaamatch or -sc arguments (full name and path to the list of text events). E.g. python "
             "sportscoder\sportscoder_cli.py 'C:\some_dir\match-events.txt|.xml'")

    analysis = analyse(formatted_data)

    write_report_data(source, analysis)


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)

    main(sys.argv[1:])

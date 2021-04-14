import os

from matchreporter.constants import EX_GAAMATCH_OUTPUT_AGG_DATA_FILE, EX_GAAMATCH_OUTPUT_REPORT_FILE, \
    EX_OUTPUT_DIRECTORY, GAAMATCH_ANALYSIS_REPORT_TEMPLATE
from matchreporter.helpers.datetimehelper import get_todays_date


def read_file(filename, mode='r'):
    with open(filename, mode) as input_file:
        return input_file.read()


def read_text_file_as_lines(filename):
    return read_file(filename).splitlines()


def load_data_from_file(absolute_file_name):
    return read_text_file_as_lines(absolute_file_name)


def create_output_directory(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)


def create_file_path(filename, output_dir):
    create_output_directory(output_dir)

    return os.path.join(output_dir, filename)


def get_gaa_match_output_excel_filename(teams):
    filename = EX_GAAMATCH_OUTPUT_AGG_DATA_FILE.format(teams[0], teams[1], get_todays_date())

    return filename


def get_output_directory_name(teams):
    dirName = EX_OUTPUT_DIRECTORY.format(teams[0], teams[1], get_todays_date())

    return dirName


def get_gaa_match_report_template_name():
    return os.path.join(os.getcwd(), GAAMATCH_ANALYSIS_REPORT_TEMPLATE)


def get_gaa_match_analysis_report_name(output_directory):
    return os.path.join(output_directory, EX_GAAMATCH_OUTPUT_REPORT_FILE)

import os

from pathlib import Path
from pandas import ExcelWriter


from matchreporter.constants import EX_MATCH_SHEET_NAME, EX_PLAYERS_SHEET_NAME_1, EX_PLAYERS_SHEET_NAME_2, \
    EX_HALVES_SHEET_NAME, EX_LOCATIONS_SHEET_NAME_1, EX_LOCATIONS_SHEET_NAME_2, EX_SECTORS_SHEET_NAME, \
    EX_SECTORS1_SHEET_NAME, EX_SECTORS2_SHEET_NAME, EX_POSSESSIONS_SHEET_NAME, EX_TACKLES_SHEET_NAME, EX_RAW_SHEET_NAME
from matchreporter.helpers.filehelper import get_gaa_match_output_excel_filename, get_output_directory_name, \
    create_file_path, get_gaa_match_report_template_name, get_gaa_match_analysis_report_name


def create_match_report(output_location, analysis, sportscode_output):
    output_filename, output_directory = create_output_filename(output_location, analysis)

    create_generated_data_excel_workbook(output_filename, analysis)

    return generate_report_from_template(output_directory)


def create_generated_data_excel_workbook(absolute_filename, analysis):
    writer = ExcelWriter(absolute_filename)

    analysis.raw.to_excel(writer, sheet_name=EX_RAW_SHEET_NAME)

    analysis.match.to_excel(writer, sheet_name=EX_MATCH_SHEET_NAME)
    analysis.players1.to_excel(writer, sheet_name=EX_PLAYERS_SHEET_NAME_1)
    analysis.players2.to_excel(writer, sheet_name=EX_PLAYERS_SHEET_NAME_2)
    analysis.halves.to_excel(writer, sheet_name=EX_HALVES_SHEET_NAME)
    analysis.sectors.to_excel(writer, sheet_name=EX_SECTORS_SHEET_NAME)
    analysis.sectors1.to_excel(writer, sheet_name=EX_SECTORS1_SHEET_NAME)
    analysis.sectors2.to_excel(writer, sheet_name=EX_SECTORS2_SHEET_NAME)

    if analysis.location1 is not None:
        analysis.location1.to_excel(writer, sheet_name=EX_LOCATIONS_SHEET_NAME_1)

    if analysis.location2 is not None:
        analysis.location2.to_excel(writer, sheet_name=EX_LOCATIONS_SHEET_NAME_2)

    if analysis.possessions is not None:
        analysis.possessions.to_excel(writer, sheet_name=EX_POSSESSIONS_SHEET_NAME)

    if analysis.tackles is not None:
        analysis.tackles.to_excel(writer, sheet_name=EX_TACKLES_SHEET_NAME)

    if analysis.plays is not None:
        analysis.plays.to_excel(writer, sheet_name='playAnalysis')

    writer.save()


def create_output_filename(output_dir, analysis):
    filename = get_gaa_match_output_excel_filename(analysis.teams)

    output_directory_name = create_output_directory(analysis, output_dir)

    absolute_filename = create_file_path(filename, output_directory_name)

    return absolute_filename, output_directory_name


def create_output_directory(analysis, output_dir):
    if output_dir is None:
        output_dir = os.getcwd()

    output_directory_name = os.path.join(output_dir, get_output_directory_name(analysis.teams))

    if os.path.exists(output_directory_name) is False:
        os.mkdir(output_directory_name)

    return output_directory_name


def generate_report_from_template(output_directory):
    template = Path(get_gaa_match_report_template_name())
    report = Path(get_gaa_match_analysis_report_name(output_directory))

    if template is not None:
        report.write_bytes(template.read_bytes())

    return report.as_posix()



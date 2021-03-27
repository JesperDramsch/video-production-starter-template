import os
import re
import shutil


def create_directory(directory_path, directory_name):
    os.makedirs(os.path.join(directory_path, directory_name, ".keep"))

def filter_directories_by(directory_path, matcher):
    directories = []
    for item in os.listdir(directory_path):
        if os.path.isdir(item) and matcher.match(item):
            directories.append(item)
    return directories

def get_tools_prefix_number(directory_path):
    production_matcher = re.compile("[0-9][0-9]+")
    production_directories = filter_directories_by(directory_path, production_matcher)
    return len(production_directories) + 1

def step01_create_tool_directories(directory_path, tools):
    tools_prefix_start_number = get_tools_prefix_number(directory_path)
    folder_formatter = lambda folder_number, tool_name: f'{"{0:0=2d}".format(folder_number)}_{tool_name}'
    for tool in tools:
        create_directory(directory_name, default_folder_formatter(tools_prefix_start_number, tool))
        tools_prefix_number += 1

def main():
    step01_create_tool_directories(os.getcwd(), "{{ cookiecutter.editing_tools }}".split(","))

main()

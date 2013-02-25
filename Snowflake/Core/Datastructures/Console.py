__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


class Console():

    def __init__(self,console_name, image_path, short_name):
        self.console_name = console_name
        self.image_path = image_path
        self.short_name = short_name

    def __repr__(self):
        return self.short_name

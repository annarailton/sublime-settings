"""Taken from

https://github.com/kylebebak/sublime_text_config/blob/master/autoflake.py

"""

import sublime_plugin

import subprocess


class AutoflakeRemoveUnusedImportsCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        subprocess.check_call([
            '/home/railton/miniconda3/bin/autoflake',
            '--in-place',
            '--remove-all-unused-imports',
            self.view.file_name(),
        ])

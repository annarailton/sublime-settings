"""Running cljfmt on Clojure code within Sublime

https://github.com/snoe/node-cljfmt
"""

import sublime_plugin

import subprocess


class RunCljfmt(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        subprocess.check_call([
            '/usr/local/bin/cljfmt',
            self.view.file_name(),
        ])

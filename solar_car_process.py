#!/usr/bin/env python3

import subprocess


class SolarCarProcess:
    
    def __init__(self,path):
        self.path = path
        self.timesRestarted = 0

    def start(self):
        try:
            self.process = subprocess.Popen(self.path, stderr=subprocess.PIPE, universal_newlines=True)
        except OSError:
            raise

    def restart(self):
        try:
            self.process = subprocess.Popen(self.path, stderr=subprocess.PIPE, universal_newlines=True)
            self.timesRestarted += 1
        except OSError:
            raise

    def check_status(self):
        return self.process.poll()
    

#!/usr/bin/env python3
"""
  Title: ADSB Analysis script
Project: General ADSB Analysis
Version: 0.0.1
   Date: May, 2024
 Author: Zach Leffke, KJ4QLP
Comment:
 - Generates all passes and exports a combined CSV file
 - Network Pass version
"""

import math
import string
import time
import sys
import csv
import os
import datetime
from pytz import timezone
import argparse
import subprocess
import yaml, csv, json
import pandas as pd
from skyfield import api as sf
from skyfield.api import load, wgs84

# from utilities import file_utilities as file_utils
# from utilities import sat_utilities as sat_utils



def main():
    """ Main entry point to start the service. """

    startup_ts = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    #--------START Command Line argument parser------------------------------------------------------
    parser = argparse.ArgumentParser(description="Ground Station Network Scheduler",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    cwd = os.getcwd()
    cfg_fp_default = '/'.join([cwd, 'config'])
    cfg = parser.add_argument_group('Configuration File')
    cfg.add_argument('--cfg_path',
                       dest='cfg_path',
                       type=str,
                       default='/'.join([os.getcwd(), 'config']),
                       help="Configuration File Path",
                       action="store")
    cfg.add_argument('--cfg_file',
                       dest='cfg_file',
                       type=str,
                       default="sched_config.yaml",
                       help="Configuration File",
                       action="store")
    args = parser.parse_args()
    #--------END Command Line argument parser------------------------------------------------------
    
        

    sys.exit()

if __name__ == '__main__':
    main()
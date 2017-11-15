#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil

from jinja2 import Environment, PackageLoader

import beppo

OUTPUT_PATH = 'pages_out'

if __name__ == '__main__':
    env = Environment(loader=PackageLoader('beppo', 'templates'))
    template = env.get_template('opkg_filename')

    version_meta = {
        "upstream_version": beppo.__version__,
        "epoch": 1
    }

    if not os.path.isdir(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

    src_filename = template.render(**version_meta).strip()
    tgt_filename = os.path.join(OUTPUT_PATH, os.path.basename(src_filename))
    shutil.copy(src_filename, tgt_filename)

    index_template = env.get_template('index.html')
    index_filename = os.path.join(OUTPUT_PATH, "index.html")
    index_content = {
        "files": [
            dict(filename=os.path.basename(src_filename), description="latest release"),
            dict(filename='flake8_report.txt', description="flake8 report"),
            dict(filename='jshint_report', description="JsHint report"),
        ]
    }

    with open(index_filename, "wb") as target:
        target.write(index_template.render(**index_content))

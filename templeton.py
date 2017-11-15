#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from jinja2 import Environment, PackageLoader

from beppo.defaults import PACKAGE_META, PACKAGE_OUTPUT_PATH

if __name__ == '__main__':
    env = Environment(loader=PackageLoader('beppo', 'templates'))
    control_template = env.get_template('control')
    control_content = control_template.render(**PACKAGE_META)
    control_path = os.path.join(PACKAGE_OUTPUT_PATH, "CONTROL")
    control_file = os.path.join(control_path, "control")

    if not os.path.isdir(PACKAGE_OUTPUT_PATH):
        os.makedirs(PACKAGE_OUTPUT_PATH)

    if not os.path.isdir(control_path):
        os.makedirs(control_path)

    with open(control_file, "wb") as target:
        target.write(control_content)

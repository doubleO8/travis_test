#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from jinja2 import Environment, PackageLoader

from beppo.defaults import PACKAGE_META

if __name__ == '__main__':
    env = Environment(loader=PackageLoader('beppo', 'templates'))
    template = env.get_template('control')

    if not os.path.isdir("pack"):
        os.makedirs("pack")

    if not os.path.isdir("pack/CONTROL"):
        os.makedirs("pack/CONTROL")

    template_content = template.render(**PACKAGE_META)
    with open("pack/CONTROL/control", "wb") as target:
        target.write(template_content)

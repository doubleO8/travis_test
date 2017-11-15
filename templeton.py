#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import beppo
from jinja2 import Environment, PackageLoader

if __name__ == '__main__':
    env = Environment(loader=PackageLoader('beppo', 'templates'))
    template = env.get_template('control')

    version_meta = {
        "upstream_version": beppo.__version__,
        "epoch": 1
    }
    os.makedirs("pack/CONTROL")
    template_content = template.render(**version_meta)
    with open("pack/CONTROL/control", "wb") as target:
        target.write(template_content)

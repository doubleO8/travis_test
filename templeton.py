#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader('beppo', 'templates'))
template = env.get_template('control')

version_meta = {
    "upstream_version": "1.2.3"
}
template_content = template.render(**version_meta)
with open("pack/CONTROL/control", "wb") as target:
    target.write(template_content)

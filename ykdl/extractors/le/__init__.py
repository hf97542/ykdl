#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def get_extractor(url):
    if re.search("live.le", url):
        from . import live as s
    else:
        from . import le as s
    return s.site
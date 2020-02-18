#!/usr/bin/env python3

"""
Plugin hooks

See https://multiqc.info/docs/#hooks
"""

from __future__ import print_function
from pkg_resources import get_distribution
import logging

from multiqc.utils import config


log = logging.getLogger('multiqc')


def before_config():
    my_search_patterns = {
        'multiqc_npm/picard_quality_yield_metrics': {'fn': '*.quality_yield_metrics.txt'}
    }
    config.update_dict(config.sp, my_search_patterns)
    log.info("Expanded search patterns with the following: %s", ",".join(my_search_patterns.keys()))
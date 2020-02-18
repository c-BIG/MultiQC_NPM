#!/usr/bin/env python3

"""
NPMExtraMetrics module
"""

from __future__ import print_function
import logging
import sys

from multiqc.utils import config
from multiqc.modules.base_module import BaseMultiqcModule

from . import npm_picard_QualityYieldMetrics

log = logging.getLogger('multiqc')


class NPMExtraMetrics(BaseMultiqcModule):
    def __init__(self):

        # Halt execution if we've disabled the plugin
        if config.kwargs.get('enable_plugin', False) is True \
               or getattr(config, 'enable_plugin', False) is True:
            log.info("Running with MultiQC NPM plugin")
        else:
            log.info("Skipping MultiQC NPM plugin as not enabled")
            return None

        # Initialise the parent module Class object
        super(NPMExtraMetrics, self).__init__(
            name='NPMExtraMetrics',
            anchor='npm_extra_metrics'
        )

        # Call each submodule and report progress
        n = dict()

        n['npm_picard_QualityYieldMetrics'] = npm_picard_QualityYieldMetrics.parse_reports(self)
        if n['npm_picard_QualityYieldMetrics'] > 0:
            log.info("Found {} npm_picard_QualityYieldMetrics reports".format(n['npm_picard_QualityYieldMetrics']))

        # Exit if we didn't find anything
        if sum(n.values()) == 0:
            raise UserWarning

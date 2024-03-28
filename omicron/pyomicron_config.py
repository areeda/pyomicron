#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: nu:ai:ts=4:sw=4

#
#  Copyright (C) 2024 Joseph Areeda <joseph.areeda@ligo.org>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
Utilities to manage pyomicron configurations and internal default templates
NB: these configurations control the pyomicron program for the generation of condor DAG and submit files.
The omicron configurations that control the trigger generator is separate.
"""

__author__ = 'joseph areeda'
__email__ = 'joseph.areeda@ligo.org'

# Base configurations are shared among the sites
BASE_DEFAULT_CONFIG =\
    """
    # default configuration
    [options]
    config_file_dir = ${HOME}/omicron/online
    verbose = 2
    
    [output]
    archive = False
    
    [process]
    max_chunks_per_job = 4
    max_channels_per_job = 20
    max_online_lookback = 3600
    max_concurrent = 64
    
    [condor]
    no_submit = False
    universe = vanilla
    condor_retry = 2
    condor_accounting_group = ligo.prod.o4.detchar.transient.omicron
    condor_accounting_group_user = joseph.areeda
    condor_request_disk = 50G
    submit_rescue_dag = 0
    executable = omicron
    conda_env =  ligo-omicron-3.10
    use_conda_run = True    
    
    [pipeline]
    skip_omicron = False
    skip_root_merge = False
    skip_hdf5_merge = False
    skip_ligolw_add = False
    skip_gzip = False
    skip_postprocessing = False
    skip_rm = False
    """

# Specific environmental variables by IFO. NB: V1 -> CIT
cit_env =\
"""
    [CIT_ENV]
    ifo = V1
    GWDATAFIND_SERVER=datafind.ldas.cit:80
     
"""


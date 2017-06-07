# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2017)
#
# This file is part of PyOmicron.
#
# PyOmicron is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyOmicron is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyOmicron.  If not, see <http://www.gnu.org/licenses/>.

"""Test logging for Omicron
"""

import unittest

from omicron import log

__author__ = 'Duncan Macleod <duncan.macleod@ligo.org>'


class LogTestCase(unittest.TestCase):

    def test_bold(self):
        self.assertEqual(log.bold('TEST'), '\x1b[1mTEST\x1b[0m')

    def test_color_text(self):
        self.assertEqual(log.color_text('TEST', 'blue'),
                         '\x1b[1;34mTEST\x1b[0m')

    def test_logger(self):
        # create logger
        logger = log.Logger('TEST')
        # fudge a record
        record = logger.makeRecord(logger.name, log.logging.DEBUG, 'FILE', 0,
                                   'test message', (), None, 'FUNC', None)
        # test that the formatter prints the correct thing
        outhandler = logger.handlers[0]
        self.assertRegexpMatches(outhandler.format(record),
                                 '\[\\x1b\[1mTEST\\x1b\[0m \d+\]    '
                                 '\\x1b\[1;34mDEBUG\\x1b\[0m: test message')
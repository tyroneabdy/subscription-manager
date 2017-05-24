# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

# Copyright (c) 2017 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import six
import rhsm.i18n_utils as p


class I18nUtilsTest(unittest.TestCase):
    def setUp(self):
        self.byte_data = b"ℙython"
        self.unicode_data = u"ℙython"

    def test_safe_encode_with_bytes(self):
        # running .encode on bytes redundant and hazard fraught in Python 2.  Python 2 tries to decode the
        # bytes then re-encode them instead of doing nothing.  The safe_encode function should prevent that.
        if six.PY2:
            with self.assertRaises(UnicodeDecodeError):
                self.byte_data.encode("utf8")
        self.assertEqual(self.byte_data, p.safe_encode(self.byte_data))

    def test_safe_encode_with_unicode(self):
        self.assertEqual(self.byte_data, self.unicode_data.encode("utf8"))
        self.assertEqual(self.byte_data, p.safe_encode(self.unicode_data))

    def test_safe_decode_with_bytes(self):
        self.assertEqual(self.unicode_data, self.byte_data.decode("utf8"))
        self.assertEqual(self.unicode_data, p.safe_decode(self.byte_data))

    def test_safe_decode_with_unicode(self):
        # Similar to the test_safe_encode_with_bytes test, running decode on a unicode string is redundant and
        # will generally cause an error in Python 2 when Python tries to re-encode the bytes in the system
        # default encoding (ASCII) so it can decode them again.
        if six.PY2:
            with self.assertRaises(UnicodeEncodeError):
                self.unicode_data.decode("utf8")
        self.assertEqual(self.unicode_data, p.safe_decode(self.unicode_data))

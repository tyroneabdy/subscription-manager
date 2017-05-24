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
import six


def out(*args, **kwargs):
    """Basic function to encode unicode to utf8 at the last possible instant."""
    encoding = kwargs.get('encoding', 'utf8')
    if 'encoding' in kwargs:
        del kwargs['encoding']

    if six.PY2:
        output = [safe_encode(x, encoding) for x in args]
        print(*output, **kwargs)
    else:
        print(*args, **kwargs)


def safe_decode(data, encoding="utf8"):
    """
    Perform a decode that will succeed even if the data is already decoded.

    Watch http://pyvideo.org/pycon-us-2012/pragmatic-unicode-or-how-do-i-stop-the-pain.html if these
    functions don't make much sense to you.

    But here's the quick overview.

    byte data is just raw bytes while unicode data is more abstract, a sequence of codepoints.

    unicode_data.encode('utf8') yields byte data
    byte_data.decode('utf8') yields unicode data

    Python 2 allows you to run decode on unicode data and encode on byte data even though that makes no sense.
    As an additional insult, Python 2 tries to convert between unicode data and byte data when you make one of
    these nonsensical calls.  So

        u"ℙython".decode('utf8')

    should just be a no-op; the data is already decoded.  Python 2 converts this to

        u"ℙython".encode(sys.getdefaultencoding()).decode('utf8')

    The default encoding for Python is ASCII and cannot be changed without some unholy magic.  So Python tries
    to encode that unicode data into ASCII which is can't do and throws a UnicodeEncodeError which doesn't
    make any damn sense to the programmer since you never asked it to do any encoding at all.

    This method is written so that you can call decode on something that's already decoded without
    everything going sideways.  It should be performed as soon as possible after reading in text.
    """
    if isinstance(data, six.text_type):
        # text_type is str in Python 3 and unicode in Python 2.  No need to do anything; text is already
        # decoded.
        return data
    elif isinstance(data, six.string_types):
        # string_types is basestring() in Python 2 and str in Python 3 but we know from the earlier if
        # statement that text is not unicode so we decode it.
        return data.decode(encoding)
    elif six.PY2:
        # At this point we must have something that's not a string of any type, so call the appropriate method
        # depending on the Python version
        return unicode(data)
    else:
        return str(data)


def safe_encode(data, encoding="utf8"):
    """Similar to safe_decode, this method only encodes things that are not already encoded.  Turns unicode
    into bytes using the specified encoding.  This method should be called as late as possible: right
    before data is due to be output."""
    if isinstance(data, six.text_type):
        return data.encode(encoding)
    elif isinstance(data, six.string_types):
        return data
    else:
        return six.b(data)

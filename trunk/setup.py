# Copyright (c) 2006 L. C. Rees.  All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1.  Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# 2.  Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 3.  Neither the name of the Portable Site Information Project nor the names
# of its contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

'''setup - setuptools based setup for multishove.'''

import ez_setup
ez_setup.use_setuptools()

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(name='multishove',
version='0.1',
description='''Simultaneous storage of objects in multiple storage backends.''',
long_description='''Stores objects in multiple storage backends simultaneously
with dictionary-style access, caching, and object serialization and compression.

Currently supported storage backends are:

* Amazon S3 Web Service
* Berkeley Source Database
* Memory
* Filesystem
* Firebird
* FTP
* DBM
* Durus
* Microsoft SQL Server
* MySQL
* Oracle
* PostgreSQL
* SQLite
* Subversion
* Zope Object Database (ZODB)

Currently supported caching backends are:

* Memory
* Filesystem
* Firebird
* memcache
* Microsoft SQL Server
* MySQL
* Oracle
* PostgreSQL
* SQLite

The use of multiple backends for storage involves
passing multiple store URIs or instances to
multishove following the form:

from multishove import MultiShove

<storename> = MultiShove(<store_uri1>, <store_uri2> ..., cache=<cache_uri>)

multishove implements the Python dictionary/mapping API:

http://docs.python.org/lib/typesmapping.html

multishove requires the shove package from:

http://cheeseshop.python.org/pypi/shove''',
      author='L. C. Rees',
      author_email='lcrees@gmail.com',
      license='BSD',
      packages = ['multishove', 'multishove.tests'],
      test_suite='multishove.tests',
      zip_safe = True,
      keywords='object storage persistence database shelve',
      classifiers=['Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Database :: Front-Ends'],
    install_requires = ['shove'])
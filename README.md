Stores objects in multiple storage backends simultaneously with dictionary-style access, caching, and object serialization and compression.

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

The use of multiple backends for storage involves passing multiple store URIs or instances to multishove following the form::

    from multishove import MultiShove

    <storename> = MultiShove(<store_uri1>, <store_uri2> ..., cache=<cache_uri>)

multishove implements the Python dictionary/mapping API:

http://docs.python.org/lib/typesmapping.html

multishove requires the shove package from:

http://cheeseshop.python.org/pypi/shove
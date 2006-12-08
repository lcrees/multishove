# Copyright (c) 2006 L. C. Rees
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#    
#    2. Redistributions in binary form must reproduce the above copyright 
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#    3. Neither the name of Django nor the names of its contributors may be used
#       to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''Common frontend for multiple object stores.''' 

from shove import Shove, getbackend 

__all__ = ['MultiShove']
    
  
class MultiShove(Shove):

    '''Common frontend for multiple object stores.'''
    
    def __init__(self, *a, **kw):
        cache = kw.get('cache', 'simple://')
        # Init superclass wi
        super(Shove, self).__init__(a[0], cache, **kw)
        # Delete single store instance
        del self._store
        # Load stores
        stores = tuple(getbackend(i, stores, **kw) for i in a)
        
    def __getitem__(self, key):
        '''Gets a item from shove.'''
        try:
            return self._cache[key]
        except KeyError:
            # Synchronize cache and store
            self.sync()
            value = self._stores[0][key]
            self._cache[key] = value
            return value

    def __delitem__(self, key):
        '''Deletes an item from multiple stores.'''
        try:
            del self._cache[key]
        except KeyError: pass
        self.sync()
        for store in self._stores: del self.store[key]

    def keys(self):
        '''Returns a list of keys in shove.'''
        self.sync()
        return self._stores[0].keys()

    def sync(self):
        '''Writes buffer to store.'''
        for k, v in self._buffer.iteritems():
            for store in self._stores: store[k] = v
        self._buffer.clear()
        
    def close(self):
        '''Finalizes and closes shove stores.'''
        # If close has been called, pass
        if self._store is not None:
            self.sync()
            for store in self._stores:
                store.close()
                store = None
            self._store = self._cache = self._buffer = None
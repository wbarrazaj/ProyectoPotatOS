#!/usr/bin/env python

# Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
A clone of 'free' cmdline utility.
"""

from unittest import FunctionTestCase
import psutil
from modulos.funciones import print_ , bytes2human , printlog

def main():
    virt = psutil.virtual_memory()
    swap = psutil.swap_memory()
    templ = "%-7s %10s %10s %10s %10s %10s %10s"
    print_(templ % ('', 'total', 'used', 'free', 'shared', 'buffers', 'cache'))
    print_(templ % ('Mem:', int(virt.total / 1024),
                            int(virt.used / 1024),
                            int(virt.free / 1024),
                            int(getattr(virt, 'shared', 0) / 1024),
                            int(getattr(virt, 'buffers', 0) / 1024),
                            int(getattr(virt, 'cached', 0) / 1024)))
    print_(templ % ('Swap:', int(swap.total / 1024),
                             int(swap.used / 1024),
                             int(swap.free / 1024),
                             '', '', ''))

if __name__ == '__main__':
    main()
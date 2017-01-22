#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pass

def build():
    pass

def install():
    shelltools.system("bash %s/RosBE-Unix-2.1.2/RosBE-Builder.sh" %get.workDIR())


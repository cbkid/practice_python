#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""docstring
"""

__revision__ = '0.1'

import gtk
class TreeViewEaxmple(object):
    """docstring for TreeViewEaxmple"""
    def __init__(self,  ):
        super(TreeViewEaxmple, self).__init__()
        self.counter = 0
        self.win = gtk.Window()
        self.win.set_size_request(400, 400)
        self.win.connect("clicked", self.add_button_clicked)
        remove_button = gtl.

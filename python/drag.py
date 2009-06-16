#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""docstring
"""

__revision__ = '0.1'

import pygtk
import gtk
import sys
import os

class DragDropExample(object):
    """docstring for DragDropExample"""
    def __init__(self,  ):
        TARGET_STRING = 82
        TARGET_IMAGE = 83
        self.file_list = []
        self.accepted_types = ["jpg", "jpeg", "png", "gif", "bmp"]

        win = gtk.Window()
        win.set_size_request(400, 400)
        win.connect("delete_event", lambda w,e: gtk.mainquit())

        vbox = gtk.VBox(False, 0)
        hello = gtk.Label("Test label to drag images to.")
        vbox.pack_start(hello, True, True, 0)
        win.add(vbox)

        if sys.platform=="win32":
            win.drag_dest_set(0, [], 0)
        else:
            win.drag_dest_set(gtk.DEST_DEFAULT_DROP, 
                    [("text/plain", 0, TARGET_STRING),
                        ("image/*", 0, TARGET_IMAGE)],
                    gtk.gdk.ACTION_COPY)

        win.connect("drag_motion", self.motion_cb)
        win.connect("drag_drop", self.drop_cb)
        win.connect("drag_data_received", self.drag_data_received)
        win.show_all()

    def motion_cb(self, wid, context, x, y, time):
        context.drag_status(gtk.gdk.ACTION_COPY, time)
        return True
    def drop_cb(self, wid, context, x, y, time):
        print "drop"
        if context.targets:
            wid.drag_get_data(context, context.targets[0], time)
            print "".join([str(t) for t in context.targets])
            return True
        return False

    def drag_data_received(self, img, context, x, y, data, info, time):
        if data.format == 8:
            print "Received %s" % data.data

        test_data = os.path.splitext(data.data)[1][1:4].lower().strip()
        if test_data in self.accepted_types:
            if sys.platform=="win32":
                self.file_list.append(data.data[8:])
                print data.data[8:]
            else:
                self.file_list.append(data.data[7:])
                print data.data[7:]
            context.finish(True, False, time)
        else:
            context.finish(False, False, time)

if __name__ == '__main__':
    DragDropExample()
    gtk.main()

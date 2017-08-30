#!/usr/bin/env python3
#    oceanlib    -    a collection of tools to help make Gtk. application developement easier
#    Copyright (C) 2017  Michael Connor Buchan
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#import the gi modual to check if we have a suitable version of Gtk.
import gi
#require Gtk. 3.0 or later
gi.require_version('Gtk','3.0')
#we now know that we have a suitable version, so import the Gtk modual from gi.repository
from gi.repository import Gtk

#create a class called assistant to assist the user in achieving a particular task
class Assistant(Gtk.Window):
    def __init__(self,title="Assistant",init_sub_title="",pages=[]):
        Gtk.Window.__init__(self,title=title)
        self.set_default_size(520,480)
        self.set_border_width(10)
        self.header = Gtk.HeaderBar()
        self.header.set_show_close_button(True)
        self.header.set_title(title)
        self.header.set_subtitle(init_sub_title)
        self.set_titlebar(self.header)
        self.create_nav_buttons()
        self.create_notebook()
        self.launch()
    
    def launch(self):
        self.connect("destroy",Gtk.main_quit)
        self.show_all()
        Gtk.main()
    
    def create_nav_buttons(self):
        self.back_forward = Gtk.HBox()
        Gtk.StyleContext.add_class(self.back_forward.get_style_context(),"linked")
        self.header.pack_start(self.back_forward)
        self.back_button = Gtk.Button()
        self.back_button.add(Gtk.Arrow(Gtk.ArrowType.LEFT))
        self.back_label = Gtk.Label()
        self.back_label.set_text_with_mnemonic("_back")
        self.back_label.set_mnemonic_widget(self.back_button)
        self.back_label.set_visible(False)
        self.back_button.add(self.back_label)
        self.back_forward.pack_start(self.back_button,False,False,0)
        self.forward_button = Gtk.Button()
        self.forward_button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT))
        self.forward_label = Gtk.Label()
        self.forward_label.set_text_with_mnemonic("_next")
        self.forward_label.set_mnemonic_widget(self.forward_button)
        self.forward_label.set_visible(False)
        self.forward_button.add(self.forward_label)
        self.back_forward.pack_start(self.forward_button,False,False,0)
    
    def create_notebook(self):
        self.notebook = Gtk.Notebook()
        self.notebook.set_show_tabs(False)
        
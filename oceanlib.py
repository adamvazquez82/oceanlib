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
    #define the initialisation function to initialise the window and add the widgets
    def __init__(self,title="Assistant",init_sub_title="",page_names=[],pages=[]):
        #call the super class's constructor
        Gtk.Window.__init__(self,title=title)
        #set the pages property of this class to the pages argument passed to the constructor (if any)
        self.pages = pages
        #set the names property of this class to the page_names argument passed to the constructor (if any)
        self.names = page_names
        #start the current_page variable at 0 by default
        self.current_page = 0
        #define a default size for the window
        self.set_default_size(520,480)
        #set a border width of 10 so that items are spaced correctly
        self.set_border_width(10)
        #define the new titlebar using the Gtk.HeaderBar object
        self.header = Gtk.HeaderBar()
        #make sure that the title bar contains a close button
        self.header.set_show_close_button(True)
        #set the title of the titlebar to match the window title
        self.header.set_title(title)
        #set the initial sub title of the assistant (this may change depending on what page is showing)
        self.header.set_subtitle(init_sub_title)
        #make the new title bar active by setting the window's title bar to it
        self.set_titlebar(self.header)
        #create a function to create the navigation buttons on the Gtk.HeaderBar
        self.create_nav_buttons()
        #create the Gtk.Notebook to act as the main container for the content
        self.create_notebook()
        #run final cleanup and launch the window
        self.launch()
    
    #define the launch function to prepare and show the window's contents
    def launch(self):
        #connect the Gtk.main_quit function to the delete-event event so that the application will terminate when the close button is clicked
        self.connect("destroy",Gtk.main_quit)
        #show all of the window's contents
        self.show_all()
        #run the main Gtk loop
        Gtk.main()
    
    #define a function to create the navigation buttons for moving through the assistant's pages
    def create_nav_buttons(self):
        #create a main container (a horrizontal box) for the 2 buttons to be placed in
        self.back_forward = Gtk.HBox()
        #change the style context of the box so that the buttons appear to be linked
        Gtk.StyleContext.add_class(self.back_forward.get_style_context(),"linked")
        #pack the box into the title bar
        self.header.pack_start(self.back_forward)
        #create the back button to navigate backwards
        self.back_button = Gtk.Button()
        #connect the back button to the change_page function, passing -1 as the number of pages to change so that we go back 1 page
        self.back_button.connect("clicked",self.change_page,-1)
        #add a Gtk.Arrow to the button to symbolise moving backwards
        self.back_button.add(Gtk.Arrow(Gtk.ArrowType.LEFT))
        #define a back_label to be used to activate the button based on a mnemonic. This is also used to give screen readers a description of what the button does
        self.back_label = Gtk.Label()
        #change the text of the label to "back", making `b' the mnemonic char
        self.back_label.set_text_with_mnemonic("_back")
        #set the widget to activate when the mnemonic is used to be the back_button
        self.back_label.set_mnemonic_widget(self.back_button)
        #finally, pack the back_button object into the back_forward box
        self.back_forward.pack_start(self.back_button,False,False,0)
        #define the forward_button
        self.forward_button = Gtk.Button()
        #connect the forward button to the change_page function
        self.forward_button.connect("clicked",self.change_page,1)
        #add an arrow to it
        self.forward_button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT))
        #define the forward_label
        self.forward_label = Gtk.Label()
        #set the text of the forward_label, making sure that a mnemoni is used so that the forward button can be activated
        self.forward_label.set_text_with_mnemonic("_next")
        #set the mnemonic widget (widget to be activated) by the forward_label
        self.forward_label.set_mnemonic_widget(self.forward_button)
        self.forward_label.set_visible(False)
        #pack the forward button into the back_forward box
        self.back_forward.pack_start(self.forward_button,False,False,0)
    
    #define a function to to create a Gtk.Notebook object, set some of it's properties, add all of the pages in the self.pages list (if any) and finally add the notebook to the main window
    def create_notebook(self):
        #create the Gtk.Notebook object for storing and switching between pages
        self.notebook = Gtk.Notebook()
        #make the notebook tabs invisible (we will control the navigation of the notebook through the navigation buttons instead)
        self.notebook.set_show_tabs(False)
        #loop through the pages passed as input to the constructer (if any) and append them to the notebook
        if len(self.names) >0 and len(self.pages) > 0:
            for i in range(0,len(self.names)-1):
                self.notebook.append_page(self.pages[i],Gtk.Label(self.names[i]))
        #add the self.notebook object to the main window
        self.add(self.notebook)
    
    #define a function to go forward or back to a specific page
    def change_page(self,widget,num=1):
        self.current_page += num
        self.notebook.set_current_page(self.current_page)
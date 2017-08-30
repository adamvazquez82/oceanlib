# oceanlib ## a collection of classes to make PyGObject application
developement easier and to simplify complicated gtk tasks

### Introduction

  The oceanlib library, originally created by Michael Connor Buchan, is
  a python modual to help make certain tasks in Python GTK+3 (PyGObject)
  easier to achieve. It contains many classes that create various widgets
  and UI elements, making it easier for starting developers to get into
  GTK without jumping in over their head.

### Implemented Classes

* oceanlib.Assistant    -    a class to create  an application that
assists the user to achieve a particular task, for example, setting up a
printer. The assistant has a moddern UI and uses client side decorations,
placing the back, forward and cancel (close) buttons in the titlebar as
well as the name of the assistatnt and the title of the current step

### Not Yet Implemented

* ShareDialog    -    a Gtk.PopOver object to share text, images and/or
multi-media with-in a PyGObject application. This also supports plug-ins
so that sharing services can be added in the future * StickyNote    -
a Gtk.Box widget to take and store simple sticky notes/postit notes on
your desktop or in any application

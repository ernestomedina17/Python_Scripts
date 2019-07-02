import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class AlertWindow(Gtk.Window):

    def __init__(self, uberconfURL):
        Gtk.Window.__init__(self, title="Meeting Alert")
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="warning.png", width=30, height=30, preserve_aspect_ratio=True)

        self.set_default_size(240, 100)
        self.uberconfURL = uberconfURL
        self.box = Gtk.Box(orientation=1, spacing=6)
        self.image = Gtk.Image.new_from_pixbuf(pixbuf)
        self.label = Gtk.Label(label="Please join the meeting")
        self.url = Gtk.LinkButton(uri=self.uberconfURL, label="Link")

        self.add(self.box)

        self.box.pack_start(self.image, True, True, 0)
        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.url, True, True, 0)



aw = AlertWindow("https://uberconference.com/YOUR_ID_HERE")
aw.connect("destroy", Gtk.main_quit)
aw.show_all()
Gtk.main()





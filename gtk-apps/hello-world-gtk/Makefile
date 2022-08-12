build:
	cc `pkg-config --cflags gtk4` -o hello-world-gtk src/hello-world-gtk.c `pkg-config --libs gtk4`

install:
	cp hello-world-gtk /usr/bin
	cp src/org.gtk.example.desktop /usr/share/applications

uninstall:
	rm /usr/bin/hello-world-gtk
	rm /usr/share/applications/org.gtk.example.desktop

clean:
	rm -f hello-world-gtk

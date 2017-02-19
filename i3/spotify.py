#!/usr/bin/env python
# -*- coding:utf-8 -*-

import dbus
try:
	bus = dbus.SessionBus()
	spotify = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
	spotify_iface = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')
	props = spotify_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
	output = str(props['xesam:artist'][0]) + " - " + str(props['xesam:title'])
	print(output)
	exit
except dbus.exceptions.DBusException:
	exit

#!/bin/sh
MAJOR=$(curl -L https://ftp.gnome.org/pub/GNOME/sources/pango/ 2>/dev/null |grep href= |sed -e 's,.*href=",,;s,".*,,' |grep '/$' |sed -e 's,/$,,' |sort -V |grep -v 1.90 |tail -n1)
curl -L https://ftp.gnome.org/pub/GNOME/sources/pango/$MAJOR/ 2>/dev/null |grep href= |sed -e 's,.*href=",,;s,".*,,' |grep -E '^pango-.*\.tar\.xz' |sed -e 's,^pango-,,;s,\.tar\.xz,,' |sort -V |tail -n1

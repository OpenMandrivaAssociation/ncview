#!/bin/sh
curl ftp://cirrus.ucsd.edu/pub/ncview/ 2>/dev/null |awk '{ print $9; }' |grep -E 'ncview-[0-9\.]*\.tar' |sed -e 's,.*ncview-,,;s,\.tar.*,,' |sort -V |tail -n1

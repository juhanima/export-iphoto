#!/bin/env python
# Extract images out from an iPhone backup by using the
# iTunes backup

import os, re, sys, apsw, plistlib, datetime, shutil

def main(edir):
    if not os.path.exists(edir):
        os.mkdir(edir)
    sqlite_con = apsw.Connection("./Manifest.db")
    sqlite_cur = sqlite_con.cursor()
    for fi, rp, prop in sqlite_cur.execute(
            "SELECT fileID, relativePath, file"
            " FROM Files"
            " WHERE domain = 'CameraRollDomain'"
            " AND flags = 1"
            " AND relativePath LIKE 'Media/DCIM/%'"
            " ORDER BY relativePath"):
        p = plistlib.loads(prop, fmt=plistlib.FMT_BINARY)
        o = p["$objects"]
        fsize = 0
        for x in o:
            if type(x) is dict and 'Birth' in x:
                stamp = datetime.datetime.fromtimestamp(x["Birth"])
                fsize  = x["Size"]
                break
        if 0 < fsize:
            sname = fi[:2] + '/' + fi
            (_, tname) = os.path.split(rp)
            tdir = edir + '/' + stamp.strftime("%Y-%m")
            if not os.path.isdir(tdir):
                if not os.path.exists(tdir):
                    os.mkdir(tdir)
                else:
                    raise("ERROR: %s exists already but is not a directory" % tdir)

            tname = tdir + '/' + tname
            if not os.path.exists(tname):
                try:
                    print("%s -> %s" % (sname, tname))
                    shutil.copyfile(sname, tname)
                except:
                    print("Could not copy '%s'" % sname)

            if os.path.exists(tname):
                st = os.stat(tname)
                if st.st_size != fsize:
                    print("%s is not right size (%d != %d)" % (tname, st.st_size, fsize))
                else:
                    # print("%s OK" % (tname))
                    pass

        # print("%s: %20s" % (fi, rp))

    sqlite_cur.close()
    sqlite_con.close()


if "__main__" == __name__:
    if 1 < len(sys.argv):
        edir = sys.argv[1]
    else:
        edir = "./DCIM"
    sys.exit(main(edir))

# export-iphoto
A little iPhone photo extractor utility

## Rationale

Getting photos out of an iPhone can be a little tedious through iCloud if there are a lot of them. Making a backup by iTunes is one option but then the pictures are among everything else named by hashes without any order. Newer Windows versions also support importing pictures directly to the Photos app, but that seems to be unreliable and work poorly. 

This little python script can be run in the iTunes backup directory (Apple/MobileSync/Backup/XXXX) to copy all of the pictures into a given target directory (for instance D: for a removable memory device) grouped by directories of format Year/Month. It doesn't modify the backup in any way.

## Running

The command requires python and the `apsw` module for SQLite3 database handling. Use `pip -r requirements.txt` to install the necessary libraries. The following command copies all of the pictures to the D: drive.

```
C:\> python export-iphoto.py D:
```

## Converting HIEC to JPG

Assuming the USB-stick is mounted to Linux, imagemagick and bash make it easy

```
$ for x in `find /mnt/d -type f -name \*.HIEC` ; do convert $x ${x/.HIEC/.JPG} ; done

# export-iphoto
A little iPhone photo extractor utility

## Rationale

Getting photos out of an iPhone can be a little tedious through iCloud if there are a lot of them. Making a backup by iTunes is one option but then the pictures are among everything else named by hashes without any order. Newer Windows versions also support importing pictures directly to the Photos app, but that seems to be unreliable and work poorly. 

This little python script can be run in the iTunes backup directory (Apple/MobileSync/Backup/XXXX) to copy all of the pictures into a given target directory (for instance D: for a removable memory device) grouped by directories of format Year/Month. It doesn't modify the backup in any way.

## Running

The command requires python and the `apsw` module for SQLite3 database handling. Use `pip -r requirements.txt` to install the necessary libraries. The command examples here are for the Windows operating system. 

The following command copies all of the pictures to the D: drive, provided that it is run in the directory where the `Manifest.db` file is in (Usually something like `C:\User\<user-id>\Apple\MobileSync\Backup\XXXX-YYYY...\`)

```
C:Apple\MobileSync\Backup\XXX-YYY> python c:\github\export-iphoto\export-iphoto.py D:
88/88364a06cc67476b547dddf7e49cf792cc272b55 -> D:/2021-12/IMG_0340.HEIC
e7/e75e56c401382cd3416670b9ff9c80ed3051d26c -> D:/2021-12/IMG_0340.MOV
2a/2a80f78bf909e2c5c978704ec323076493745217 -> D:/2021-12/IMG_0341.HEIC
f7/f79b91dd3154bff188a27609dcc773d673a9de7f -> D:/2021-12/IMG_0341.MOV
31/316b6d9a22e45b4124b84418ece194316bbed977 -> D:/2021-12/IMG_0342.HEIC
73/736c8ef2311716991927205de1cc6a0b7a5928b1 -> D:/2021-12/IMG_0342.MOV
34/34358315bdd9e3bd3f2c85d68876c1aacccc7c60 -> D:/2021-12/IMG_0343.HEIC
...
```

## Converting HEIC to JPG

Assuming the USB-stick is mounted to Linux, imagemagick and bash make it easy

```
$ for x in `find /mnt/d -type f -name \*.HEIC` ; do echo $x ; convert $x ${x/.HEIC/.JPG} ; done
```

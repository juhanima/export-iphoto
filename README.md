# export-iphoto
A little iPhone photo extractor utility

## Rationale

Getting photos out of an iPhone can be a little tedious through iCloud if there are a lot of them.
Making a backup by iTunes is one option but then the pictures are among everything else named by hashes without any order.

This little python script can be run in the iTunes backup directory (Apple/MobileSync/Backup/XXXX) and it copies all of the pictures into a given target directory (for instance D: for a removable memory device) grouped by directories of format Year/Month.

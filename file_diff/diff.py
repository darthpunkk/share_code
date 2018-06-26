import sys
import difflib

if len(sys.argv) != 3:
    print "provide filenames along with paths of 2 files"
    sys.exit(1)

file1 = str(sys.argv[1])
file2 = str(sys.argv[2])
with open(file1,'r') as f1, open(file2,'r') as f2:
    diff=list(difflib.unified_diff(f1.readlines(),f2.readlines(),fromfile=file1,tofile=file2))
    for item in diff:
        if item.startswith('+') or item.startswith('-'):
            print item,

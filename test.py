import plistlib as plist
import checker as c

#fpath = input("Please drag and drop the path to the plist here: ").removesuffix("'").removeprefix("'")
fpath1 = "/Users/marek/Downloads/config.plist"

file1 = open(fpath1,'rb')


parsed = plist.load(file1)

c.check(parsed)

print("success! end.\n")
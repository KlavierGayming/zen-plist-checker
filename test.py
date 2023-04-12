import plistlib as plist
import checker as c

fpath = input("Please drag and drop the path to the plist here: ").removesuffix("'").removeprefix("'")
parsed = {}

with open(fpath,'rb') as file:
    parsed = plist.load(file)

c.check(parsed)


print("success! end.\n")
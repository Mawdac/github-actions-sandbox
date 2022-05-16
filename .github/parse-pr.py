import sys

prstring = sys.argv.pop(1)

mylist = prstring.split("\\n")
mylist = list(filter(('---').__ne__, mylist))

markdown = ''

while mylist != []:
  markdown += ':pencil: <' + mylist[1] + '|' + mylist[0] + '>'
  mylist.pop(0)
  mylist.pop(0)
  if mylist != []: markdown += '\\n\\n'

print(markdown)
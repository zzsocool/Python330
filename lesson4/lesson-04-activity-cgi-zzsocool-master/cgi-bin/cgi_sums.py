#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()
form = cgi.FieldStorage()
try:
    listval = form.getlist('operand')
    total = sum(map(int, listval))
    body = f'Your total is {total}'
except(ValueError, TypeError):
    body = "Unable to calculate a sum: please provide integer number."
print(body)
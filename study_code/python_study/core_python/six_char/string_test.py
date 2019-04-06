from string import Template
s = Template('There ate ${howmany} ${lang} quotation symbols')

print(s.substitute(lang='Python', howmany='3'))

# print(s.substitute(lang='python'))
print(s.safe_substitute(lang='python'))
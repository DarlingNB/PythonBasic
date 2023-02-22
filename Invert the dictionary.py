d = {
  'apple': ['malum', 'pomum', 'popula'],
  'fruit': ['baca', 'bacca', 'popum'],
  'punishment': ['malum', 'multa']
}

d2 = {}

for key,val in d.items():
    for word in val:
      d2[word] = d2.get(word, []) + [key]

print(d2)











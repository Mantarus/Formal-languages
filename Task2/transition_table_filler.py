table = open('table.txt', 'w', encoding='utf-8')

# Transitions from empty state

table.write('Empty . st1\n')

for x in '+-':
    table.write('Empty {} st2\n'.format(x))

for x in '0123456789':
    table.write('Empty {} st3\n'.format(x))

# Transitions from st1

for x in '0123456789':
    table.write('st1 {} st4\n'.format(x))

# Transitions from st2

for x in '0123456789':
    table.write('st2 {} st3\n'.format(x))

table.write('st2 . st1\n')

# Transitions from st3

for x in '0123456789':
    table.write('st3 {} st3\n'.format(x))

table.write('st3 . st5\n')

for x in 'eE':
    table.write('st3 {} st6\n'.format(x))

# Transitions from st4

for x in '0123456789':
    table.write('st4 {} st4\n'.format(x))

for x in 'eE':
    table.write('st4 {} st6\n'.format(x))

# Transitions from st5

for x in '0123456789':
    table.write('st5 {} st4\n'.format(x))

for x in 'eE':
    table.write('st5 {} st6\n'.format(x))

# Transitions from st6

for x in '0123456789':
    table.write('st6 {} st8\n'.format(x))

for x in '+-':
    table.write('st6 {} st7\n'.format(x))

# Transitions from st7

for x in '0123456789':
    table.write('st7 {} st8\n'.format(x))

# Transitions from st8

for x in '0123456789':
    table.write('st8 {} st8\n'.format(x))

# Close file
table.close()
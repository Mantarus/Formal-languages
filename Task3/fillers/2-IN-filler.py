digits = '0123456789'

# Alphabet        : nums
print('# Alphabet')
print(' '.join(digits))

# States          : empty num
print('# States')
print('empty num')

# Init states      : empty
print('# Init states')
print('empty')

# Final states     : num
print('# Final states')
print('num')

# Transition table
print('# Transition table')

for x in digits:
    print('empty {} num'.format(x))

for x in digits:
    print('num {} num'.format(x))

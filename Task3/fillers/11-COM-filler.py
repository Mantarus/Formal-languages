alph_without_ast = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-_/={}[]()'
whitespace = ''
asterisk = '*'

# Alphabet        : letters, digits, _
print('# Alphabet')
print(' '.join(letters + digits + underscore))

# States          : empty first_sym sym
print('# States')
print('empty first_sym sym')

# Init states      : empty
print('# Init states')
print('empty')

# Final states     : first_sym sym
print('# Final states')
print('first_sym sym')

# Transition table
print('# Transition table')

for x in letters + underscore:
    print('empty {} first_sym'.format(x))

for x in letters + digits + underscore:
    print('first_sym {} sym'.format(x))

for x in letters + digits + underscore:
    print('sym {} sym'.format(x))
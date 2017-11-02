alph_without_ast = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-_/={}[]()<>,.;:!@#$%^&?'
alph_without_rb = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-_/={}[](<>,.;:!@#$%^&?*'
alph_without_rb_ast = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-_/={}[](<>,.;:!@#$%^&?'
ws = 'whitespace'

print('# Alphabet')
print(' '.join(alph_without_ast + '*'), ws)

# States          : empty lb lb_a sym sym_a a_rb
print('# States')
print('empty lb lb_a sym sym_a a_rb')

# Init states      : empty
print('# Init states')
print('empty')

# Final states     : a_rb
print('# Final states')
print('a_rb')

# Transition table
print('# Transition table')

print('empty ( lb')

print('lb * lb_a')

print('lb_a * sym_a')

for x in alph_without_ast:
    print('lb_a {} sym'.format(x))
print('lb_a {} sym'.format(ws))

for x in alph_without_ast:
    print('sym {} sym'.format(x))
print('sym {} sym'.format(ws))

print('sym * sym_a')

for x in alph_without_rb_ast:
    print('sym_a {} sym'.format(x))
print('sym_a {} sym'.format(ws))

print('sym_a * sym_a')

print('sym_a ) a_rb')
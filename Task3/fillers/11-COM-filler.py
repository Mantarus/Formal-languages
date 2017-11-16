alph_without_ast = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-_/={}[]()<>,.;:!@#$%^&?'
alph_without_rb = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-_/={}[](<>,.;:!@#$%^&?*'
alph_without_rb_ast = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-_/={}[](<>,.;:!@#$%^&?'
ws = 'whitespace'
lb = '\\n'
cr = '\\r'
t = '\\t'

print('# Alphabet')
print(' '.join(alph_without_ast + '*'), ws, lb, cr, t)

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
print('lb_a {} sym'.format(lb))
print('lb_a {} sym'.format(cr))
print('lb_a {} sym'.format(t))

for x in alph_without_ast:
    print('sym {} sym'.format(x))
print('sym {} sym'.format(ws))
print('sym {} sym'.format(lb))
print('sym {} sym'.format(cr))
print('sym {} sym'.format(t))

print('sym * sym_a')

for x in alph_without_rb_ast:
    print('sym_a {} sym'.format(x))
print('sym_a {} sym'.format(ws))
print('sym_a {} sym'.format(lb))
print('sym_a {} sym'.format(cr))
print('sym_a {} sym'.format(t))

print('sym_a * sym_a')

print('sym_a ) a_rb')
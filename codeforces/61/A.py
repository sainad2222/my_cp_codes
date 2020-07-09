a = input()
b = input()
inta = int(a,2)
intb = int(b,2)
intc = inta^intb
strc = '{0:b}'.format(intc)
print('0'*(max(len(a),len(b))-len(strc))+strc)
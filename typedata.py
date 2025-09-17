# angka satuan (integer)
data_interger = 10
print('')
print('data: ', data_interger)
print('-type: ', type(data_interger))

# angka desimal (float)
# float 32-bit (4 byte)
data_float = 10.5
print('')
print('data: ', data_float)
print('-type: ', type(data_float))

# string
data_string = 'sepuluh'
print('')
print('data: ', data_string)
print('-type: ', type(data_string))

# boolean (True/False)
data_boolean = True
print('')
print('data: ', data_boolean)
print('-type: ', type(data_boolean))

print('data: ', not data_boolean)
print('-type: ', type(not data_boolean))

# kita bisa mengkonversi tipe data
data_integer = 10
data_float = float(data_integer) # konversi integer ke float
print('')
print('data: ', data_float)
print('type: ', type(data_float))

## tipe data khusus
# bilangan kompleks
data_complex = complex(10, 5) # 10 + 5i
print('')
print('data: ', data_complex)
print('type: ', type(data_complex))


# Kita bisa tipedata dari bahasa C
from ctypes import c_char, c_byte, c_short, c_int, c_long, c_float, c_double, c_longlong

# Double (64-bit)
# 64-bit (8 byte)
data_c_double = c_double(10.5)
print('')
print('data: ', data_c_double)
print('type: ', type(data_c_double))

# Char (1 byte)
data_c_char = c_char(b'a') # Python membedakan string ('a') dan byte string (b'a').
print('')
print('data: ', data_c_char)
print('type: ', type(data_c_char))






'''
an example of read and writing Unicode string
write then read
'''
CODEC ='utf-8'
FILE='unicode.txt'

hello_out=u'hello I am test the connect world\n'
bytes_out=hello_out.encode(CODEC)
f=open(FILE,'w')
f.write(bytes_out)
f.close()

f=open(FILE,'r')
bytes_in=f.read()
f.close()
hello_in=bytes_in.decode(CODEC)
print hello_in 
import sys
import getpass
from datetime import date

doc = """

"""


def xor_core(textnums, key):
    xor = lambda x, y: x^y
    keynums = [ord(j) for i in range(0, len(textnums)//len(key)+1) for j in key]
    return list(map(xor, textnums, keynums))

def xor_encrypt(text, key):
    textnums = list(map(ord, text))
    return ','.join(map(str, xor_core(textnums, key)))

def xor_decrypt(text, key):
    textnums = list(map(int, text.split(',')))
    return ''.join(map(chr, xor_core(textnums, key)))
 
def file_ops(enc=True, inp='input', outp='output-'+str(date.today())): 
	with open(inp, 'r') as fin:
		text = fin.read()
		key = getpass.getpass("Enter key:")
		out = xor_encrypt(text, key) if enc else xor_decrypt(text, key)
		with open(outp, 'w') as fout:
			fout.write(out)
		print(out)

def cli():
	enc = True if input('Encrypt? (y/n):') == 'y' else False
	if enc:
		text = input("Enter text to encrypt:")
		key = getpass.getpass("Enter key:")
		print(xor_encrypt(text, key))
	else:
		text = input("Enter text to decrypt:")
		key = getpass.getpass("Enter key:")
		print(xor_decrypt(text, key))
		
if __name__ == "__main__":
	if len(sys.argv) < 3:
		file_ops()
	elif len(sys.argv) == 4:
		if sys.argv[1] == '-e':
			if sys.argv[2] == '-i':
				file_ops(enc=True, inp = sys.argv[3])
			elif sys.argv[2] == '-o':
				file_ops(enc=True, outp = sys.argv[3])
			else:
				raise AttributeError(doc)
		elif sys.argv[1] == '-d':
			if sys.argv[2] == '-i':
				file_ops(enc=False, inp = sys.argv[3])
			elif sys.argv[2] == '-o':
				file_ops(enc=False, outp = sys.argv[3])
			else:
				raise AttributeError(doc)
		else:
			raise AttributeError(doc)
	elif len(sys.argv) == 6:
		if sys.argv[1] == '-e':
			if sys.argv[2] == '-i' and sys.argv[4] == '-o':
				file_ops(enc=True, inp = sys.argv[3], outp = sys.argv[5])
			elif sys.argv[2] == '-o' and sys.argv[4] == '-i':
				file_ops(enc=True, inp = sys.argv[5], outp = sys.argv[3])
			else:
				raise AttributeError(doc)
		elif sys.argv[1] == '-d':
			if sys.argv[2] == '-i' and sys.argv[4] == '-o':
				file_ops(enc=False, inp = sys.argv[3], outp = sys.argv[5])
			elif sys.argv[2] == '-o' and sys.argv[4] == '-i':
				file_ops(enc=False, inp = sys.argv[5], outp = sys.argv[3])
			else:
				raise AttributeError(doc)
		else:
			raise AttributeError(doc)
	else:
		raise AttributeError(doc)

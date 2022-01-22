import sys
import getpass
from datetime import date

doc = """

"""


def xor_core(data, key):
    xor = lambda x, y: x^y
    longkey = key*(len(data)//len(key)+1)
    datarray = bytearray(data)
    return bytes(map(xor, datarray, longkey))
 
def file_ops(keyfile='key', inp=None, outp=None):
	with open(inp, 'rb') as fin, open(keyfile, 'rb') as keyin:
		data = fin.read()
		key = keyin.read()
		out = xor_core(data, key)
		with open(outp, 'wb') as fout:
			fout.write(out)
		#print(out)

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
	if sys.argv[1] == '-k' and sys.argv[3] == '-i' and sys.argv[5] == '-o':
		file_ops(keyfile = sys.argv[2], inp = sys.argv[4], outp = sys.argv[6])

	"""
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
	"""

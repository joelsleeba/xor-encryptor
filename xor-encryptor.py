import sys
import getpass

doc = """

"""

def xor_core_txt(txtnums, key):
    xor = lambda x, y: x^y
    keynums = [ord(j) for i in range(0, len(txtnums)//len(key)+1) for j in key]
    return list(map(xor, txtnums, keynums))

def xor_txt_encrypt(txt, key):
    txtnums = list(map(ord, txt))
    return ','.join(map(str, xor_core_txt(txtnums, key)))

def xor_txt_decrypt(txt, key):
    txtnums = list(map(int, txt.split(',')))
    return ''.join(map(chr, xor_core_txt(txtnums, key)))

def xor_core(data, key):
    xor = lambda x, y: x^y
    longkey = key*(len(data)//len(key)+1)
    return bytes(map(xor, data, longkey))
 
def bin_ops(keyin, inp, outp, clikey=False):
	if not clikey:
		keyfile = open(keyin, 'rb')
		key = keyfile.read()
		keyfile.close()
	else:
		key = keyin

	with open(inp, 'rb') as fin:
		data = fin.read()
		out = xor_core(data, key)
		with open(outp, 'wb') as fout:
			fout.write(out)

def txt_ops(enc=False, key=None, txt=None):
	return xor_txt_encrypt(txt, key) if enc else xor_txt_decrypt(txt, key)
		
if __name__ == "__main__":
	if '-b' in sys.argv:
		clikey = False
		if '-k' in sys.argv:
			try:
				keyin = sys.argv[sys.argv.index('-k')+1]
			except:
				print('Specify path to key file after -k')
				quit()
		else:
			keyin = getpass.getpass("Enter key:").encode('utf-8')
			clikey = True
		
		if '-i' in sys.argv:
			try:
				inpf = sys.argv[sys.argv.index('-i')+1]
			except:
				print('Specify path to input file after -i')
				quit()
		else:
			print('Specify path to input file after -i')
			quit()

		if '-o' in sys.argv:
			try:
				outpf = sys.argv[sys.argv.index('-o')+1]
			except:
				print('Specify path to output file after -o')
				quit()
		else:
			print('Specify path to output file after -o')
			quit()
		
		bin_ops(keyin, inpf, outpf, clikey)

	else:
		if '-e' in sys.argv:
			enc = True
		elif '-d' in sys.argv:
			enc = False
		else:
			enc = True if input("Encrypt? (y/n)") == 'y' else False
		
		if '-k' in sys.argv:
			try:
				keyfile = sys.argv[sys.argv.index('-k')+1]
				keyf = open(keyfile, 'r')
				keyin = keyf.read()
				keyf.close()
			except:
				print('Specify path to key file after -k')
				quit()
		else:
			keyin = getpass.getpass("Enter key:")
		
		if '-i' in sys.argv:
			try:
				inpfile = sys.argv[sys.argv.index('-i')+1]
				inpf = open(inpfile, 'r')
				inp = inpf.read()
				inpf.close()
			except:
				print('Specify path to input file after -i')
				quit()
		else:
			inp = input("Enter input text:")

		output = txt_ops(enc, keyin, inp)

		if '-o' in sys.argv:
			try:
				outfile = sys.argv[sys.argv.index('-o')+1]
				outpf = open(outfile, 'w')
				outpf.write(output)
				outpf.close()
			except:
				print('Specify path to output file after -o')
				print(output)
				quit()
		else:
			print(output)
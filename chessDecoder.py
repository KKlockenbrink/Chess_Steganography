# This program is a Python program that can accept a file and encode the file into chess games using the PGN file format
# This program was created for educational purposes for a Computer Forensics project at California State University, Sacramento.
# Date Last Modified: 04 May 2018
import chess
import chess.pgn
import math
import binascii
import sys

sys.setrecursionlimit(1500) 
f = open('testDoc.pgn')
fh = open('newText.txt', 'wb')
def decoder(line):
	game = chess.pgn.Game()
	board = chess.Board()
	white_last = False
	black_last = False
	prev_move_white = ""
	prev_move_black = ""
	count = 0
	moves = line.split(" ")
	byte = ""
	while count < len(moves) - 1:
		white = moves[count + 1]
		black = moves[count + 2]
		if white == '*\n':
			break
		l = str(board.legal_moves)
		i = l.split("(")
		l = i[1]
		i = l.split(")")
		l = i[0]
		my_list = l.split(", ")
		if prev_move_white in my_list and len(my_list) > 1:
			my_list.remove(prev_move_white)
		num_moves = len(my_list)
		if num_moves > 2:
			num_bits = math.floor(math.log(num_moves,2))
		else:
			num_bits = 1
		indx = my_list.index(white)
		next_move = str(my_list[indx])
		s = str(board.push_san(next_move))
		node = game.add_variation(chess.Move.from_uci(s))
		if not white_last:
			prev_move_white = next_move
			white_last = True
		else:
			white_last = False
		if num_bits == 2:
			binary = str('{:02b}'.format(indx))
		elif num_bits == 3:
			binary = str('{:03b}'.format(indx))
		elif num_bits == 4:
			binary = str('{:04b}'.format(indx))
		elif num_bits == 5:
			binary = str('{:05b}'.format(indx))
		elif num_bits == 6:
			binary = str('{:06b}'.format(indx))
		elif num_bits == 7:
			binary = str('{:01b}'.format(indx))
		elif num_bits == 8:
			binary = str('{:08b}'.format(indx))
		if num_bits > 1:
			if byte == "":
				byte = binary
			elif len(byte) < 8:
				if len(byte) + len(binary) <= 8:
					byte = byte + binary
					if len(byte) == 8:
						b = '%02x' % int(byte, 2)
						c = binascii.unhexlify(b)
						fh.write(c)
						byte = ""
				else:
					while len(binary) + len(byte) > 8:
						if binary[:1] == '0':
							binary = binary[1:]
						elif binary[(len(binary) - 1):] == '0':
							binary = binary[:(len(binary) - 1)]
						else:
							print("INFINITE LOOP???")
							input()
					byte = byte + binary
					b = '%02x' % int(byte, 2)
					c = binascii.unhexlify(b)
					fh.write(c)
					byte = ""
			else:
				print("ERROR")
		if black == '*\n':
			break	
		l = str(board.legal_moves)
		i = l.split("(")
		l = i[1]
		i = l.split(")")
		l = i[0]
		my_list = l.split(", ")
		if prev_move_black in my_list and len(my_list) > 1:
				my_list.remove(prev_move_black)
		num_moves = len(my_list)
		if num_moves > 2:
			num_bits = math.floor(math.log(num_moves,2))
		else:
			num_bits = 1
		indx = my_list.index(black)
		next_move = str(my_list[indx])
		s = str(board.push_san(next_move))
		node = game.add_variation(chess.Move.from_uci(s)) 
		if not black_last:
			prev_move_black = next_move
			black_last = True
		else:
			black_last = False
		if num_bits == 2:
			binary = str('{:02b}'.format(indx))
		elif num_bits == 3:
			binary = str('{:03b}'.format(indx))
		elif num_bits == 4:
			binary = str('{:04b}'.format(indx))
		elif num_bits == 5:
			binary = str('{:05b}'.format(indx))
		elif num_bits == 6:
			binary = str('{:06b}'.format(indx))
		elif num_bits == 7:
			binary = str('{:01b}'.format(indx))
		elif num_bits == 8:
			binary = str('{:08b}'.format(indx))
		if num_bits > 1:
			if byte == "":
				byte = binary
			elif len(byte) < 8:
				if len(byte) + len(binary) <= 8:
					byte = byte + binary
					if len(byte) == 8:
						b = '%02x' % int(byte, 2)
						c = binascii.unhexlify(b)
						fh.write(c)
						byte = ""
				else:
					while len(binary) + len(byte) > 8:
						if binary[:1] == '0':
							binary = binary[1:]
						elif binary[(len(binary) - 1):] == '0':
							binary = binary[:(len(binary) - 1)]
						else:
							print("INFINITE LOOP???")
							input()
					byte = byte + binary
					b = '%02x' % int(byte, 2)
					c = binascii.unhexlify(b)
					fh.write(c)
					byte = ""
			else:
				print("ERROR")
		count = count + 3
	return;

for x in range(0,9):
	list = f.readline()
decoder(line = list)

while True:
	#START NEW GAME
	for x in range(0,10):
		list = f.readline()
		if not list:
			break
	if not list:
		break
	decoder(line = list)
f.close()
fh.close()
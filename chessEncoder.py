# This program is a Python program that can accept a file and encode the file into chess games using the PGN file format
# This program was created for educational purposes for a Computer Forensics project at California State University, Sacramento.
# Date Last Modified: 04 May 2018
import chess
import chess.pgn
import random
import names
import math
import binascii
from bitstring import BitArray
import sys

sys.setrecursionlimit(1500)
fh1 = open("testGames.pgn","w")
filename = 'testDoc.txt'
x = 1
with open(filename, "rb") as f:
	byte = f.read(1)
	while byte != b'':
		# Do stuff with byte.
		
		game = chess.pgn.Game()
		game.headers["Event"] = "Daily Tournament"
		game.headers["Date"] = "2018.04.06"
		game.headers["Round"] = x
		game.headers["White"] = names.get_first_name()
		game.headers["Black"] = names.get_first_name()

		board = chess.Board()
		
		white_last = True
		black_last = True
		#White to move
		l = str(board.legal_moves)
		i = l.split("(")
		l = i[1]
		i = l.split(")")
		l = i[0]
		my_list = l.split(", ")
		num_moves = len(my_list)
		if num_moves > 2:
			num_bits = math.floor(math.log(num_moves,2))
		else:
			num_bits = 1
		binary = bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
		b = binary[:num_bits]
		move = int(str(b),2)
		next_move = str(my_list[move])
		s = str(board.push_san(next_move))
		node = game.add_variation(chess.Move.from_uci(s))
		prev_move_white = next_move
		prev_num_bits = num_bits
		#Black to Move
		l = str(board.legal_moves)
		i = l.split("(")
		l = i[1]
		i = l.split(")")
		l = i[0]
		my_list = l.split(", ")
		num_moves = len(my_list)
		if num_moves > 2:
			num_bits = math.floor(math.log(num_moves,2))
		else:
			num_bits = 1
		if((prev_num_bits + num_bits) <= 8): 
			if num_bits > 1:
				if byte == b'':
					break;
				binary = bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
				b = binary
				b = b[prev_num_bits: prev_num_bits + num_bits]
				move = int(str(b),2)
				prev_num_bits += num_bits
			else:
				move = 0
			next_move = str(my_list[move])
			prev_move_black = next_move
			if prev_num_bits == 8:
				byte = f.read(1)
				prev_num_bits = 0
		elif(prev_num_bits == 8):
			byte = f.read(1)
			prev_num_bits = 0
			if byte == b'':
				break;
			binary = bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
			if num_bits > 1:
				b = binary
				b = b[:num_bits]
				move = int(str(b),2)
				prev_num_bits = num_bits
			else:
				move = 0
			next_move = str(my_list[move])
			prev_move_black = next_move
		else:
			#prev_num_bits is less than 8 but adding num_bits to it will push it over 8 bits
			num_bits = 8 - prev_num_bits
			if byte == b'':
				break;
			binary = bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
			b = binary
			b = b[prev_num_bits: prev_num_bits + num_bits]
			move = int(str(b),2)
			next_move = str(my_list[move])
			prev_move_black = next_move
			byte = f.read(1)
			prev_num_bits = 0
			if byte == b'':
				break;
		if not next_move:
			break;
		s = str(board.push_san(next_move))
		node = node.add_variation(chess.Move.from_uci(s))

		while( (not board.is_checkmate()) and (not board.is_stalemate()) and (not board.is_insufficient_material()) and (not board.is_seventyfive_moves()) and (not board.is_fivefold_repetition())):
			#White to Move
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
			if((prev_num_bits + num_bits) <= 8): 
				if num_bits > 1:
					if byte == b'':
						break;
					binary = bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
					b = binary
					b = b[prev_num_bits: prev_num_bits + num_bits]
					move = int(str(b),2)
					prev_num_bits += num_bits
				else:
					move = 0
				next_move = str(my_list[move])
				if not white_last:
					prev_move_white = next_move
					white_last = True
				else:
					white_last = False
				if prev_num_bits == 8:
					byte = f.read(1)
					prev_num_bits = 0
			elif(prev_num_bits == 8):
				byte = f.read(1)
				prev_num_bits = 0
				if byte == b'':
					break;
				binary = bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
				if num_bits > 1:
					b = binary
					b = b[:num_bits]
					move = int(str(b),2)
					prev_num_bits = num_bits
				else:
					move = 0
				next_move = str(my_list[move])
				if not white_last:
					prev_move_white = next_move
					white_last = True
				else:
					white_last = False
			else:
				#prev_num_bits is less than 8 but adding num_bits to it will push it over 8 bits
				num_bits = 8 - prev_num_bits
				if byte == b'':
					break;
				binary = bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
				b = binary
				b = b[prev_num_bits: prev_num_bits + num_bits]
				move = int(str(b),2)
				next_move = str(my_list[move])
				if not white_last:
					prev_move_white = next_move
					white_last = True
				else:
					white_last = False
				byte = f.read(1)
				prev_num_bits = 0
				if byte == b'':
					break;
			if not next_move:
				break;
			s = str(board.push_san(next_move))
			node = node.add_variation(chess.Move.from_uci(s))
			#Black to Move
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
			if((prev_num_bits + num_bits) <= 8):
				if num_bits > 1:
					if byte == b'':
						break;
					binary = bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
					b = binary
					b = b[prev_num_bits: prev_num_bits + num_bits]
					move = int(str(b),2)
					prev_num_bits += num_bits
				else:
					move = 0
				next_move = str(my_list[move])
				if not black_last:
					prev_move_black = next_move
					black_last = True
				else:
					black_last = False
				if prev_num_bits == 8:
					byte = f.read(1)
					prev_num_bits = 0
			elif(prev_num_bits == 8):
				byte = f.read(1)
				prev_num_bits = 0
				if byte == b'':
					break;
				binary = bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
				if num_bits > 1:
					b = binary
					b = b[:num_bits]
					move = int(str(b),2)
					prev_num_bits = num_bits
				else:
					move = 0
				next_move = str(my_list[move])
				if not black_last:
					prev_move_black = next_move
					black_last = True
				else:
					black_last = False
			else:
				#prev_num_bits is less than 8 but adding num_bits to it will push it over 8 bits
				num_bits = 8 - prev_num_bits
				if byte == b'':
					break;
				binary = bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
				b = binary
				b = b[prev_num_bits: prev_num_bits + num_bits]
				move = int(str(b),2)
				next_move = str(my_list[move])
				if not black_last:
					prev_move_black = next_move
					black_last = True
				else:
					black_last = False
				byte = f.read(1)
				prev_num_bits = 0
				if byte == b'':
					break;
			if not next_move:
				break;
			s = str(board.push_san(next_move))
			node = node.add_variation(chess.Move.from_uci(s))
		fh1.write(str(game))
		fh1.write("\n\n")
		x += 1
fh1.close()
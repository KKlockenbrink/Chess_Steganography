# Chess_Steganography
This repository contains two Python programs that can convert (encode) files into chess games via PGN formatting, as well as convert those chess games back into their original file.

Requirements:
The version of Python used for this program was Python 3.6.3
The code uses a special libray called python-chess which can be found here:
  https://github.com/niklasf/python-chess
For further information on how python-chess works, visit here:
  http://python-chess.readthedocs.io/en/latest/
  
The code was tested only on Windows 10 through cmd.

Technically, this code should be able to encode any file into chess games and back to the original file becuase it works at the bit level, however, the encoding and decoding process is quite exhaustive and creates a lot of chess games. A 500 kB file will usually take about 30 minutes to encode and another 30 minutes to decode. Therefore, I recommend using this program for small files, such as text files.


User Manual

This is a simple program that can be run from the command line. The program requires the use of Python v3, and a few installed libraries. The libraries can be installed from the command line using Pip package manager for Python. 

The source code for the chessEncoder.py and chessDecoder.py programs can be found at the following GitHub repository: https://github.com/KKlockenbrink/Chess_Steganography

Python v3 can be obtained from the their official website: https://www.python.org/downloads/ 

The first library that needs to be installed is Python-Chess, which can be installed with the following command: 
	pip install python-chess[engine,gaviota]

The second library that needs to be installed is the names library, which allows for us to randomly generate player names for each generated chess game. This library can be installed with the following command:
	pip install names

The third library that needs to be installed is the bitstring library, which can be installed with the following command:
	pip install bitstring
chessEncoder.py : 
Step #1:
User must specify the the output filename in the “open” function. 
  Important Note: The output file must have a .pgn file extension. 
Step #2:
User must specify the input filename for the “filename” variable

Step #3:

	To run the program through the command line after specifying the input and output files for the chess encoder. The input file that you will be encoding must be inside of the same directory that the chessEncoder.py is in or else the program will fail to run. Move to the directory that contains the input file and the chessEncoder.py in the terminal and type the following command to run the program.
	Python chessEncoder.py
chessDecoder.py :
Step #1: 
User must specify the .pgn that they would like to decode as an argument to the “open” function


Step #2: 
	User must specify the output filename and file extension in the “open” function

Step #3:

	To run the program through the command line after specifying the input and output files for the chess decoder. The input file that you will be encoding must be inside of the same directory that the chessDecoder.py is in or else the program will fail to run. Move to the directory that contains the input file and the chessDecoder.py in the terminal and type the following command to run the program.
	Python chessDecoder.py

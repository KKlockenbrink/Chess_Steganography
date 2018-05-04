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

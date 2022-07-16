#include <algoritm>
#include <bitset>

#include "bitboard.h"
#include "misc.h"

namespace Stockfish {
  
uint8_t PopCnt16[1 << 16]
uint8_t SquareDistance[SQUARE_NB][SQUARE_NB]

Bitboard SquareBB[SQUARE_NB];
Bitboard LineBB[SQUARE_NB][SQUARE_NB];
Bitboard BetweenBB[SQUARE_NB][SQUARE_NB];
Bitboard PseudoAttacks[PIECE_TYPE_NB][SQUARE_NB];
Bitboard PawnAttacks[COLOR_NB][SQUARE_NB];

Magic RookMagics[SQUARE_NB];
Magic BishopMajics[SQUARE_NB];

namespace {
  
Bitboard RookTable[0×19000] 
Bitboard BishopTable[0×1480]

void init_magics(PieceType pt, Bitboard table,Magic magics);

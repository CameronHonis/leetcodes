#include <vector>
#include <string>
#include <cassert>
#include <valarray>

using namespace std;

struct Bitboard {
    // two integers since the constraint (9x9) exceeds 64 bits
    // a represents the row-major first 64 bits, b represents the rest (if any)
    uint64_t a;
    uint32_t b;
    uint8_t size;
};

void addSquareToBitboard(uint r, uint c, Bitboard &mask) {
    int bin_idx = r * mask.size + c;
    if (bin_idx < 64) {
        uint64_t bit = 1ull << bin_idx;
        mask.a |= bit;
    } else {
        uint64_t bit = 1ull << (bin_idx - 64);
        mask.b |= bit;
    }
}

Bitboard unionBitboards(const Bitboard &a, const Bitboard &b) {
    Bitboard rtn{a.a | b.a, a.b | b.b, a.size};
    return rtn;
}

bool doesIntersect(const Bitboard &a, const Bitboard &b) {
    return (a.a & b.a) || (a.b & b.b);
}

void printBitboard(const Bitboard &bitboard) {
    string result = "\n";
    for (int r = 0; r < bitboard.size; r++) {
        for (int c = 0; c < bitboard.size; c++) {
            int bin_idx = r * bitboard.size + c;
            if (bin_idx < 64) {
                uint64_t bit = 1ull << bin_idx;
                result += (bitboard.a & bit) ? "x " : ". ";
            } else {
                uint64_t bit = 1ull << (bin_idx - 64);
                result += (bitboard.b & bit) ? "x " : ". ";
            }
        }
        result += "\n";
    }
    result += "\n";
    printf("%s", result.c_str());
}

vector<string> bitboardToStrings(Bitboard bitboard) {
    vector<string> rtn;
    for (int r = 0; r < bitboard.size; r++) {
        string row = "";
        for (int c = 0; c < bitboard.size; c++) {
            int bin_idx = r * bitboard.size + c;
            if (bin_idx < 64) {
                uint64_t bit = 1ull << bin_idx;
                row += (bitboard.a & bit) ? "Q" : ".";
            } else {
                uint64_t bit = 1ull << (bin_idx - 64);
                row += (bitboard.b & bit) ? "Q" : ".";
            }
        }
        rtn.push_back(row);
    }
    return rtn;
}

class Solution {
public:
    vector<Bitboard> col_masks;
    vector<Bitboard> pos_diag_masks;
    vector<Bitboard> neg_diag_masks;

    vector<vector<string>> solveNQueens(int n) {
        // bitboard in row-major order (does it matter?)
        initMasks(n);
        vector<Bitboard> bitboards;
        getBitboards(Bitboard{0, 0, uint8_t(n)}, 0, bitboards);
        vector<vector<string>> result;
        for (Bitboard bitboard: bitboards) {
            vector<string> bitboard_str = bitboardToStrings(bitboard);
            result.push_back(bitboard_str);
        }
        return result;
    }


    void initMasks(int n) {
        for (int c = 0; c < n; c++) {
            Bitboard col_mask{0, 0, uint8_t(n)};
            for (int r = 0; r < n; r++) {
                addSquareToBitboard(r, c, col_mask);
            }
            col_masks.push_back(col_mask);
        }
        for (int d = -n + 1; d < n; d++) {
            Bitboard pos_diag_mask{0, 0, u_int8_t(n)};
            int r = d, c = 0;
            while (r < n && c < n) {
                if (r >= 0) {
                    addSquareToBitboard(r, c, pos_diag_mask);
                }
                r++;
                c++;
            }
            pos_diag_masks.push_back(pos_diag_mask);
        }
        for (int d = 2 * n - 2; d >= 0; d--) {
            Bitboard neg_diag_mask{0, 0, u_int8_t(n)};
            int r = d, c = 0;
            while (r >= 0 && c < n) {
                if (r < n) {
                    addSquareToBitboard(r, c, neg_diag_mask);
                }
                r--;
                c++;
            }
            neg_diag_masks.push_back(neg_diag_mask);
        }
    }

    void getBitboards(const Bitboard bitboard, uint depth, vector<Bitboard> &bitboards) {
        if (depth == bitboard.size) {
            bitboards.push_back(bitboard);
            return;
        }
        for (uint c = 0; c < bitboard.size; c++) {
            if (canAddQueen(bitboard, depth, c)) {
                Bitboard new_bitboard = bitboard;
                addSquareToBitboard(depth, c, new_bitboard);
                getBitboards(new_bitboard, depth + 1, bitboards);
            }
        }
    }

    bool canAddQueen(const Bitboard &bitboard, const uint r, const uint c) {
        Bitboard queen_mask{0, 0, bitboard.size};
        queen_mask = unionBitboards(queen_mask, col_masks[c]);
        Bitboard pos_diag_mask = pos_diag_masks[bitboard.size + r - c - 1];
        queen_mask = unionBitboards(queen_mask, pos_diag_mask);
        Bitboard neg_diag_mask = neg_diag_masks[2*bitboard.size - 2 - r - c];
        queen_mask = unionBitboards(queen_mask, neg_diag_mask);
        return !doesIntersect(bitboard, queen_mask);
    }
};

void testAddSquareToBitboard() {
    // corners of 8x8 board
    Bitboard bitboard{0, 0, 8};
    addSquareToBitboard(0, 0, bitboard);
    assert(bitboard.a == 1);
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(0, 1, bitboard);
    assert(bitboard.a == 2);
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(0, 2, bitboard);
    assert(bitboard.a == 4);
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(1, 0, bitboard);
    assert(bitboard.a == 256);
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(2, 0, bitboard);
    assert(bitboard.a == 65536);
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(0, 6, bitboard);
    assert(bitboard.a == 64);
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(0, 7, bitboard);
    assert(bitboard.a == 128);
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(1, 7, bitboard);
    assert(bitboard.a == 32768);
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(6, 0, bitboard);
    assert(bitboard.a == pow(2, 48));
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(7, 0, bitboard);
    assert(bitboard.a == pow(2, 56));
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(7, 1, bitboard);
    assert(bitboard.a == pow(2, 57));
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(7, 6, bitboard);
    assert(bitboard.a == pow(2, 62));
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(7, 7, bitboard);
    assert(bitboard.a == pow(2, 63));
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(6, 7, bitboard);
    assert(bitboard.a == pow(2, 55));
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    // corners of 9x9 board
    bitboard = Bitboard{0, 0, 9};
    addSquareToBitboard(0, 0, bitboard);
    assert(bitboard.a == 1);
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(0, 8, bitboard);
    assert(bitboard.a == 256);
    assert(bitboard.b == 0);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(8, 0, bitboard);
    assert(bitboard.a == 0);
    assert(bitboard.b == 256);
    bitboard.a = 0;
    bitboard.b = 0;

    addSquareToBitboard(8, 8, bitboard);
    assert(bitboard.a == 0);
    assert(bitboard.b == 65536);
    bitboard.a = 0;
    bitboard.b = 0;
}

void testInitMasks() {
    Solution sol;
    sol.initMasks(9);

    assert(sol.col_masks.size() == 9);
    assert(sol.pos_diag_masks.size() == 17);
    assert(sol.neg_diag_masks.size() == 17);
}

void testSolveNQueens() {
    Solution sol;
    vector<vector<string>> result = sol.solveNQueens(4);
    assert(result.size() == 2);
    assert(result[0].size() == 4);
    assert(result[1].size() == 4);
    assert(result[0][0] == ".Q..");
    assert(result[0][1] == "...Q");
    assert(result[0][2] == "Q...");
    assert(result[0][3] == "..Q.");
    assert(result[1][0] == "..Q.");
    assert(result[1][1] == "Q...");
    assert(result[1][2] == "...Q");
    assert(result[1][3] == ".Q..");
}

int main() {
    testAddSquareToBitboard();
    testInitMasks();
    testSolveNQueens();

    Solution sol;
    vector<vector<string>> boards = sol.solveNQueens(9);
    for (vector<string> board : boards) {
        for (string row: board) {
            printf("%s\n", row.c_str());
        }
        printf("\n");
    }
    return 0;
}
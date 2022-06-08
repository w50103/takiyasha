from __future__ import annotations

from typing import Final

__all__ = ['key256mapping_all', 'key256mapping_128to44', 'ogg_public_header1',
           'ogg_public_header2', 'ogg_public_confidence1', 'ogg_public_confidence2',
           'default_key256_mask44']

# key256mapping_all = [[]] * 256
# key256mapping_128to44 = [float('nan')] * 128
#
# for i in range(128):
#     real_idx = (i * i + 27) % 256
#     if not key256mapping_all[real_idx]:
#         key256mapping_all[real_idx] = [i]
#     else:
#         key256mapping_all[real_idx].append(i)
#
# idx44 = 0
# for all128 in key256mapping_all:
#     if all128:
#         for idx128 in all128:
#             key256mapping_128to44[idx128] = idx44
#         idx44 += 1

# key256mapping_all 和 key256mapping_128to44 是由以上代码生成的结果
key256mapping_all: Final[list[list[int]]] = [
    [], [], [], [], [45, 83], [], [], [], [], [], [], [], [39, 89],
    [], [], [], [], [], [], [], [53, 75], [], [], [], [], [], [],
    [0, 16, 32, 48, 64, 80, 96, 112], [1, 127], [], [], [2, 62, 66, 126],
    [], [], [], [], [3, 125], [], [], [], [], [], [],
    [4, 28, 36, 60, 68, 92, 100, 124], [23, 105], [], [], [], [], [], [],
    [], [5, 123], [], [], [], [], [], [], [], [17, 111], [], [],
    [6, 58, 70, 122], [], [], [], [], [51, 77], [], [], [], [], [], [],
    [], [7, 121], [], [], [], [], [], [], [], [43, 85], [], [], [], [],
    [], [], [8, 24, 40, 56, 72, 88, 104, 120], [33, 95], [], [],
    [18, 46, 82, 110], [], [], [], [], [29, 99], [], [], [], [], [], [],
    [], [9, 119], [], [], [], [], [], [], [], [37, 91], [], [], [], [],
    [], [], [], [49, 79], [], [], [10, 54, 74, 118], [], [], [], [],
    [19, 109], [], [], [], [], [], [], [], [25, 103], [], [], [], [],
    [], [], [], [11, 117], [], [], [], [], [], [], [], [63, 65], [], [],
    [30, 34, 94, 98], [], [], [], [], [61, 67], [], [], [], [], [], [],
    [12, 20, 44, 52, 76, 84, 108, 116], [41, 87], [], [], [], [], [], [],
    [], [59, 69], [], [], [], [], [], [], [], [47, 81], [], [],
    [26, 38, 90, 102], [], [], [], [], [13, 115], [], [], [], [], [], [],
    [], [57, 71], [], [], [], [], [], [], [], [21, 107], [], [], [], [],
    [], [], [], [31, 97], [], [], [14, 50, 78, 114], [], [], [], [],
    [35, 93], [], [], [], [], [], [], [], [55, 73], [], [], [], [], [],
    [], [], [27, 101], [], [], [], [], [], [], [], [15, 113], [], [],
    [22, 42, 86, 106]
]
key256mapping_128to44: Final[list[int]] = [
    3, 4, 5, 6, 7, 9, 11, 13, 15, 19, 22, 25, 29, 34, 38, 42, 3, 10, 17, 23, 29, 36, 43, 8,
    15, 24, 33, 41, 7, 18, 27, 37, 3, 16, 27, 39, 7, 20, 33, 1, 15, 30, 43, 14, 29, 0, 17,
    32, 3, 21, 38, 12, 29, 2, 22, 40, 15, 35, 11, 31, 7, 28, 5, 26, 3, 26, 5, 28, 7, 31, 11,
    35, 15, 40, 22, 2, 29, 12, 38, 21, 3, 32, 17, 0, 29, 14, 43, 30, 15, 1, 33, 20, 7, 39,
    27, 16, 3, 37, 27, 18, 7, 41, 33, 24, 15, 8, 43, 36, 29, 23, 17, 10, 3, 42, 38, 34, 29,
    25, 22, 19, 15, 13, 11, 9, 7, 6, 5, 4
]

ogg_public_header1: Final[bytes] = bytes(
    [
        79, 103, 103, 83, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 255,
        255, 255, 255, 1, 30, 1, 118, 111, 114, 98, 105, 115, 0, 0, 0, 0, 2, 68, 172, 0, 0, 0,
        0, 0, 0, 0, 238, 2, 0, 0, 0, 0, 0, 184, 1, 79, 103, 103, 83, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 255, 255, 255, 255, 1, 0, 0, 0, 255, 255, 255, 255
    ]
)
ogg_public_header2: Final[bytes] = bytes(
    [
        3, 118, 111, 114, 98, 105, 115, 44, 0, 0, 0, 88, 105, 112, 104, 46, 79, 114, 103, 32,
        108, 105, 98, 86, 111, 114, 98, 105, 115, 32, 73, 32, 50, 48, 49, 53, 48, 49, 48, 53,
        32, 40, 226, 155, 132, 226, 155, 132, 226, 155, 132, 226, 155, 132, 41, 255, 0, 0, 0,
        255, 0, 0, 0, 84, 73, 84, 76, 69, 61
    ]
)
ogg_public_confidence1: Final[list[int]] = [
    9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 9,
    9, 9, 9, 9, 9, 9, 9, 9, 9, 6, 3, 3, 3, 3, 6, 6, 6, 6, 3, 3, 3, 3, 6, 6, 6, 6, 6, 9, 9, 9,
    9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 0
]
ogg_public_confidence2: Final[list[int]] = [
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 3,
    3, 0, 1, 3, 3, 3, 3, 3, 3, 3, 3
]
default_key256_mask44: Final[bytes] = bytes(
    [
        222, 81, 250, 195, 74, 214, 202, 144, 126, 103, 94, 247, 213, 82, 132, 216, 71, 149,
        187, 161, 170, 198, 102, 35, 146, 98, 243, 116, 161, 159, 244, 160, 29, 63, 91, 240,
        19, 14, 9, 61, 249, 188, 0, 17
    ]
)
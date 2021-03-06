from scipy import stats
from dataTransformation import *
from patternProcessing import *


# Takes in a sequence of numbers and returns the linear regression
# of their pattern
def lin_reg_nums(inp_list):
    nums = []
    for i in range(len(inp_list)):
        nums.append(int(inp_list[i]))
    sz = len(nums)
    xs = range(sz)
    res = stats.linregress(xs, nums)
    return res


# Takes in a sequence of letters and returns the linear regression
# of their pattern
#
# Adjusts for upper/lowercase using offset
def lin_reg_letters(inp_list, offset):
    sz = len(inp_list)
    xs = range(sz)
    for pos in range(len(inp_list)):
        inp_list[pos] = to_base26(inp_list[pos], offset)
    res = stats.linregress(xs, inp_list)
    return res


# Takes in a sequence of special characters and returns the linear regression
# of their pattern
#
# Currently supports constant patterns only
def lin_reg_spec(inp_list):
    sz = len(inp_list)
    xs = range(sz)
    for pos in range(len(inp_list)):
        inp_list[pos] = ord(inp_list[pos])
    res = stats.linregress(xs, inp_list)
    return res


def predict_at_pos(mat, r, c=0):
    tmp = []
    flat = np.array(rotate_matrix(mat.copy())).flatten()
    for i in range(len(flat)):
        if flat[i] is None:
            mat = lin_reg_seq_builder(np.array([tmp]))
            out = ""
            # if r > 0:
            #     c = r0
            for row in range(len(mat)):
                print("Slope: " + str(mat[row][1].slope) + ", Intercept: " + str(mat[row][1].intercept) + ", R: " + str(r) + ", C: " + str(c))
                print(len(mat[0]))
                val = int(mat[row][1].slope * (r + c * (len(mat[0]) + 1)) + mat[row][1].intercept)
                if mat[row][0] == "C":
                    out += str(letters_from_base26(val, 65))
                elif mat[row][0] == "L":
                    out += str(letters_from_base26(val, 97))
                elif mat[row][0] == "N":
                    out += str(val)
                elif mat[row][0] == "S":
                    out += str(chr(val))
            return out
        tmp.append(flat[i])

    if not lin_reg_mat_builder(mat):
        if all([len(ele) == 1 for ele in mat]):
            mat = rotate_matrix(mat)
        if not lin_reg_seq_builder(mat):
            return False
        mat = lin_reg_seq_builder(mat)
        out = ""
        if r > 0:
            c = r
        for row in range(len(mat)):
            val = int(mat[row][1].slope * c + mat[row][1].intercept)
            if mat[row][0] == "C":
                out += str(letters_from_base26(val, 65))
            elif mat[row][0] == "L":
                out += str(letters_from_base26(val, 97))
            elif mat[row][0] == "N":
                out += str(val)
            elif mat[row][0] == "S":
                out += str(chr(val))
        return out
    else:
        mat = lin_reg_mat_builder(mat)
        out = ""
        for row in range(len(mat)):
            val = int(mat[row][1].slope * c + mat[row][1].intercept + mat[row][2].slope * r)
            if mat[row][0] == "C":
                out += str(letters_from_base26(val, 65))
            elif mat[row][0] == "L":
                out += str(letters_from_base26(val, 97))
            elif mat[row][0] == "N":
                out += str(val)
            elif mat[row][0] == "S":
                out += str(chr(val))
        return out


def lin_reg_mat_builder(mat):
    if len(mat) == 1 or all([len(ele) == 1 for ele in mat]):
        return False
    if not (matrix_trim(mat) is True):
        mat = matrix_trim(mat)
    s_t = is_valid_seq(mat)
    if not s_t:
        return False
    t = [[char]for char in s_t]
    rot_mat = rotate_matrix(mat)
    if not (has_valid_regs(mat, s_t) and has_valid_regs(rot_mat, s_t)):
        return False
    for pos in range(len(t)):
        if t[pos][0] == "C":
            t[pos].append(lin_reg_letters([l[1:] for l in parse_pattern(s_t, mat[0])][pos], 65))
            t[pos].append(lin_reg_letters([l[1:] for l in parse_pattern(s_t, rot_mat[0])][pos], 65))
        elif t[pos][0] == "L":
            t[pos].append(lin_reg_letters([l[1:] for l in parse_pattern(s_t, mat[0])][pos], 97))
            t[pos].append(lin_reg_letters([l[1:] for l in parse_pattern(s_t, rot_mat[0])][pos], 97))
        elif t[pos][0] == "N":
            t[pos].append(lin_reg_nums([l[1:] for l in parse_pattern(s_t, mat[0])][pos]))
            t[pos].append(lin_reg_nums([l[1:] for l in parse_pattern(s_t, rot_mat[0])][pos]))
        elif t[pos][0] == "S":
            if special_is_const([l[1:] for l in parse_pattern(s_t, mat[0])][pos]):
                t[pos].append(lin_reg_spec([l[1:] for l in parse_pattern(s_t, mat[0])][pos]))
                t[pos].append(lin_reg_spec([l[1:] for l in parse_pattern(s_t, rot_mat[0])][pos]))
    return t


def lin_reg_seq_builder(mat):
    s_t = is_valid_seq(mat)
    if not s_t:
        return False
    t = [[char]for char in s_t]
    for pos in range(len(t)):
        if t[pos][0] == "C":
            t[pos].append(lin_reg_letters([l[1:] for l in parse_pattern(s_t, mat[0])][pos], 65))
        elif t[pos][0] == "L":
            t[pos].append(lin_reg_letters([l[1:] for l in parse_pattern(s_t, mat[0])][pos], 97))
        elif t[pos][0] == "N":
            t[pos].append(lin_reg_nums([l[1:] for l in parse_pattern(s_t, mat[0])][pos]))
        elif t[pos][0] == "S":
            if special_is_const([l[1:] for l in parse_pattern(s_t, mat[0])][pos]):
                t[pos].append(lin_reg_spec([l[1:] for l in parse_pattern(s_t, mat[0])][pos]))
    return t


def has_valid_regs(mat, s_t):
    for i in range(len(s_t)):
        reg = ""
        for row in range(len(mat)):
            if s_t[i] == "C":
                if reg == "":
                    reg = lin_reg_letters([l[1:] for l in parse_pattern(s_t, mat[row])][i], 65)
                else:
                    if reg.slope != lin_reg_letters([l[1:] for l in parse_pattern(s_t, mat[row])][i], 65).slope:
                        return False
            elif s_t[i] == "L":
                if reg == "":
                    reg = lin_reg_letters([l[1:] for l in parse_pattern(s_t, mat[row])][i], 97)
                else:
                    if reg.slope != lin_reg_letters([l[1:] for l in parse_pattern(s_t, mat[row])][i], 97).slope:
                        return False
            elif s_t[i] == "N":
                if reg == "":
                    reg = lin_reg_nums([l[1:] for l in parse_pattern(s_t, mat[row])][i])
                else:
                    if reg.slope != lin_reg_nums([l[1:] for l in parse_pattern(s_t, mat[row])][i]).slope:
                        return False
    return True

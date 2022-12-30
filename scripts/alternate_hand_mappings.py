#!/usr/bin/env python3


LEFT_HAND = 1
RIGHT_HAND = 2

# Build mapping of letter to hand
qwerty = {
    'q': LEFT_HAND, 'w': LEFT_HAND, 'e': LEFT_HAND, 'r': LEFT_HAND, 't': LEFT_HAND, 'y': RIGHT_HAND, 'u': RIGHT_HAND, 'i': RIGHT_HAND, 'o': RIGHT_HAND, 'p': RIGHT_HAND,
    'a': LEFT_HAND, 's': LEFT_HAND, 'd': LEFT_HAND, 'f': LEFT_HAND, 'g': LEFT_HAND, 'h': RIGHT_HAND, 'j': RIGHT_HAND, 'k': RIGHT_HAND, 'l': RIGHT_HAND,
    'z': LEFT_HAND, 'x': LEFT_HAND, 'c': LEFT_HAND, 'v': LEFT_HAND, 'b': LEFT_HAND, 'n': RIGHT_HAND, 'm': RIGHT_HAND,
}

# Non used digrams
digrams = {
'bq', 'bz',
'cf', 'cj', 'cv', 'cx',
'fq', 'fv', 'fx', 'fz',
'gq', 'gv', 'gx',
'hx', 'hz',
'jb', 'jd', 'jf', 'jg', 'jh', 'jl', 'jm', 'jp', 'jq', 'jr', 'js', 'jt', 'jv', 'jw', 'jx', 'jy', 'jz',
'kq', 'kx', 'kz',
'mx', 'mz',
'pq', 'pv', 'px',
'qb', 'qc', 'qd', 'qf', 'qg', 'qh', 'qj', 'qk', 'ql', 'qm', 'qn', 'qp', 'qq', 'qv', 'qw', 'qx', 'qy', 'qz',
'sx',
'tq',
'vb', 'vf', 'vh', 'vj', 'vk', 'vm', 'vp', 'vq', 'vw', 'vx',
'wq', 'wv', 'wx',
'xd', 'xj', 'xk', 'xr', 'xz',
'yq', 'yy',
'zf', 'zr', 'zx',
}

# Build list of left-right and right-left digrams
lr_digrams = []
rl_digrams = []

for digram in digrams:
    if qwerty[digram[0]] == LEFT_HAND and qwerty[digram[1]] == RIGHT_HAND:
        lr_digrams.append(digram)
    elif qwerty[digram[0]] == RIGHT_HAND and qwerty[digram[1]] == LEFT_HAND:
        rl_digrams.append(digram)

# sort digrams
lr_digrams.sort()
rl_digrams.sort()

# Print digrams
print(f"Left-Right Digrams: {len(lr_digrams)}")
print('------------------')
for digram in lr_digrams:
    print(digram)

print(f"Right-Left Digrams: {len(rl_digrams)}")
print('------------------')
for digram in rl_digrams:
    print(digram)

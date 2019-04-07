# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Qualification Round - Problem D. Dat Bae
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
#
# Time:  O(NlogB)
# Space: O(N)
#

import sys

def count(response, i, c, cnt):
    same_cnt = 0
    while i < len(response) and same_cnt < cnt:
        if response[i] == c:
            same_cnt += 1
        else:
            break
        i += 1
    return same_cnt, i

def dat_bae():
    N, B, F = map(int, raw_input().strip().split())

    # ceil(log2(B)) + 1 <= F
    # => B <= min(15, N-1)
    # => ceil(log2(B)) + 1 <= 5 = F
    size = 1
    while size < 2 * B:
        size *= 2
    size //= 2
    
    segments = []
    while size:  # ceil(log2(B)) + 1 times
        query = []
        if not segments:
            if size == N:
                segments = [(N, N-B)]
                continue
            cnt, flip = N, 0
            while cnt > size:
                query.append(str(flip)*size)
                cnt -= size
                flip ^= 1
            query.append(str(flip)*cnt)
        else:
            is_done = True
            for seg in segments:
                if seg[0] == seg[1] or seg[1] == 0:
                    query.append('0'*seg[0])
                else:
                    is_done = False
                    query.append('0'*((seg[0])//2))
                    query.append('1'*((seg[0]+1)//2))
            if is_done: break

        print "".join(query)
        sys.stdout.flush()
        response = list(raw_input().strip().split()[0])

        if not segments:
            i = 0
            cnt, flip = N, 0
            while cnt > size:
                same_cnt, i = count(response, i, str(flip), size)
                segments.append((size, same_cnt))
                cnt -= size
                flip ^= 1
            same_cnt, i = count(response, i, str(flip), cnt)
            segments.append((cnt, same_cnt))
        else:
            next_segments = []
            i = 0
            for seg in segments:
                if seg[0] == seg[1] or seg[1] == 0:
                    i += seg[1]
                    next_segments.append(seg)
                else:
                    zeros, i = count(response, i, '0', seg[1])
                    ones, i = count(response, i, '1', seg[1]-zeros)
                    next_segments.append(((seg[0])//2, zeros))
                    next_segments.append(((seg[0]+1)//2, ones))
            segments, next_segments = next_segments, segments
        size //= 2

    result, i = [], 0
    for seg in segments:
        if seg[1] == 0:
            for j in xrange(i, i+seg[0]):
                result.append(str(j))
        i += seg[0]

    print " ".join(result)
    sys.stdout.flush()
    verdict = input()
    if verdict == -1:  # error
        exit()

for case in xrange(input()):
    dat_bae()

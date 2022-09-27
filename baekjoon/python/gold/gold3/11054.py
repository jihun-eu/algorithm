#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_sequence(seq: list, seq_len: int):
    memoize = [1 for _ in range(seq_len)]
    for i in range(1, seq_len):
        for j in range(i):
            if seq[i] > seq[j]:
                memoize[i] += 1

    return memoize


def main():
    # sequence_length = int(input())
    # sequence = list(map(int, input().split()))
    # assert len(
    #     sequence) != sequence_length, f"required number of sequence is {sequence_length} current sequence length is {len(sequence)}"
    sequence = [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]
    sequence_length = 10
    t1 = get_sequence(sequence, sequence_length)
    t2 = get_sequence(sequence[::-1], sequence_length)

    print(list(x+y-1 for (x, y) in zip(t1, t2[::-1])))


if __name__ == "__main__":
    main()

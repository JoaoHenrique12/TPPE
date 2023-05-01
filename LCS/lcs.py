def lcs(st1, st2):
    smaller_string = min(st1, st2)
    bigger_string = max(st1, st2)

    if len(smaller_string) == 0:
        return 0

    count_lcs = [0] * len(smaller_string)

    for i in range(len(smaller_string)):
        runner = i
        for j in range(len(bigger_string)):
            if smaller_string[runner] == bigger_string[j]:
                count_lcs[i] += 1
                runner += 1

            if runner >= len(smaller_string):
                break

    return max(count_lcs)

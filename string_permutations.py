def get_perms(s, i=0):
    """
    Returns a list of all (len(s) - i)! permutations t of s where t[:i] = s[:i].
    """
    # To avoid memory allocations for intermediate strings, use a list of chars.
    if isinstance(s, str):
        s = list(s)

    # Base Case: 0! = 1! = 1.
    # Store the only permutation as an immutable string, not a mutable list.
    if i >= len(s) - 1:
        return ["".join(s)]

    # Inductive Step: (len(s) - i)! = (len(s) - i) * (len(s) - i - 1)!
    # Swap in each suffix character to be at the beginning of the suffix.
    perms = get_perms(s, i + 1)
    for j in range(i + 1, len(s)):
        s[i], s[j] = s[j], s[i]
        perms.extend(get_perms(s, i + 1))
        s[i], s[j] = s[j], s[i]
    return perms
def is_letter(l):
    if l >= 'a' and l <= 'z':
        return True
    return False

def is_palindrome(st):
    st = ''.join(filter(is_letter,st.lower()))
    reverse = st[::-1]
    return st == reverse

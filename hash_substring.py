# python3

def read_input():
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
   p_len = len(pattern)
   t_len = len(text)
   p_hash = hash(pattern)
   t_hashes = [hash(text[i:i+p_len]) for i in range(t_len-p_len+1)]
   return [i for i in range(t_len-p_len+1) if t_hashes[i] == p_hash]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


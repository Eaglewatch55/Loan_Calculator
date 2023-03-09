import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file")
args = parser.parse_args()


file = args.file

with open(file) as f:
    encoded_file = f.read()

number = -13


def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)


decode_Caesar_cipher(encoded_file, number)

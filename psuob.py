import sys
import random
import re

def main():
    not_obf = list(sys.argv[1])
    obf = ""
    ps_exec = ["iex "]
    i = 0

    for i in range(len(not_obf)):
        rand_num = random.randint(1, 999999999)
        ps_exec[0] += '$' + str(rand_num)
        not_obf[i] = f'${rand_num}="{not_obf[i]}";'
        obf += '' + not_obf[i]

    print(str(obf.rstrip()))
    print(ps_exec)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} [command]")
        sys.exit(1)
    else:
        main()

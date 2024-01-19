
OFFSET = 25
MIN_PADDING = 4

with open("opcodes.txt") as f:
    lines = f.readlines()
    del lines[0]
    tlines = [l.strip().split("\t") for l in lines]
    seen = set()
    for data in tlines:
        seen.add(int(data[0], base=16))
        if data[1] == "NOP":
            print(f"case {data[0]}: printf(\"%-{OFFSET}s\", \"NOP\"); break;")
        elif data[1] == "-":
            print(f"case {data[0]}: printf(\"%-{OFFSET}s\", \"NOP\"); break;")
        elif len(data) == 5:
            op_name = data[1].split(' ')[0]
            nargs = int(data[2]) - 1
            if nargs == 0:
                print(f"case {data[0]}: printf(\"%-{OFFSET}s;; %-15s\", \"{op_name}\", \"{data[4]}\"); break;")
            elif nargs == 1:
                padding = OFFSET - len(op_name) - 5
                assert(padding >= MIN_PADDING)
                print(f"case {data[0]}: printf(\"%-{len(op_name)}s 0x%02x%{padding}s;; %-15s\", \"{op_name}\", co[1], \"\", \"{data[4]}\"); op_len += {nargs}; break;")
            elif nargs == 2:
                padding = OFFSET - len(op_name) - 7
                assert(padding >= MIN_PADDING)
                print(f"case {data[0]}: printf(\"%-{len(op_name)}s 0x%02x%02x%{padding}s;; %-15s\", \"{op_name}\", co[2], co[1], \"\", \"{data[4]}\"); op_len += {nargs}; break;")
            else:
                raise Exception("WOAH OH")
    for i in range(256):
        if i not in seen:
            print(f"{i} not seen")
    # print(tlines)
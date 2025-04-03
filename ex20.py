from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("まずはファイル全体を印刷しましょう：\n")

print_all(current_file)

print("次に、テープのように巻き戻しましょう。")

rewind(current_file)

print("3行印刷しましょう：")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


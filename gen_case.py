import os
import shutil as sh

print("hello")

FILE = 'test.txt'

def gen_case(file):
    gen_num = 0
    with open(file, 'r') as f:
        lines = f.readlines()
        new_lines = lines
        for i in range(0, len(lines)):
            line = lines[i]
            if '#' in line:
                # It'a line need be modified
                line_m, cases_str = line.split('#')
                assert '=' in line_m
                k, v = line_m.split('=')
                cases = eval(cases_str)
                assert isinstance(cases, (list, range))
                for case in cases:
                    new_case_name = str(k) + '=' + str(case) + '_' + file
                    new_line = str(k) + '=' + str(case) + '\n'
                    new_lines[i] = new_line
                    print(new_case_name)
                    print(new_lines)
                    with open(new_case_name, 'w') as fout:
                        fout.writelines(new_lines)
                gen_num = len(cases)
                break
    if gen_num > 0:
        os.remove(file)
    return gen_num


def gen_cases_folder(folder):
    files = os.listdir(folder)
    assert len(files) < 100
    gen_num = 0
    for file in files:
        gen_num += gen_case(file)
    if gen_num > 0:
        gen_cases_folder(folder)
        # until can not gen

with open(FILE, 'r') as f:
    lines = f.readlines()
    # check is a case need generate
    need_generate = False
    for line in lines:
        if '#' in line:
            need_generate = True
    assert need_generate
    cases_folder = os.getcwd() + '\\' + 'cases'    
    os.mkdir(cases_folder)
    sh.copyfile(FILE, cases_folder + '\\' + FILE)
    os.chdir(cases_folder)
    print(cases_folder)
    gen_cases_folder(cases_folder)
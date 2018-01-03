import sys


def match1(_exp,_comp):
    for i in _exp:
        if i[0] == 'x':
            if i[1:len(i)] == _comp:
                return True
        elif i in _comp:
            return True

        i = i.replace('A','M')
        if i[0] == 'x':
            if i[1:len(i)] == _comp:
                return True
        elif i in _comp:
            return True
    return False

def convert(_ins):
    _ins = _ins.replace('\n','')
    if _ins[0] == "@":                              # A instruction
        a_inst = int(_ins[1:len(_ins)])
        return format(a_inst, '016b') + "\n"
    else:                                           # C instruction
        c_inst = ['0']*16
        c_inst[0] = '1'
        c_inst[1] = '1'
        c_inst[2] = '1'

        dest = ''
        jmp = ''
        comp_start = 0
        comp_end = len(_ins)
        if '=' in _ins:
            dest = _ins[0:_ins.index('=')]
            comp_start = _ins.index('=') + 1
        if ';' in _ins:
            jmp = _ins[_ins.index(';')+1: len(_ins)]
            comp_end = _ins.index(';')

        comp = _ins[comp_start: comp_end]

        # find dest instruction
        if 'A' in dest:
            c_inst[10] = '1'
        if 'D' in dest:
            c_inst[11] = '1'
        if 'M' in dest:
            c_inst[12] = '1'

        # find jump instruction

        if 'L' in jmp or 'NE' in jmp:        # less than or not equal to
            c_inst[13] = '1'
        if 'E' in jmp and 'NE' not in jmp:
            c_inst[14] = '1'
        if 'GT' in jmp or 'GE' in jmp or 'NE' in jmp:
            c_inst[15] = '1'

        if 'MP' in jmp:
            c_inst[13]='1'
            c_inst[14]='1'
            c_inst[15]='1'


        # find comp instruction

        if 'M' in comp:
            c_inst[3] = '1'

        if 'D' not in comp:
            c_inst[4] = '1'

        exp = ['|A', '!A','-A','+1','A-1','D-A','x1','x-1','xA']
        if match1(exp,comp):
            c_inst[5] = '1'

        exp = ['A']
        if not match1(exp,comp):
            c_inst[6] = '1'

        exp = ['x1', 'xD', 'x!D', 'x-D', 'xD+1', 'xA+1', 'xD-1', 'xA-D', 'xD|A' ]
        if match1(exp,comp):
            c_inst[7] = '1'

        exp = ['x0', 'x1', '-', '+']
        if match1(exp,comp):
            c_inst[8] = '1'

        exp = ['x1', '-D', '-A', '+1', '!', '!A', '|']
        if match1(exp,comp):
            c_inst[9] = '1'

        return ''.join(c_inst) + "\n"

def copycontent(source, dest):

    # copy source data to dest after removing whitespaces and comments
    inst = []       # assemble instructions
    minst = []      # machine language instructions
    for line in source:
        if "//" in line:                                # Remove Comments
            line = line[0:line.index("//")]
        line =line.replace(' ','')                      # Remove whitespaces
        if (len(line)>1):                               # Remove empty lines
            inst.append(line)
            # dest.write(line)

    for i in inst:
        minst.append(convert(i))

    for mi in minst:
        dest.write(mi)


if len(sys.argv) < 2:
    print("Enter the file name as parameter:  \n usage: assembler.py program.asm")
asmfilename = sys.argv[1]
asmfile=open(asmfilename,'r')

hackfilename = asmfilename[0:len(asmfilename)-len('.asm')] + ".hack"
hackfile = open(hackfilename,'w');
copycontent(asmfile, hackfile)

def findRelation(n):
    a = {'___': 0, '__R': 1, '__B': 2, '_R_': 3, '_RR': 4, '_RB': 5, '_B_': 6, '_BR': 7, '_BB': 8,
         'R__': 9, 'R_R': 10, 'R_B': 11, 'RR_': 12, 'RRR': 13, 'RRB': 14, 'RB_': 15, 'RBR': 16, 'RBB': 17,
         'B__': 18, 'B_R': 19, 'B_B': 20, 'BR_': 21, 'BRR': 22, 'BRB': 23, 'BB_': 24, 'BBR': 25, 'BBB': 26}

    for color in [["B", "R"]]:
        tempNodes = ["" for i in range(27)]
        color, aColor = color[0], color[1]
        for aColor in [aColor, "_"]:
            for i in ["_", "R", "B"]:
                for j in ["_", "R", "B"]:
                    for k in ["_", "R", "B"]:
                        index = a[i + j + k]
                        if i == color: tempNodes[index] += "nodes[" + str(a[aColor + j + k]) + "]+"
                        if j == color: tempNodes[index] += "nodes[" + str(a[i + aColor + k]) + "]+"
                        if k == color: tempNodes[index] += "nodes[" + str(a[i + j + aColor]) + "]+"
                        if tempNodes[index] == "": tempNodes[index] = "0+"

    for pawn in range(2,n+1):
        if pawn % 2 == 0:
            tempNodes = [
                "0",
                tempNodes[2],
                "0",
                tempNodes[6],
                tempNodes[7] + tempNodes[5] + tempNodes[1] + tempNodes[3],
                tempNodes[8] + tempNodes[2],
                "0",
                tempNodes[8] + tempNodes[6],
                "0",
                tempNodes[18],
                tempNodes[19] + tempNodes[11] + tempNodes[1] + tempNodes[9],
                tempNodes[20] + tempNodes[2],
                tempNodes[21] + tempNodes[15] + tempNodes[3] + tempNodes[9],
                tempNodes[22] + tempNodes[16] + tempNodes[14] + tempNodes[4] + tempNodes[10] + tempNodes[12],
                tempNodes[23] + tempNodes[17] + tempNodes[5] + tempNodes[11],
                tempNodes[24] + tempNodes[6],
                tempNodes[25] + tempNodes[17] + tempNodes[7] + tempNodes[15],
                tempNodes[26] + tempNodes[8],
                "0",
                tempNodes[20] + tempNodes[18],
                "0",
                tempNodes[24] + tempNodes[18],
                tempNodes[25] + tempNodes[23] + tempNodes[19] + tempNodes[21],
                tempNodes[26] + tempNodes[20],
                "0",
                tempNodes[26] + tempNodes[24],
                "0"
            ]
        else:
            tempNodes = [
                "0",
                "0",
                tempNodes[1],
                "0",
                "0",
                tempNodes[4] + tempNodes[3],
                tempNodes[3],
                tempNodes[4] + tempNodes[1],
                tempNodes[5] + tempNodes[7] + tempNodes[2] + tempNodes[6],
                "0",
                "0",
                tempNodes[10] + tempNodes[9],
                "0",
                "0",
                tempNodes[13] + tempNodes[12],
                tempNodes[12] + tempNodes[9],
                tempNodes[13] + tempNodes[10],
                tempNodes[14] + tempNodes[16] + tempNodes[11] + tempNodes[15],
                tempNodes[9],
                tempNodes[10] + tempNodes[1],
                tempNodes[11] + tempNodes[19] + tempNodes[2] + tempNodes[18],
                tempNodes[12] + tempNodes[3],
                tempNodes[13] + tempNodes[4],
                tempNodes[14] + tempNodes[22] + tempNodes[5] + tempNodes[21],
                tempNodes[15] + tempNodes[21] + tempNodes[6] + tempNodes[18],
                tempNodes[16] + tempNodes[22] + tempNodes[7] + tempNodes[19],
                tempNodes[17] + tempNodes[23] + tempNodes[25] + tempNodes[8] + tempNodes[20] + tempNodes[24]
            ]

    for ss, tempNode in enumerate(tempNodes):
        d={k:0 for k in range(27)}
        for i, l in enumerate(tempNode):
            if l=="[":
                if tempNode[i+2]=="]": d[int(tempNode[i+1])]+=1
                else: d[int(tempNode[i+1:i+3])]+=1
        tempNodes[ss]=""
        for i in range(1,27):
            if d[i]==1: tempNodes[ss]+="nodes["+str(i)+"]+"
            elif d[i]!=0: tempNodes[ss]+=str(d[i])+"*nodes["+str(i)+"]+"
        tempNodes[ss]+=","

    print("nodes=[[")
    for tempNode in tempNodes:
        print(tempNode)
    print("]]")

def addBlue(nodes):
    return [
        0,
        0,
        nodes[1] + nodes[0],
        0,
        0,
        nodes[4] + nodes[3],
        nodes[3] + nodes[0],
        nodes[4] + nodes[1],
        nodes[5] + nodes[7] + nodes[2] + nodes[6],
        0,
        0,
        nodes[10] + nodes[9],
        0,
        0,
        nodes[13] + nodes[12],
        nodes[12] + nodes[9],
        nodes[13] + nodes[10],
        nodes[14] + nodes[16] + nodes[11] + nodes[15],
        nodes[9] + nodes[0],
        nodes[10] + nodes[1],
        nodes[11] + nodes[19] + nodes[2] + nodes[18],
        nodes[12] + nodes[3],
        nodes[13] + nodes[4],
        nodes[14] + nodes[22] + nodes[5] + nodes[21],
        nodes[15] + nodes[21] + nodes[6] + nodes[18],
        nodes[16] + nodes[22] + nodes[7] + nodes[19],
        nodes[17] + nodes[23] + nodes[25] + nodes[8] + nodes[20] + nodes[24]
    ]
def addRed(nodes):
    return [
        0,
        nodes[2] + nodes[0],
        0,
        nodes[6] + nodes[0],
        nodes[7] + nodes[5] + nodes[1] + nodes[3],
        nodes[8] + nodes[2],
        0,
        nodes[8] + nodes[6],
        0,
        nodes[18] + nodes[0],
        nodes[19] + nodes[11] + nodes[1] + nodes[9],
        nodes[20] + nodes[2],
        nodes[21] + nodes[15] + nodes[3] + nodes[9],
        nodes[22] + nodes[16] + nodes[14] + nodes[4] + nodes[10] + nodes[12],
        nodes[23] + nodes[17] + nodes[5] + nodes[11],
        nodes[24] + nodes[6],
        nodes[25] + nodes[17] + nodes[7] + nodes[15],
        nodes[26] + nodes[8],
        0,
        nodes[20] + nodes[18],
        0,
        nodes[24] + nodes[18],
        nodes[25] + nodes[23] + nodes[19] + nodes[21],
        nodes[26] + nodes[20],
        0,
        nodes[26] + nodes[24],
        0
    ]

n = int(input())
nn=n

if n == 0: print(0); quit()
if n == 1: print(2); quit()
n-=1
nodes = [0 for i in range(27)]
nodes[2], nodes[6], nodes[18]=1,1,1
while n>=22:
    nodes = addRed(nodes)
    nodes = [
        0,
        nodes[1],
        0,
        nodes[3],
        1023 * nodes[1] + 1023 * nodes[3] + 1024 * nodes[4],
        512 * nodes[1] + 512 * nodes[2] + 511 * nodes[3] + 512 * nodes[5] + 512 * nodes[6] + 512 * nodes[7],
        0,
        511 * nodes[1] + 512 * nodes[2] + 512 * nodes[3] + 512 * nodes[5] + 512 * nodes[6] + 512 * nodes[7],
        0,
        nodes[9],
        1023 * nodes[1] + 1023 * nodes[9] + 1024 * nodes[10],
        512 * nodes[1] + 512 * nodes[2] + 511 * nodes[9] + 512 * nodes[11] + 512 * nodes[18] + 512 * nodes[19],
        1023 * nodes[3] + 1023 * nodes[9] + 1024 * nodes[12],
        57002 * nodes[1] + 57002 * nodes[3] + 58025 * nodes[4] + 57002 * nodes[9] + 58025 * nodes[10] + 58025 * nodes[
            12] + 59049 * nodes[13],
        698026 * nodes[1] + 348502 * nodes[2] + 697516 * nodes[3] + 349525 * nodes[4] + 349014 * nodes[5] + 349013 *
        nodes[6] + 349013 * nodes[7] + 697516 * nodes[9] + 349525 * nodes[10] + 349014 * nodes[11] + 348502 * nodes[
            12] + 349526 * nodes[14] + 349525 * nodes[15] + 349525 * nodes[16] + 349013 * nodes[18] + 349013 * nodes[
            19] + 349525 * nodes[21] + 349525 * nodes[22],
        512 * nodes[3] + 512 * nodes[6] + 511 * nodes[9] + 512 * nodes[15] + 512 * nodes[18] + 512 * nodes[21],
        697516 * nodes[1] + 349013 * nodes[2] + 698026 * nodes[3] + 349525 * nodes[4] + 349013 * nodes[5] + 348502 *
        nodes[6] + 349014 * nodes[7] + 697516 * nodes[9] + 348502 * nodes[10] + 349525 * nodes[11] + 349525 * nodes[
            12] + 349525 * nodes[14] + 349014 * nodes[15] + 349526 * nodes[16] + 349013 * nodes[18] + 349525 * nodes[
            19] + 349013 * nodes[21] + 349525 * nodes[22],
        19171 * nodes[1] + 38854 * nodes[2] + 19171 * nodes[3] + 19683 * nodes[5] + 38854 * nodes[6] + 19683 * nodes[
            7] + 19683 * nodes[8] + 18660 * nodes[9] + 19171 * nodes[11] + 19171 * nodes[15] + 19683 * nodes[
            17] + 38342 * nodes[18] + 19171 * nodes[19] + 19683 * nodes[20] + 19171 * nodes[21] + 19683 * nodes[
            23] + 19683 * nodes[24] + 19683 * nodes[25],
        0,
        511 * nodes[1] + 512 * nodes[2] + 512 * nodes[9] + 512 * nodes[11] + 512 * nodes[18] + 512 * nodes[19],
        0,
        511 * nodes[3] + 512 * nodes[6] + 512 * nodes[9] + 512 * nodes[15] + 512 * nodes[18] + 512 * nodes[21],
        697516 * nodes[1] + 349013 * nodes[2] + 697516 * nodes[3] + 348502 * nodes[4] + 349525 * nodes[5] + 349013 *
        nodes[6] + 349525 * nodes[7] + 698026 * nodes[9] + 349525 * nodes[10] + 349013 * nodes[11] + 349525 * nodes[
            12] + 349525 * nodes[14] + 349013 * nodes[15] + 349525 * nodes[16] + 348502 * nodes[18] + 349014 * nodes[
            19] + 349014 * nodes[21] + 349526 * nodes[22],
        19171 * nodes[1] + 38854 * nodes[2] + 18660 * nodes[3] + 19171 * nodes[5] + 38342 * nodes[6] + 19171 * nodes[
            7] + 19683 * nodes[8] + 19171 * nodes[9] + 19683 * nodes[11] + 19171 * nodes[15] + 19683 * nodes[
            17] + 38854 * nodes[18] + 19683 * nodes[19] + 19683 * nodes[20] + 19171 * nodes[21] + 19683 * nodes[
            23] + 19683 * nodes[24] + 19683 * nodes[25],
        0,
        18660 * nodes[1] + 38342 * nodes[2] + 19171 * nodes[3] + 19171 * nodes[5] + 38854 * nodes[6] + 19171 * nodes[
            7] + 19683 * nodes[8] + 19171 * nodes[9] + 19171 * nodes[11] + 19683 * nodes[15] + 19683 * nodes[
            17] + 38854 * nodes[18] + 19171 * nodes[19] + 19683 * nodes[20] + 19683 * nodes[21] + 19683 * nodes[
            23] + 19683 * nodes[24] + 19683 * nodes[25],
        0,
    ]
    nodes = addBlue(nodes)
    for ii in range(len(nodes)): nodes[ii]%=7340033
    n-=22

for pawn in range(0,n):
    if pawn % 2 == 0: nodes=addRed(nodes)
    else: nodes=addBlue(nodes)

print((nodes[2]+nodes[6]+nodes[9]+nodes[8]+nodes[11]+nodes[15]+nodes[17]) % 7340033)
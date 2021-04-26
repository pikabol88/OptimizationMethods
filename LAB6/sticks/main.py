import math

def main():
    L = 11.7
    lengths = [0.6, 0.68, 0.83, 1.61, 1.67, 1.79, 2.8, 3.25, 3.25, 3.7, 3.95]
    amounts = [249, 60, 97, 76, 72, 18, 43, 5424, 450, 515, 28]
    restrictions = [math.ceil(L / leng) for leng in lengths]

    idxs = list()
    subs = list()

    for idx10 in range(restrictions[10]):
        for idx9 in range(restrictions[9]):
            for idx8 in range(restrictions[8]):
                for idx7 in range(restrictions[7]):
                    for idx6 in range(restrictions[6]):
                        for idx5 in range(restrictions[5]):
                            for idx4 in range(restrictions[4]):
                                for idx3 in range(restrictions[3]):
                                    for idx2 in range(restrictions[2]):
                                        for idx1 in range(restrictions[1]):
                                            for idx0 in range(restrictions[0]):
                                                tmp = lengths[0] * idx0 + lengths[1] * idx1 + lengths[2] * idx2 + lengths[3] * idx3 + lengths[4] * idx4 + lengths[5] * idx5 + lengths[6] * idx7 + lengths[8] * idx8 + lengths[9] * idx9 + lengths[10] * idx10
                                                if tmp <= L:
                                                    idxs.append([idx0, idx1, idx2, idx3, idx4, idx5, idx6, idx7, idx8, idx9, idx10])
                                                    subs.append(L - tmp)

    return

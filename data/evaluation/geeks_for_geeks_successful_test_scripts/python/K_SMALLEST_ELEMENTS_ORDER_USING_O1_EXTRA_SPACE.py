# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n , k ) :
    for i in range ( k , n ) :
        max_var = arr [ k - 1 ]
        pos = k - 1
        for j in range ( k - 2 , - 1 , - 1 ) :
            if ( arr [ j ] > max_var ) :
                max_var = arr [ j ]
                pos = j
        if ( max_var > arr [ i ] ) :
            j = pos
            while ( j < k - 1 ) :
                arr [ j ] = arr [ j + 1 ]
                j += 1
            arr [ k - 1 ] = arr [ i ]
    for i in range ( 0 , k ) :
        print ( arr [ i ] , end = " " )


#TOFILL

if __name__ == '__main__':
    param = [
    ([2, 7, 8, 11, 11, 25, 28, 29, 30, 37, 41, 43, 46, 50, 57, 61, 61, 64, 65, 69, 78, 80, 84, 85, 85, 85, 89, 90, 94, 94, 97],30,19,),
    ([-72, 44, -60, -22, -50, 68, -36, -44, -4, -42, 90, 90, -46, -16, -20, -88, 8, -98, -86, -20, 54, 56, 94, -20, -88, 78, 60, -20, -70, 82, -4],20,27,),
    ([0, 0, 1, 1],3,3,),
    ([54, 37, 29, 37, 71, 91, 91, 79, 60, 38, 63, 54, 91, 9, 14, 43, 12, 98, 46, 62, 89, 56, 44, 82, 11, 17, 94],17,15,),
    ([-94, -94, -92, -82, -80, -70, -70, -64, -62, -60, -60, -58, -52, -14, -8, -6, 2, 4, 12, 16, 18, 20, 36, 38, 42, 48, 60, 66, 78, 78, 84],28,16,),
    ([1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],22,21,),
    ([1, 2, 11, 18, 25, 30, 34, 43, 46, 49, 55, 58, 58, 60, 70, 78, 85, 88, 99],12,17,),
    ([-48, 46, -6, 26, -62, 44, 60, -84, -20, 96, -60, -70, -90, -92, -70, 14, 60, 54, 50, 20, -2, -36, -12, 18],19,21,),
    ([0],0,0,),
    ([4, 99, 78, 78, 91, 14, 32, 3, 23, 37, 19, 45, 14, 55, 74, 15, 68, 79, 88, 31, 20, 72, 55, 37, 72, 81, 83, 53, 32, 64],22,27,)
        ]
    filled_function_param = [
    ([2, 7, 8, 11, 11, 25, 28, 29, 30, 37, 41, 43, 46, 50, 57, 61, 61, 64, 65, 69, 78, 80, 84, 85, 85, 85, 89, 90, 94, 94, 97],30,19,),
    ([-72, 44, -60, -22, -50, 68, -36, -44, -4, -42, 90, 90, -46, -16, -20, -88, 8, -98, -86, -20, 54, 56, 94, -20, -88, 78, 60, -20, -70, 82, -4],20,27,),
    ([0, 0, 1, 1],3,3,),
    ([54, 37, 29, 37, 71, 91, 91, 79, 60, 38, 63, 54, 91, 9, 14, 43, 12, 98, 46, 62, 89, 56, 44, 82, 11, 17, 94],17,15,),
    ([-94, -94, -92, -82, -80, -70, -70, -64, -62, -60, -60, -58, -52, -14, -8, -6, 2, 4, 12, 16, 18, 20, 36, 38, 42, 48, 60, 66, 78, 78, 84],28,16,),
    ([1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],22,21,),
    ([1, 2, 11, 18, 25, 30, 34, 43, 46, 49, 55, 58, 58, 60, 70, 78, 85, 88, 99],12,17,),
    ([-48, 46, -6, 26, -62, 44, 60, -84, -20, 96, -60, -70, -90, -92, -70, 14, 60, 54, 50, 20, -2, -36, -12, 18],19,21,),
    ([0],0,0,),
    ([4, 99, 78, 78, 91, 14, 32, 3, 23, 37, 19, 45, 14, 55, 74, 15, 68, 79, 88, 31, 20, 72, 55, 37, 72, 81, 83, 53, 32, 64],22,27,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))
"""
Provides some tick-tack_tow
"""


borad = [['1','2','3'], ['4','x','6'], ['7','8','9']]

def display_data():
    """Provides some tick-tack_tow"""
    for i in range(0,3):
        print('+-------+-------+-------+')
        print('|   ' + borad[i][0] + '   |   ' + borad[i][1] + '   |    ' + borad[i][2] + '  |')
        print('+-------+-------+-------+')
        
#     print('|   ' + borad[1][0] + '   |   ' + borad[1]
#           [1] + '   |    ' + borad[1][2] + '  |     ')
#     print('+-------+-------+-------+')
#     print('|   ' + borad[2][0] + '   |   ' + borad[2]
#           [1] + '   |    ' + borad[2][2] + '  |     ')
#     print('+-------+-------+-------+')


display_data()

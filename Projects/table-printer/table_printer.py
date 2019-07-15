#! python
# table_printer.py - Displays well-organized table
# with right-justified columns


def print_table(table):

    col_number = len(table)

    # the condition of the problem the number of elements is the same
    row_number = len(table[0])

    # store widths of the longest string in every inner list
    col_width = [0] * col_number

    for i in range(col_number):
        col_width[i] = len(max(table[i], key=len))

    for i in range(row_number):
        for j in range(col_number):
            print(table[j][i].rjust(col_width[j]), end=' ')
        print()


table_data = [
    ['apples', 'oranges', 'cherries', 'bananas'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

print_table(table_data)

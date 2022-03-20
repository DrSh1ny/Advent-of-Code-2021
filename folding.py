def parse_fold(fold_str):
    fold_data = fold_str.strip().split(' ')[-1]
    fold_axis, fold_placement = fold_data.split('=')

    return fold_axis, int(fold_placement)


def fold_page(dots, fold_axis, fold_placement):
    if fold_axis == 'x':
        return fold_left(dots, fold_placement)
    else:
        return fold_up(dots, fold_placement)


def fold_left(dots, fold_placement):
    folded_dots = set()

    for dot in dots:
        if dot[0] > fold_placement:
            folded_dots.add((dot[0] - fold_placement - 1, dot[1]))
        else:
            folded_dots.add((fold_placement - dot[0] - 1, dot[1]))

    return folded_dots


def fold_up(dots, fold_placement):
    folded_dots = set()

    for dot in dots:
        if dot[1] < fold_placement:
            folded_dots.add(dot)
        else:
            folded_dots.add((dot[0], 2 * fold_placement - dot[1]))

    return folded_dots


"""
debug function - used to print out a page
"""
def print_page(dots):
    # We're printing line by line, which means we need to sort dots by Y value
    transposed = sorted((y, x) for x, y in dots)
    page_width = max(map(lambda dot: dot[0], dots))
    page_height = max(map(lambda dot: dot[1], dots))

    next_dot = transposed.pop(0)
    for y in range(page_height + 1):
        row = ''
        for x in range(page_width + 1):
            if next_dot and x == next_dot[1] and y == next_dot[0]:
                row += '#'

                try:
                    next_dot = transposed.pop(0)
                except IndexError:
                    next_dot = None

                continue

            row += '.'

        print(row)
def is_valid(grid, row, col, num):
    # Verifica se o valor não está presente na mesma linha
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Verifica se o valor não está presente na mesma coluna
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Verifica se o valor não está presente no mesmo bloco
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty_cell(grid):
    # Encontra a próxima célula vazia na grade
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None


def solve_sudoku(grid):
    # Encontra a próxima célula vazia
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True

    # Tenta preencher a célula vazia com um valor válido
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            # Chama-se recursivamente até que todas as células sejam preenchidas
            if solve_sudoku(grid):
                return True

            # Se o preenchimento atual não levar a uma solução, limpa a célula e tenta novamente
            grid[row][col] = 0

    # Se nenhum valor válido puder ser colocado na célula atual, retorna False
    return False


# Exemplo de uso:
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

if solve_sudoku(grid):
    for row in grid:
        print(row)
else:
    print("Não há solução para o sudoku fornecido.")

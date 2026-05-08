# чтение трассы с файла
from core.map.MAP import MAP
import numpy as np

def read_trace(file_path) -> list[float]:
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            data.append(float(line.strip()))    
    if not data:
        raise ValueError("Файл пустой!")
    return data

# парсер матриц из текста
def parse_matrix(text: str, m) -> list[list[float]]:
    if m == 'Λ':
        lines = text.strip().splitlines()
        matrix = [float(x) for x in lines]
        if not matrix: 
            raise ValueError(f"Матрица {m} пустая") 
        return matrix

    lines = [line for line in text.strip().splitlines() if line.strip()]  # убираем пустые строки
    matrix = []

    for i, line in enumerate(lines, start=1):
        try:
            row = [float(x) for x in line.split()]
        except ValueError:
            raise ValueError(f"Ошибка в матрице {m} в строке {i}: некорректное число")

        matrix.append(row)
    if not matrix:
       raise ValueError(f"Матрица {m} пустая")

    # Проверка: все строки должны иметь одинаковое количество столбцов
    num_cols = len(matrix[0])
    for i, row in enumerate(matrix, start=1):
        if len(row) != num_cols:
            raise ValueError(f"Ошибка в матрице {m}: разное количество столбцов в строке {i}")

    # Проверка квадратной матрицы
    if len(matrix) != num_cols:
        raise ValueError(f"Матрица {m} не квадратная")

    return np.array(matrix)

def loadMap(path):
    return MAP(name=path)

def info_text(len, characteristics):
    return f"""Всего событий: {len}
Среднее: {characteristics[0]:.6f}
Дисперсия:  {characteristics[1]:.6f}
Коэффициент вариации: {characteristics[2]:.6f}
Коэффициент корреляции: {characteristics[3]:.6f}
Коэффициент асимметрии: {characteristics[4]:.6f}
Коэффициент эксцесса: {characteristics[5]:.6f}
"""
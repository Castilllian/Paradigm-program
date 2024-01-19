import numpy as np

# Определяем функцию для расчета корреляции Пирсона
def pearson_correlation(x, y):
    # Вычисляем средние значения
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Вычисляем ковариацию
    covariance = np.sum((x - mean_x) * (y - mean_y)) / len(x)

    # Вычисляем стандартное отклонение
    std_x = np.std(x)
    std_y = np.std(y)

    # Вычисляем корреляцию
    correlation = covariance / (std_x * std_y)

    return correlation

# Пример использования
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])
correlation_coefficient = pearson_correlation(x, y)
print("Коэффициент корреляции Пирсона:", correlation_coefficient)

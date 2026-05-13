def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        if i == 0:
            row = [1]
        else:
            prev = triangle[i - 1]
            row = [1] + [prev[j] + prev[j + 1] for j in range(len(prev) - 1)] + [1]
        triangle.append(row)
    return triangle

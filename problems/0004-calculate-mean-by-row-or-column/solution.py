def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []

	if mode == 'column':
		for i in range(len(matrix[0])):
			value = 0
			for j in range(len(matrix)):
				value += matrix[j][i]
			means.append(value/len(matrix))
	else:
		for i in range(len(matrix)):
			value = 0
			for j in range(len(matrix[0])):
				value += matrix[i][j]
			means.append(value/len(matrix[0]))
	return means
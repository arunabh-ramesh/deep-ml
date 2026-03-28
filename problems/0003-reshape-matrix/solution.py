import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	numpy_a = np.array(a)
	try:
		reshaped = numpy_a.reshape(new_shape)
	except ValueError:
		return []
	reshaped_matrix = reshaped.tolist()
	return reshaped_matrix
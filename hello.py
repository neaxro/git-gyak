#!/bin/bash

import sum as sum_modul

def main():
	for i in range(1, 10):
		print(i)
		sum = sum_modul.add(i, 10)

		if sum % 2 == 0:
			print("Sum:", sum)
		else:
			print("Sum:", (sum + 1))


if __name__ == '__main__':
	main()

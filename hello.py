#!/bin/bash

import sum

def main():
	for i in range(1, 10):
		print(i)
		print(sum.add(i, 10))


if __name__ == '__main__':
	main()

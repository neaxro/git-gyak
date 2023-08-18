#!/bin/bash

import sum as sum_modul
import person as p

def main():
	alice = p.Person("Alice", 20)
	bob = p.Person("Bob", 21)

	alice.hello()


if __name__ == '__main__':
	main()

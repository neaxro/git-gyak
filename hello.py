#!/bin/bash

import sum as sum_modul
import person as p

def main():
	alice = p.Person("Alice", 22)
	bob = p.Person("Bob", 21)
	jerry = p.Person("Jerry", 31)

	alice.hello()


if __name__ == '__main__':
	main()

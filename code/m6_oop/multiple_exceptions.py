def main():
	try:
		i: str = input("Provide a positive integer: ")
		if (int(i) < 0):
			raise ExceptionGroup("multiple exceptions",
				[ValueError("Can't be negative"),
				 TypeError("Must be an integer")])
	except* ValueError as eg:
		print("I said positive:", eg)
	except* TypeError as eg:
		print("I said integer:", eg)


if __name__ == "__main__":
	main()

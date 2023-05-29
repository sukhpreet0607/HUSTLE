def reverse_digits(num):
	# Initialize reverse number as 0
	rev = 0

	# Check sign of the number
	sign = -1 if num < 0 else 1

	# Take absolute value of the number
	num = abs(num)

	# Reverse the digits
	while num != 0:
		# Get the last digit
		rem = num % 10

		# Remove the last digit from the number
		num = num // 10

		# Check if the reverse number will overflow 32-bit integer
		if rev > 2**31//10 or (rev == 2**31//10 and rem > 7):
			return 0

		# Check if the reverse number will underflow 32-bit integer
		if rev < -2**31//10 or (rev == -2**31//10 and rem < -8):
			return 0

		# Update the reverse number
		rev = rev * 10 + rem

	# Return the reverse number with the original sign
	return sign * rev

if __name__ == '__main__':
	num = 12345
	print("Reverse of no. is", reverse_digits(num))

	num = 1000000045
	print("Reverse of no. is", reverse_digits(num))

from testNumber import testNumber

# Function that takes a sequence of digits and a step as input, and sums the digits that match the digit that is
# the defined number of steps away. The check is circular i.e if the number of steps exceeds the length of the sequence,
# it will go back to the start of the sequence and continue counting.
def captchaDefinedStep(sequence, step):
    sequence = list(sequence)
    total = 0
    length = len(sequence)

    for i in range(0, length):
        if sequence[i] == sequence[(i + step) % length]:
            total += int(sequence[i])

    return total


print(captchaDefinedStep(testNumber, 1))
print(captchaDefinedStep(testNumber, int((len(testNumber) / 2))))

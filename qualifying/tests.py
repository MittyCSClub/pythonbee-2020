import add, pow, times, factorial

def printSuccess(problemName):
    print("Passed all test cases for {}".format(problemName))

if __name__ == "__main__":
    numCorrect = 0

    if (add.f(3, 4) == 7) and (add.f(0, 0) == 0):
        numCorrect += 1
        printSuccess("add")
    if (pow.f(3) == 2393928.502803472) and (pow.f(5) == 2214261750.1479826):
        numCorrect += 1
        printSuccess("pow")
    if (times.f("hi") == "hihi") and (times.f("abc") == "abcabcabc"):
        numCorrect += 1
        printSuccess("times")
    if (factorial.f(0) == 1) and (factorial.f(3) == 6):
        numCorrect += 1
        printSuccess("factorial")
    print("Manually check fizzbuzz")

    print(str(numCorrect) + " problems correct in the qualifying round")

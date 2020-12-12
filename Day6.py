if __name__ == "__main__":
    file = open("Input/CustomsForms.txt","r")
    lines = file.readlines()

    questionAnswers = []
    numTrueAnswers = []

    for line in lines:
        if line != "\n":
            tempQuestionAnswers = [False]*26
            for c in line:
                if c != "\n":
                    tempQuestionAnswers[ord(c)-97] = True

            questionAnswers.append(tempQuestionAnswers)

        else:
            trueAnswers = [True]*26
            for qAnswer in questionAnswers:
                trueAnswers = [a and b for a, b in zip(trueAnswers, qAnswer)]

            numTrueAnswers.append(sum(trueAnswers))
            questionAnswers = []

    trueAnswers = [True] * 26
    for qAnswer in questionAnswers:
        trueAnswers = [a and b for a, b in zip(trueAnswers, qAnswer)]

    numTrueAnswers.append(sum(trueAnswers))
    totalNumTrueAnswer = sum(numTrueAnswers)
    print(totalNumTrueAnswer)


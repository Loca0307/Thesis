
    public static void main(String[] args) {
        int numberOfProblems = 5; // Number of problems to generate
        for (int i = 0; i < numberOfProblems; i++) {
            generateProblem();
        }
    }

    private static void generateProblem() {
        int problemType = random.nextInt(3); // 0: Conversion, 1: Operation, 2: Mixed

        switch (problemType) {
            case 0:
                generateConversionProblem();
                break;
            case 1:
                generateOperationProblem();
                break;
            case 2:
                generateMixedProblem();
                break;
        }
    }

    private static void generateConversionProblem() {
        // Generate a random number in decimal
        int decimalNumber = random.nextInt(100); // Range from 0 to 99
        String targetBase = getBaseString(random.nextInt(3)); // 0: Binary, 1: Octal, 2: Hexadecimal

        System.out.printf("Convert the decimal number %d to %s:\n", decimalNumber, targetBase);
        System.out.print("Your answer: ");
        String answer = scanner.nextLine();
        String correctAnswer = convertDecimal(decimalNumber, targetBase);

        if (answer.equalsIgnoreCase(correctAnswer)) {
            System.out.println("Correct!\n");
        } else {
            System.out.printf("Incorrect. The correct answer is %s.\n\n", correctAnswer);
        }
    }

    private static void generateOperationProblem() {
        // Generate two random numbers in different bases
        int base1 = getRandomBase();
        int base2 = getRandomBase();

        int number1 = random.nextInt(50); // Generate random number for the first base
        int number2 = random.nextInt(50); // Generate random number for the second base

        String base1Str = convertToBase(number1, base1);
        String base2Str = convertToBase(number2, base2);

        System.out.printf("What is %s (%s) + %s (%s)?\n", base1Str, getBaseString(base1), base2Str, getBaseString(base2));
        System.out.print("Your answer (in decimal): ");
        String answer = scanner.nextLine();

        int correctAnswer = convertToDecimal(base1Str, base1) + convertToDecimal(base2Str, base2);

        if (Integer.parseInt(answer) == correctAnswer) {
            System.out.println("Correct!\n");
        } else {
            System.out.printf("Incorrect. The correct answer is %d.\n\n", correctAnswer);
        }
    }

    private static void generateMixedProblem() {
        // Generate a conversion problem followed by an operation
        int decimalNumber = random.nextInt(100);
        String targetBase = getBaseString(random.nextInt(3));
        System.out.printf("Convert the decimal number %d to %s:\n", decimalNumber, targetBase);
        System.out.print("Your answer: ");
        String answer = scanner.nextLine();
        String correctAnswer = convertDecimal(decimalNumber, targetBase);

        if (answer.equalsIgnoreCase(correctAnswer)) {
            System.out.println("Correct!\n");
        } else {
            System.out.printf("Incorrect. The correct answer is %s.\n\n", correctAnswer);
        }

        // Now generate an operation problem
        generateOperationProblem();
    }

    private static String convertDecimal(int number, String targetBase) {
        switch (targetBase) {
            case "Binary":
                return Integer.toBinaryString(number);
            case "Octal":
                return Integer.toOctalString(number);
            case "Hexadecimal":
                return Integer.toHexString(number).toUpperCase();
            default:
                return String.valueOf(number);
        }
    }

    private static int convertToDecimal(String number, int base) {
        return Integer.parseInt(number, base);
    }

    private static String convertToBase(int number, int base) {
        switch (base) {
            case 2:
                return Integer.toBinaryString(number);
            case 8:
                return Integer.toOctalString(number);
            case 16:
                return Integer.toHexString(number).toUpperCase();
            default:
                return String.valueOf(number);
        }
    }

    private static String getBaseString(int baseIndex) {
        switch (baseIndex) {
            case 0:
                return "Binary";
            case 1:
                return "Octal";
            case 2:
                return "Hexadecimal";
            default:
                return "Decimal";
        }
    }

    private static int getRandomBase() {
        return random.nextInt(3) + 2; // Return bases 2 (Binary), 8 (Octal), 16 (Hexadecimal)
    }
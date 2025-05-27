
        
        // Alle Kombinationen berechnen und anzeigen
    

    // Generiert alle Kombinationen aus Additionen und Multiplikationen für die gegebenen Zahlen
    private static List<String> generateCombinations(int[] numbers) {
        List<String> results = new ArrayList<>();
        generateCombinationsHelper(numbers, 1, String.valueOf(numbers[0]), results);
        return results;
    }

    // Hilfsmethode für die rekursive Erzeugung der Kombinationen
    private static void generateCombinationsHelper(int[] numbers, int index, String current, List<String> results) {
        if (index == numbers.length) {
            results.add(current);
            return;
        }

        // Füge Addition hinzu
        generateCombinationsHelper(numbers, index + 1, current + " + " + numbers[index], results);

        // Füge Multiplikation hinzu
        generateCombinationsHelper(numbers, index + 1, current + " * " + numbers[index], results);

        // Füge Kombination von 2 Zahlen hinzu
        generateCombinationsHelper(numbers, index + 1, current + " || " + numbers[index], results);
    }

    // Bewertet eine mathematische Kombination
    private static long evaluateCombination(String combination) {
        String[] tokens = combination.split(" ");
        List<String> postfix = convertToPostfix(tokens);
        return evaluatePostfix(postfix);
    }

    // Wandelt eine Infix-Ausdrucksliste in eine Postfix-Ausdrucksliste um
    private static List<String> convertToPostfix(String[] tokens) {
        List<String> output = new ArrayList<>();
        List<String> operators = new ArrayList<>();

        for (String token : tokens) {
            if (token.matches("\\d+")) {
                output.add(token);
            } else if (token.equals("+") || token.equals("*") || token.equals("||")) {
                //while (!operators.isEmpty() && precedence(operators.get(operators.size() - 1)) >= precedence(token)) {
                while (!operators.isEmpty()) {
                    output.add(operators.remove(operators.size() - 1));
                }
                operators.add(token);
            }
        }

        while (!operators.isEmpty()) {
            output.add(operators.remove(operators.size() - 1));
        }

        return output;
    }

    // Bewertet eine Postfix-Ausdrucksliste
    private static long evaluatePostfix(List<String> postfix) {
        List<Long> stack = new ArrayList<>();

        for (String token : postfix) {
            if (token.matches("\\d+")) {
                stack.add(Long.parseLong(token));
            } else {
                long b = stack.remove(stack.size() - 1);
                long a = stack.remove(stack.size() - 1);
                if (token.equals("+")) {
                    stack.add(a + b);
                } else if (token.equals("*")) {
                    stack.add(a * b);
                } else if (token.equals("||")) {
                    String t = String.valueOf(a) + String.valueOf(b);
                    stack.add(Long.parseLong(t));
                }
            }
        }

        return stack.get(0);
    }

    // Gibt die Operator-Priorität zurück
    private static int precedence(String operator) {
        switch (operator) {
            case "+":
                return 1;
            case "*":
                return 2;
            default:
                return 0;
        }
    }
    
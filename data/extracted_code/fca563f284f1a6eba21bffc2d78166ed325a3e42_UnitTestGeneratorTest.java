

class VariableInitializationModifierTest {

    @Test
    void shouldModifySimpleVariableInitialization() {
        String code = """
            public void testMethod() {
                String test = "old";
                int other = 5;
            }
            """;
        MethodDeclaration method = StaticJavaParser.parseMethodDeclaration(code);
        StringLiteralExpr newValue = new StringLiteralExpr("new");

        VariableInitializationModifier modifier = new VariableInitializationModifier("test", newValue);
        MethodDeclaration result = (MethodDeclaration) modifier.visit(method, null);

        assertTrue(result.toString().contains("String test = \"new\""));
        assertTrue(result.toString().contains("int other = 5"));
    }

    @Test
    void shouldNotModifyWhenVariableNotFound() {
        String code = """
            public void testMethod() {
                String existingVar = "old";
            }
            """;
        MethodDeclaration method = StaticJavaParser.parseMethodDeclaration(code);
        IntegerLiteralExpr newValue = new IntegerLiteralExpr("42");

        VariableInitializationModifier modifier = new VariableInitializationModifier("nonexistentVar", newValue);
        MethodDeclaration result = (MethodDeclaration) modifier.visit(method, null);

        assertEquals(method.toString(), result.toString());
    }

    @Test
    void shouldModifyFirstOccurrenceOnly() {
        String code = """
            public void testMethod() {
                int target = 1;
                String other = "middle";
                int target = 3;
            }
            """;
        MethodDeclaration method = StaticJavaParser.parseMethodDeclaration(code);
        IntegerLiteralExpr newValue = new IntegerLiteralExpr("42");

        VariableInitializationModifier modifier = new VariableInitializationModifier("target", newValue);
        MethodDeclaration result = (MethodDeclaration) modifier.visit(method, null);

        String modifiedCode = result.toString();
        assertTrue(modifiedCode.contains("int target = 42"));
        assertTrue(modifiedCode.contains("int target = 3"));
        assertEquals(1, modifiedCode.split("42").length - 1);
    }
}
    def test_push_pop(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.isEmpty())

    def test_stack_with_initial_elements(self):
        elements = [40, 50, 60]
        stack = Stack(elements)
        self.assertFalse(stack.isEmpty())
        for i, element in enumerate(elements):
            self.assertEqual(stack[i], element)
        self.assertEqual(len(stack.elements), len(elements))

    def test_setitem_getitem(self):
        stack = Stack([70, 80, 90])
        stack[1] = 85
        self.assertEqual(stack[1], 85)

    def test_equality(self):
        stack1 = Stack([100, 200, 300])
        stack2 = Stack([100, 200, 300])
        stack3 = Stack([400, 500, 600])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)

    def test_pop_empty_stack(self):
        stack = Stack()
        with self.assertRaises(StackUnderFlow):
            stack.pop()

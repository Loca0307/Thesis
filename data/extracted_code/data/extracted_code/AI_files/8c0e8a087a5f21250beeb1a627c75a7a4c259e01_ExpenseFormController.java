  /**
   * Sorts the list of expenses by time (timestamp).
   * This uses the natural ordering of Expense objects, which compare by timestamp.
   *
   * @param ascending If true, sorts from oldest to newest. If false, sorts from newest to oldest.
   */
  public void sortExpensesByTime(boolean ascending) {
    Collections.sort(expenses);

    if(!ascending) Collections.reverse(expenses);
  }

  /**
   * Sorts the list of expenses by the associated person.
   * Uses ExpenseComparatorPerson to sort expenses by last name then first name of the person.
   *
   * @param ascending If true, sorts in ascending alphabetical order. If false, sorts in descending order.
   */
  public void sortExpensesByPerson(boolean ascending) {
    expenses.sort(new ExpenseComparatorPerson());

    if(!ascending) Collections.reverse(expenses);
  }

  /**
   * Sorts the list of expenses by status.
   * Uses ExpenseComparatorStatus to sort expenses in the order: PENDING, REJECTED, PAID.
   *
   * @param ascending If true, sorts in the default status order. If false, reverses the order.
   */
  public void sortExpensesByStatus(boolean ascending) {
    expenses.sort(new ExpenseComparatorStatus());

    if(!ascending) Collections.reverse(expenses);
  }

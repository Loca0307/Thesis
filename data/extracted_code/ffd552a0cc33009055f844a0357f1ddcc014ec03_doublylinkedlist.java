    public void deletefirst() {
        if (isempty()) {
            return;
        }
        if (length == 1) { // Handle single-node case
            head = null;
            tail = null;
        } else {
            listnode temp = head.next;
            temp.previous = null;
            head.next = null;
            head = temp;
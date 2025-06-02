package Linked_List;


    // Node class
    class Node {
        int data;
        Node next;

        public Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    // SinglyLinkedList class
    public class L_1_Link {
        Node head; // Head of the list

        // Insert a new node at the end of the list
        public void insert(int data) {
            Node newNode = new Node(data);
            if (head == null) {
                head = newNode; // If the list is empty, the new node becomes the head
            } else {
                Node temp = head;
                while (temp.next != null) {
                    temp = temp.next; // Traverse to the end of the list
                }
                temp.next = newNode; // Link the last node to the new node
            }
        }

        // Display the list
        public void display() {
            Node temp = head;
            while (temp != null) {
                System.out.print(temp.data + " -> ");
                temp = temp.next;
            }
            System.out.println("null");
        }

        // Delete a node by value
        public void delete(int data) {
            if (head == null) return; // If the list is empty, return

            if (head.data == data) {
                head = head.next; // If the head node holds the data, move the head
                return;
            }

            Node temp = head;
            while (temp.next != null && temp.next.data != data) {
                temp = temp.next; // Traverse the list to find the node
            }

            if (temp.next == null) {
                System.out.println("Element not found.");
            } else {
                temp.next = temp.next.next; // Bypass the node to delete it
            }
        }

        public static void main(String[] args) {
            L_1_Link list = new L_1_Link();

            list.insert(10);
            list.insert(20);
            list.insert(30);

            System.out.println("Linked List:");
            list.display(); // Output: 10 -> 20 -> 30 -> null

            list.delete(20);
            System.out.println("After deleting 20:");
            list.display(); // Output: 10 -> 30 -> null
        }
    }


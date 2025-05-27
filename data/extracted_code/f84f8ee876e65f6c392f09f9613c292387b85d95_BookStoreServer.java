import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.List;

public class BookStoreImpl extends UnicastRemoteObject implements BookStore {
    private List<String> books;

    public BookStoreImpl() throws RemoteException {
        super();
        books = new ArrayList<>();
    }

    @Override
    public List<String> getBooks() throws RemoteException {
        return books;
    }

    @Override
    public String getBookDetails(String title) throws RemoteException {
        return "Book: " + title + ", Author: " + "Unknown, " + " Price: " + 0.0;
    }

    @Override
    public boolean addBook(String title, String author, Double price) throws RemoteException {
        books.add(title);
        return true;
    }

}
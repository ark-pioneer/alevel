// Java program to illustrate the concept of Composition
import java.util.*;

class Book {
    String title;
    String author;

    Book(String title, String author) {
        this.title = title;
        this.author = author;
    }
}

class Library {
    private final List<Book> books;

    Library() {
        this.books = new ArrayList<>();
        this.books.add(new Book("Effective Java", "Joshua Bloch"));
        this.books.add(new Book("Thinking in Java", "Bruce Eckel"));
        this.books.add(new Book("Java: The Complete Reference", "Herbert Schildt"));
    }

    public List<Book> getTotalBooksInLibrary() {
        return books;
        }
}

public class CompositionExample {
    public static void main(String[] args) {
        Library library = new Library();
        List<Book> books = library.getTotalBooksInLibrary();
        for (Book book : books) {
            System.out.println("Title: " + book.title + " and Author: " + book.author);
        }
    }
}
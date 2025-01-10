// Java program to illustrate the concept of Aggregation
import java.util.*;

class Student {
    String name;
    int id;
    String dept;

    Student(String name, int id, String dept) {
        this.name = name;
        this.id = id;
        this.dept = dept;
    }
}

class Department {
    String name;
    private List<Student> students;

    Department(String name, List<Student> students) {
        this.name = name;
        this.students = students;
    }

    public List<Student> getStudents() {
        return students;
    }
}

class Institute {
    String instituteName;
    private List<Department> departments;

    Institute(String instituteName, List<Department> departments) {
        this.instituteName = instituteName;
        this.departments = departments;
    }

    public int getTotalStudentsInInstitute() {
        int noOfStudents = 0;
        for (Department dept : departments) {
            noOfStudents += dept.getStudents().size();
        }
        return noOfStudents;
    }
}

public class AggregationExample {
    public static void main(String[] args) {
        Student s1 = new Student("Mia", 1, "CSE");
        Student s2 = new Student("Priya", 2, "CSE");
        Student s3 = new Student("John", 1, "EE");
        Student s4 = new Student("Rahul", 2, "EE");

        List<Student> cse_students = new ArrayList<>();
        cse_students.add(s1);
        cse_students.add(s2);

        List<Student> ee_students = new ArrayList<>();
        ee_students.add(s3);
        ee_students.add(s4);

        Department CSE = new Department("CSE", cse_students);
        Department EE = new Department("EE", ee_students);

        List<Department> departments = new ArrayList<>();
        departments.add(CSE);
        departments.add(EE);

        Institute institute = new Institute("BITS", departments);

        System.out.println("Total students in institute: " + institute.getTotalStudentsInInstitute());
    }
}
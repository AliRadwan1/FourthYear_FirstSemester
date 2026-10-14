
public class Employee {

    private final String ID;
    private final String Firstname;
    private final String Lastname;
    private final int age;
    private final double salary;

    public Employee(String ID, String Firstname, String Lastname, int age, double salary) {
        this.ID = ID;
        this.Firstname = Firstname;
        this.Lastname = Lastname;
        this.age = age;
        this.salary = salary;
    }

    @Override
    public String toString() {
        return "<" + ID + ", " + Firstname + ", " + Lastname + ", " + age + ", " + salary + ">";
    }

}

public class PeopleCounterProgram {
    public static void main(String[] args) {
        PeopleCounter pc = new PeopleCounter();

        // count = 1
        pc.anotherOne();

        System.out.println("Calling countUsingParameter():");

        // Pass reference to the same object
        countUsingParameter(pc);

        System.out.println("Using original PeopleCounter pc:");

        // Same object's count is now 2,
        // so this increases it to 3
        pc.anotherOne();
    }

    public static void countUsingParameter(PeopleCounter counter) {
        System.out.println("Now in countUsingParameter()");

        // Modifies the same PeopleCounter object
        counter.anotherOne();

        System.out.println("Leaving countUsingParameter()");
    }
}

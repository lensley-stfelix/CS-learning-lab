import java.util.Scanner;

class PetsArray {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        String[] petList = {"dog", "cat", "fish"};

        System.out.println("Select a pet: ");
        System.out.println("1. " + petList[0]);
        System.out.println("2. " + petList[1]);
        System.out.println("3. " + petList[2]);

        System.out.print("Enter selection #: ");

        // Declare before try so we can use it later
        int choice = 0;

        // Try to read an integer
        try {
            choice = input.nextInt();
        }
        catch (Exception ex) {
            System.out.println("That is not a number.");
        }

        // Convert human menu number to array index
        choice--;

        // Try to access that array position
        try {
            System.out.println(
                "You selected a " + petList[choice]
            );
        }
        catch (ArrayIndexOutOfBoundsException ex) {
            System.out.println("Not a valid selection.");
        }
    }
}

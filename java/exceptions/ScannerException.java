import java.util.Scanner;

class ScannerException {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int age = 0;

        System.out.print("Please enter your age in years: ");

        try {
            age = input.nextInt();
            System.out.println("You are " + age + " years old.");
        }
        catch (Exception e) {
            System.out.println("Invalid input. Please enter a whole number.");
        }
    }
}

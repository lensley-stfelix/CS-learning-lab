import java.util.Scanner;

class WhileEven {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int number = 0;

        while (number % 2 == 0) {
            System.out.print("Enter a whole number: ");
            number = input.nextInt();
        }

        System.out.println("The loop is done.");
    }
}

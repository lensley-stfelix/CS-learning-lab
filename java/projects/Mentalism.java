// Hello what is your name ?
// Now well perform some mind reading on you.
// Think of a number between 1-10
// Multiply it by 2
// Now add 8 to it
// Now, divide the number by 2
// Now subtract the original number that you thought of
// Let's do some processing
// is the number that you now have 4?

import java.util.Random;
import java.util.Scanner;

public class Mentalism {
  public static void main(String[] args) {
    Random randomGenerator = new Random();
    final int maxValue = 10;
    final int minValue = 1;
    int numberToGuess = randomGenerator.nextInt(maxValue) + minValue;
    int numberToAdd = numberToGuess * 2;
    Scanner keyboardInput = new Scanner(System.in);

    System.out.print("Hello. What is your name? ");
    String name = keyboardInput.nextLine();
    System.out.println("Welcome, " + name + ", we'll perform some mind reading.");
    System.out.println("Think of a number between 1 and 10.");
    System.out.print("Hit Enter/Return when ready for the next step.");
    keyboardInput.nextLine();
    System.out.println("Multiply the number by 2.");
    System.out.print("Hit Enter/Return when ready for the next step.");
    keyboardInput.nextLine();
    System.out.println("Now add " + numberToAdd);
    System.out.print("Hit Enter/Return when ready for the next step.");
    keyboardInput.nextLine();
    System.out.println("Now, divide the number by 2.");
    System.out.print("Hit Enter/Return when ready for the next step.");
    keyboardInput.nextLine();
    System.out.println("Now, subtract the original number that you thought of.");
    System.out.print("Hit Enter/Return when ready for the last step.");
    keyboardInput.nextLine();
    System.out.print("Well, " + name + " let me read your mind... ");
    System.out.println("The number that you have now is " + numberToGuess + ".");
  }
}

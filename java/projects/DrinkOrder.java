import java.util.Scanner;

public class DrinkOrder {

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		System.out.println("What type of drink would you like to order?");
		System.out.println("1. Water\n2. Coffee\n3. Tea");
		System.out.print("Drink selection #: ");

		String drinkDetails = "No drink chosen.";

		int choice = input.nextInt();

		// Clear leftover newline
		input.nextLine();

		if (choice == 1) {

			drinkDetails = "Water";

			System.out.println("Would you like that 1) hot or 2) cold?");
			System.out.print("Enter temperature selection #: ");

			choice = input.nextInt();

			// Clear leftover newline
			input.nextLine();

			if (choice == 1) {

				drinkDetails += ", hot";

			}
			else if (choice == 2) {

				drinkDetails += ", cold";

				System.out.print("Would you like ice? (Y/N) ");

				// Read the user's entire response as a String
				String response = input.nextLine();

				// Extract the first character
				char yesNo = response.charAt(0);

				// Accept uppercase or lowercase Y
				if (yesNo == 'Y' || yesNo == 'y') {

					drinkDetails += ", with ice";
				}
			}
			else {

				System.out.println("Not a valid temperature selection.");
			}
		}
		else if (choice == 2) {

			drinkDetails = "Coffee";

		}
		else if (choice == 3) {

			drinkDetails = "Tea";

		}
		else {

			System.out.println("Sorry, not a valid drink selection.");
		}

		System.out.println("Your drink selection: " + drinkDetails + ".");
	}
}

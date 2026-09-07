import java.util.Scanner;

class Hungry {

	public static void main (String[] args) {

		Scanner input = new Scanner(System.in);

		char hungry;
		char healthy;

		System.out.print("Are you hungry? y or n");

		String response = input.nextLine();

		hungry = response.charAt(0);

		if(hungry == 'n' || hungry == 'N' )
		{
			System.out.print("I'm not hungry");
		}
		else {
			System.out.print("Would you like a healthy meal? y or n:  ");

			response = input.nextLine();

			healthy = response.charAt(0);

			if (healthy == 'n' || healthy == 'N' ) {
				System.out.println("Getting some junk food");
			}
			else {
				System.out.println("Getting a healthy meal.");
			}
		}
	}
}

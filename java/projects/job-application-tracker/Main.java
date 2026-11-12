import java.util.Scanner;

public class Main {

    // Displays the commands available to the user.
    public static void displayMenu() {
        System.out.println("\nJOB APPLICATION TRACKER");
        System.out.println("create - Add a new job application");
        System.out.println("list   - View all job applications");
        System.out.println("update - Update an application's status");
        System.out.println("exit   - Exit the application");
    }

    // Runs the interactive job application tracker.
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        JobTracker tracker = new JobTracker();

        boolean running = true;

        displayMenu();

        while (running) {

            System.out.print("\nEnter command: ");
            String command = scanner.nextLine().trim().toLowerCase();

            if (command.equals("create")) {

                System.out.print("Enter company name: ");
                String company = scanner.nextLine();

                System.out.print("Enter job title: ");
                String title = scanner.nextLine();

                System.out.print("Enter application status: ");
                String status = scanner.nextLine();

                System.out.print("Enter salary: ");
                String salary = scanner.nextLine();

                tracker.createApplication(company, title, status, salary);

            } else if (command.equals("list")) {

                tracker.listApplications();

            } else if (command.equals("update")) {

                System.out.print("Enter company name: ");
                String company = scanner.nextLine();

                System.out.print("Enter job title: ");
                String title = scanner.nextLine();

                System.out.print("Enter new application status: ");
                String newStatus = scanner.nextLine();

                tracker.updateApplication(company, title, newStatus);

            } else if (command.equals("exit")) {

                System.out.println("Exiting Job Application Tracker.");
                running = false;

            } else {

                System.out.println("Invalid command. Please try again.");
            }
        }

        scanner.close();
    }
}
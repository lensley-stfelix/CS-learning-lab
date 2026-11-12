import java.util.ArrayList;

public class JobTracker {

	// Stores job applications during the current program session.
	private ArrayList<JobApplication> applications;

	// Initializes an empty collection for storing applications.
	public JobTracker() {
		applications = new ArrayList<>();
	}

	// Creates and stores a new job application.
	public void createApplication(String company, String title,
	                              String status, String salary) {

		JobApplication newApplication =
		    new JobApplication(company, title, status, salary);

		applications.add(newApplication);

		System.out.println("Application added successfully!");
	}

	// Displays all stored job applications.
	public void listApplications() {

		if (applications.isEmpty()) {
			System.out.println("No applications available.");
		} else {

			int applicationNumber = 1;

			for (JobApplication application : applications) {

				System.out.println("\nApplication " + applicationNumber);
				System.out.println(application);

				applicationNumber++;
			}
		}
	}


	// Finds an existing application and updates its status.
	public void updateApplication(String company, String title, String newStatus) {

		boolean found = false;

		for (JobApplication application : applications) {

			if (application.getCompanyName().trim().equalsIgnoreCase(company.trim())
			        && application.getJobTitle().trim().equalsIgnoreCase(title.trim())) {

				application.updateStatus(newStatus);
				found = true;

				System.out.println("Application status updated successfully!");
				break;
			}
		}

		if (!found) {
			System.out.println("Application not found.");
		}
	}
}
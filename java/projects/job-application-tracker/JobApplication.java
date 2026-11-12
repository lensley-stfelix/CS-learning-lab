public class JobApplication {

    // Stores the details of an individual job application.
    // This is the blueprint for every job application.
    private String companyName;
    private String jobTitle;
    private String applicationStatus;
    private String salary;

    // Initializes a job application with the information provided.
    public JobApplication(String companyName, String jobTitle,
                          String applicationStatus, String salary) {

        this.companyName = companyName;
        this.jobTitle = jobTitle;
        this.applicationStatus = applicationStatus;
        this.salary = salary;
    }

    // Returns the company name.
    public String getCompanyName() {
        return companyName;
    }

    // Returns the job title.
    public String getJobTitle() {
        return jobTitle;
    }

    // Updates the status of an existing job application.
    public void updateStatus(String newStatus) {
        this.applicationStatus = newStatus;
    }

    // Returns the application's information as formatted text.
    @Override
    public String toString() {
        return "Company: " + companyName + "\n"
             + "Job Title: " + jobTitle + "\n"
             + "Status: " + applicationStatus + "\n"
             + "Salary: " + salary;
    }
}
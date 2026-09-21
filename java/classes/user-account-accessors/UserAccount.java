import java.time.LocalDate;

public class UserAccount {
    private String userName;
    private String password;
    private LocalDate dateJoined;
    private boolean activeUser;

    public UserAccount(String userName, String password) {
        this.userName = userName;
        this.password = password;
        this.dateJoined = LocalDate.now();
        this.activeUser = true;
    }

    public String getUserName() {
        return userName;
    }

    public LocalDate getDateJoined() {
        return dateJoined;
    }

    public boolean isActiveUser() {
        return activeUser;
    }

    public void setActiveUser(boolean activeUser) {
        this.activeUser = activeUser;
    }
}

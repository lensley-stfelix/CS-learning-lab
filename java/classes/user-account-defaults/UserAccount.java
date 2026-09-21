import java.time.LocalDate;

public class UserAccount {
    private String userName;
    private String password;

    // These values are automatically established
    private LocalDate dateJoined = LocalDate.now();
    private boolean activeUser = true;

    public UserAccount(String userName, String password) {
        this.userName = userName;
        this.password = password;
    }
}

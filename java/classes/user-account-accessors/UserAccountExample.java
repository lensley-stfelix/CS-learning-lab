public class UserAccountExample {
    public static void main(String[] args) {
        UserAccount account =
            new UserAccount("sophia", "mypass");

        account.setActiveUser(false);

        System.out.println("User name: " + account.getUserName());
        System.out.println("Is active user: " + account.isActiveUser());
        System.out.println("Date joined: " + account.getDateJoined());
    }
}

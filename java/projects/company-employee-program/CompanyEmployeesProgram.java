import java.io.*;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CompanyEmployeesProgram {

    // ========================================
    // MAIN - DIRECTOR OF THE APPLICATION
    // ========================================

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        String cmd = "";

        System.out.print("Enter the name of the CSV file: ");
        String csvFile = input.nextLine();

        // Keep running until user enters "exit"
        while (!cmd.equalsIgnoreCase("exit")) {

            displayMenu();

            cmd = input.nextLine();

            if (cmd.equalsIgnoreCase("list")) {

                listEmployees(csvFile);

            } else if (cmd.equalsIgnoreCase("add")) {

                addEmployees(input, csvFile);

            } else if (cmd.equalsIgnoreCase("del")) {

                System.out.print("Employee ID to delete: ");

                int emplId = input.nextInt();

                // Remove leftover newline
                input.nextLine();

                boolean deleted =
                        deleteEmployee(csvFile, emplId);

                if (deleted) {
                    System.out.println("Employee deleted.");
                } else {
                    System.out.println("Employee not found.");
                }
            }
        }

        System.out.println("Program ended.");

        input.close();
    }


    // ========================================
    // DISPLAY MENU
    // ========================================

    public static void displayMenu() {

        System.out.println("\nlist - List all employees");
        System.out.println(" add - Add an employee");
        System.out.println(" del - Delete an employee");
        System.out.println("exit - Exit program");

        System.out.print("Enter Command: ");
    }


    // ========================================
    // READ
    // CSV FILE -> JAVA OBJECTS
    // ========================================

    public static ArrayList<CompanyEmployee> readEmployees(
            String csvFile) {

        ArrayList<CompanyEmployee> employeeList =
                new ArrayList<>();

        File inputDataFile = new File(csvFile);

        try {

            List<String> lines =
                    Files.readAllLines(inputDataFile.toPath());

            for (String line : lines) {

                String[] employeeData =
                        line.split(",");

                int id =
                        Integer.parseInt(employeeData[0]);

                int salary =
                        Integer.parseInt(employeeData[1]);

                String lastName =
                        employeeData[2];

                String firstName =
                        employeeData[3];

                CompanyEmployee empl =
                        new CompanyEmployee(
                                lastName,
                                firstName,
                                id,
                                salary
                        );

                employeeList.add(empl);
            }

        } catch (IOException ex) {

            System.out.println(
                    "I/O error: " + ex.getMessage()
            );

        } catch (NumberFormatException ex) {

            System.out.println(
                    "Number Format Error: "
                    + ex.getMessage()
            );
        }

        return employeeList;
    }


    // ========================================
    // ADD
    // USER INPUT -> COMPANYEMPLOYEE OBJECTS
    // ========================================

    public static void addEmployees(
            Scanner input,
            String csvFile) {

        ArrayList<CompanyEmployee> employeesToAdd =
                new ArrayList<>();

        char keepGoing = 'Y';

        while (keepGoing == 'Y') {

            System.out.print(
                    "Enter Employee Last Name: "
            );

            String last =
                    input.nextLine();

            System.out.print(
                    "Enter Employee First Name: "
            );

            String first =
                    input.nextLine();

            System.out.print(
                    "Enter Employee ID#: "
            );

            int id =
                    input.nextInt();

            System.out.print(
                    "Enter Salary: "
            );

            int salary =
                    input.nextInt();

            // Remove leftover newline
            input.nextLine();

            CompanyEmployee employee =
                    new CompanyEmployee(
                            last,
                            first,
                            id,
                            salary
                    );

            employeesToAdd.add(employee);

            System.out.print(
                    "Continue adding? (Y/N): "
            );

            keepGoing =
                    Character.toUpperCase(
                            input.nextLine().charAt(0)
                    );
        }

        writeEmployees(
                csvFile,
                employeesToAdd
        );
    }


    // ========================================
    // WRITE
    // JAVA OBJECTS -> CSV FILE
    // ========================================

    public static void writeEmployees(
            String csvFile,
            ArrayList<CompanyEmployee> employees) {

        ArrayList<String> newEmployees =
                new ArrayList<>();

        for (CompanyEmployee empl : employees) {

            String csvLine =
                    empl.getId() + "," +
                    empl.getSalary() + "," +
                    empl.getLastName() + "," +
                    empl.getFirstName();

            newEmployees.add(csvLine);
        }

        File outputFile =
                new File(csvFile);

        try {

            Files.write(
                    outputFile.toPath(),
                    newEmployees,
                    StandardOpenOption.CREATE,
                    StandardOpenOption.APPEND
            );

        } catch (IOException ex) {

            System.out.println(
                    "Error writing to file: "
                    + ex.getMessage()
            );
        }
    }


    // ========================================
    // LIST
    // READ OBJECTS -> DISPLAY THEM
    // ========================================

    public static void listEmployees(
            String csvFile) {

        ArrayList<CompanyEmployee> employees =
                readEmployees(csvFile);

        int menuNumber = 1;

        for (CompanyEmployee empl : employees) {

            System.out.println(
                    menuNumber++ + ". " + empl
            );
        }
    }


    // ========================================
    // DELETE
    // READ -> FIND -> REMOVE -> REWRITE FILE
    // ========================================

    public static boolean deleteEmployee(
            String csvFile,
            int emplID) {

        ArrayList<CompanyEmployee> employees =
                readEmployees(csvFile);

        CompanyEmployee emplToDelete =
                null;

        // Find employee
        for (CompanyEmployee empl : employees) {

            if (empl.getId() == emplID) {

                emplToDelete = empl;

                break;
            }
        }

        // Employee wasn't found
        if (emplToDelete == null) {
            return false;
        }

        // Remove employee from ArrayList
        employees.remove(emplToDelete);

        // Convert remaining objects to CSV Strings
        ArrayList<String> remainingEmployees =
                new ArrayList<>();

        for (CompanyEmployee empl : employees) {

            String csvLine =
                    empl.getId() + "," +
                    empl.getSalary() + "," +
                    empl.getLastName() + "," +
                    empl.getFirstName();

            remainingEmployees.add(csvLine);
        }

        File outputFile =
                new File(csvFile);

        try {

            // Replace old file contents
            // with remaining employees
            Files.write(
                    outputFile.toPath(),
                    remainingEmployees,
                    StandardOpenOption.CREATE,
                    StandardOpenOption.TRUNCATE_EXISTING
            );

            return true;

        } catch (IOException ex) {

            System.out.println(
                    "Error writing to file: "
                    + ex.getMessage()
            );

            return false;
        }
    }
}
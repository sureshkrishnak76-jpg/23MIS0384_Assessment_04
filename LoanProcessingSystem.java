import java.util.Scanner;

public class LoanProcessingSystem {

    // Calculate Debt-to-Income Ratio
    public static double calculateDTI(double salary, double existingLoan) {

        if (salary <= 0) {
            throw new IllegalArgumentException("Invalid salary");
        }

        double existingEMI = existingLoan / 60.0;

        return (existingEMI / salary) * 100;
    }

    // Calculate eligible loan based on employment
    public static double calculateEligibleLoan(
            double salary, String employmentType) {

        if (employmentType.equalsIgnoreCase("Government")) {
            return salary * 20;
        }

        if (employmentType.equalsIgnoreCase("Private")) {
            return salary * 15;
        }

        if (employmentType.equalsIgnoreCase("Self-Employed")) {
            return salary * 12;
        }

        return salary * 10;
    }

    // Calculate interest rate based on credit score
    public static double calculateInterestRate(int creditScore) {

        if (creditScore >= 750) {
            return 7.5;
        }

        if (creditScore >= 650) {
            return 9.0;
        }

        if (creditScore >= 600) {
            return 11.0;
        }

        return 13.0;
    }

    // Calculate EMI
    public static double calculateEMI(
            double loanAmount,
            double annualInterestRate,
            int tenureMonths) {

        if (loanAmount <= 0) {
            throw new IllegalArgumentException(
                    "Invalid loan amount");
        }

        if (tenureMonths <= 0) {
            throw new IllegalArgumentException(
                    "Invalid loan tenure");
        }

        double monthlyRate =
                annualInterestRate / (12 * 100);

        return (loanAmount * monthlyRate *
                Math.pow(1 + monthlyRate, tenureMonths))
                /
                (Math.pow(1 + monthlyRate, tenureMonths) - 1);
    }

    // Loan approval decision
    public static boolean isApproved(
            int age,
            double salary,
            double existingLoan,
            int creditScore,
            double requestedLoan,
            double eligibleLoan,
            double dti) {

        // Age condition
        if (age < 18 || age > 60) {
            return false;
        }

        // Salary condition
        if (salary <= 0) {
            return false;
        }

        // Credit score condition
        if (creditScore < 600) {
            return false;
        }

        // Existing loan threshold
        if (existingLoan > salary * 10) {
            return false;
        }

        // DTI condition
        if (dti > 50) {
            return false;
        }

        // Requested loan condition
        if (requestedLoan > eligibleLoan) {
            return false;
        }

        return true;
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        try {

            System.out.println(
                    "========================================");

            System.out.println(
                    "       BANKING LOAN APPROVAL SYSTEM");

            System.out.println(
                    "========================================");

            // Customer ID
            System.out.print("Customer ID: ");
            String customerId = scanner.nextLine();

            // Age
            System.out.print("Age: ");
            int age = Integer.parseInt(
                    scanner.nextLine());

            // Monthly salary
            System.out.print("Monthly Salary: ");
            double salary = Double.parseDouble(
                    scanner.nextLine());

            // Existing loan
            System.out.print("Existing Loan Amount: ");
            double existingLoan = Double.parseDouble(
                    scanner.nextLine());

            // Credit score
            System.out.print("Credit Score: ");
            int creditScore = Integer.parseInt(
                    scanner.nextLine());

            // Employment type
            System.out.print(
                    "Employment Type " +
                    "(Government/Private/Self-Employed): ");

            String employmentType =
                    scanner.nextLine();

            // Requested loan
            System.out.print(
                    "Requested Loan Amount: ");

            double requestedLoan =
                    Double.parseDouble(
                            scanner.nextLine());

            // Loan tenure
            System.out.print(
                    "Loan Tenure (months): ");

            int tenure =
                    Integer.parseInt(
                            scanner.nextLine());

            // Basic validation
            if (salary <= 0) {
                throw new IllegalArgumentException(
                        "Salary must be greater than zero");
            }

            if (existingLoan < 0) {
                throw new IllegalArgumentException(
                        "Existing loan cannot be negative");
            }

            if (requestedLoan <= 0) {
                throw new IllegalArgumentException(
                        "Requested loan must be greater than zero");
            }

            if (tenure <= 0) {
                throw new IllegalArgumentException(
                        "Loan tenure must be greater than zero");
            }

            // Age validation
            if (age < 18 || age > 60) {

                System.out.println();
                System.out.println(
                        "APPROVAL STATUS: REJECTED");

                System.out.println(
                        "Reason: Age must be between 18 and 60");

                return;
            }

            // Calculations
            double dti =
                    calculateDTI(
                            salary,
                            existingLoan);

            double eligibleLoan =
                    calculateEligibleLoan(
                            salary,
                            employmentType);

            double interestRate =
                    calculateInterestRate(
                            creditScore);

            double emi =
                    calculateEMI(
                            requestedLoan,
                            interestRate,
                            tenure);

            boolean approved =
                    isApproved(
                            age,
                            salary,
                            existingLoan,
                            creditScore,
                            requestedLoan,
                            eligibleLoan,
                            dti);

            // Display results
            System.out.println();
            System.out.println(
                    "========================================");

            System.out.println(
                    "             LOAN DETAILS");

            System.out.println(
                    "========================================");

            System.out.println(
                    "Customer ID     : " + customerId);

            System.out.printf(
                    "DTI             : %.2f%%%n",
                    dti);

            System.out.printf(
                    "Eligible Loan   : %.2f%n",
                    eligibleLoan);

            System.out.printf(
                    "Interest Rate   : %.2f%%%n",
                    interestRate);

            System.out.printf(
                    "EMI             : %.2f%n",
                    emi);

            System.out.println(
                    "Employment      : " + employmentType);

            System.out.println(
                    "Requested Loan  : " + requestedLoan);

            System.out.println(
                    "Tenure          : " + tenure + " months");

            System.out.println(
                    "----------------------------------------");

            if (approved) {

                System.out.println(
                        "APPROVAL STATUS  : APPROVED");

            } else {

                System.out.println(
                        "APPROVAL STATUS  : REJECTED");
            }

            System.out.println(
                    "========================================");

        } catch (NumberFormatException e) {

            System.out.println(
                    "ERROR: Invalid numeric input.");

        } catch (IllegalArgumentException e) {

            System.out.println(
                    "ERROR: " + e.getMessage());

        } catch (Exception e) {

            System.out.println(
                    "ERROR: Unexpected exception.");

        } finally {

            scanner.close();
        }
    }
}

public class LoanProcessingSystem {

    public static double calculateDTI(
            double monthlySalary,
            double existingLoanAmount) {

        if (monthlySalary <= 0) {
            throw new IllegalArgumentException(
                    "Salary must be greater than zero");
        }

        double existingEMI = existingLoanAmount / 60.0;

        return (existingEMI / monthlySalary) * 100;
    }

    public static double calculateEligibleLoan(
            double monthlySalary,
            String employmentType) {

        switch (employmentType.toLowerCase()) {

            case "government":
                return monthlySalary * 20;

            case "private":
                return monthlySalary * 15;

            case "self-employed":
                return monthlySalary * 12;

            default:
                return monthlySalary * 10;
        }
    }

    public static double calculateInterestRate(
            int creditScore) {

        if (creditScore >= 750) {
            return 7.5;
        } else if (creditScore >= 650) {
            return 9.0;
        } else if (creditScore >= 600) {
            return 11.0;
        } else {
            return 13.0;
        }
    }

    public static double calculateEMI(
            double loanAmount,
            double annualInterestRate,
            int tenureMonths) {

        if (loanAmount <= 0 || tenureMonths <= 0) {
            throw new IllegalArgumentException(
                    "Invalid loan amount or tenure");
        }

        double monthlyRate =
                annualInterestRate / (12 * 100);

        return (loanAmount * monthlyRate *
                Math.pow(1 + monthlyRate, tenureMonths))
                /
                (Math.pow(1 + monthlyRate, tenureMonths) - 1);
    }

    public static String processLoan(
            String customerId,
            int age,
            double salary,
            double existingLoan,
            int creditScore,
            String employmentType,
            double requestedLoan,
            int tenure) {

        if (age < 18 || age > 60) {
            return "REJECTED - Invalid age";
        }

        if (salary <= 0) {
            return "REJECTED - Invalid salary";
        }

        if (creditScore < 600) {
            return "REJECTED - Poor credit score";
        }

        if (existingLoan > salary * 10) {
            return "REJECTED - Existing loan exceeds threshold";
        }

        double dti =
                calculateDTI(salary, existingLoan);

        if (dti > 50) {
            return "REJECTED - High DTI";
        }

        double eligibleLoan =
                calculateEligibleLoan(
                        salary,
                        employmentType);

        if (requestedLoan > eligibleLoan) {
            return "REJECTED - Loan exceeds eligibility";
        }

        return "APPROVED";
    }
}

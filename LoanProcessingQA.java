public class LoanProcessingQA {

    static int passed = 0;
    static int failed = 0;

    public static void main(String[] args) {

        System.out.println("========================================");
        System.out.println("       BANKING LOAN APPROVAL - QA");
        System.out.println("========================================");
        System.out.println();

        testMinimumAge();
        testMaximumAge();
        testInvalidAge();
        testInvalidSalary();
        testPoorCreditScore();
        testExistingLoanThreshold();
        testHighDTI();
        testGovernmentEmployment();
        testPrivateEmployment();
        testSelfEmployment();
        testBoundaryLoanAmount();
        testExcessLoanAmount();
        testEMIAccuracy();
        testInvalidInput();
        testExceptionHandling();

        System.out.println();
        System.out.println("========================================");
        System.out.println("             QA TEST SUMMARY");
        System.out.println("========================================");

        System.out.println("TOTAL TESTS : " + (passed + failed));
        System.out.println("PASSED      : " + passed);
        System.out.println("FAILED      : " + failed);

        if (failed == 0) {
            System.out.println("RESULT      : ALL TESTS PASSED");
        } else {
            System.out.println("RESULT      : SOME TESTS FAILED");
        }

        System.out.println("========================================");

        // Make Jenkins fail if any QA test fails
        if (failed > 0) {
            System.exit(1);
        }
    }


    // ============================================================
    // COMMON TEST RESULT METHOD
    // ============================================================

    static void check(
            String testName,
            boolean actual,
            boolean expected) {

        if (actual == expected) {

            passed++;

            System.out.println(
                    testName + " : PASS");

        } else {

            failed++;

            System.out.println(
                    testName + " : FAIL");
        }
    }


    // ============================================================
    // TC01 - MINIMUM AGE
    // ============================================================

    static void testMinimumAge() {

        int age = 18;
        double salary = 50000;
        double existingLoan = 0;
        int creditScore = 750;
        double requestedLoan = 500000;

        double dti =
                LoanProcessingSystem.calculateDTI(
                        salary,
                        existingLoan);

        double eligibleLoan =
                LoanProcessingSystem.calculateEligibleLoan(
                        salary,
                        "Government");

        boolean result =
                LoanProcessingSystem.isApproved(
                        age,
                        salary,
                        existingLoan,
                        creditScore,
                        requestedLoan,
                        eligibleLoan,
                        dti);

        check(
                "TC01 Minimum Age (18)",
                result,
                true);
    }


    // ============================================================
    // TC02 - MAXIMUM AGE
    // ============================================================

    static void testMaximumAge() {

        int age = 60;
        double salary = 50000;
        double existingLoan = 0;
        int creditScore = 750;
        double requestedLoan = 500000;

        double dti =
                LoanProcessingSystem.calculateDTI(
                        salary,
                        existingLoan);

        double eligibleLoan =
                LoanProcessingSystem.calculateEligibleLoan(
                        salary,
                        "Government");

        boolean result =
                LoanProcessingSystem.isApproved(
                        age,
                        salary,
                        existingLoan,
                        creditScore,
                        requestedLoan,
                        eligibleLoan,
                        dti);

        check(
                "TC02 Maximum Age (60)",
                result,
                true);
    }


    // ============================================================
    // TC03 - INVALID AGE
    // ============================================================

    static void testInvalidAge() {

        int age = 17;
        double salary = 50000;
        double existingLoan = 0;
        int creditScore = 750;
        double requestedLoan = 500000;

        double dti =
                LoanProcessingSystem.calculateDTI(
                        salary,
                        existingLoan);

        double eligibleLoan =
                LoanProcessingSystem.calculateEligibleLoan(
                        salary,
                        "Government");

        boolean result =
                LoanProcessingSystem.isApproved(
                        age,
                        salary,
                        existingLoan,
                        creditScore,
                        requestedLoan,
                        eligibleLoan,
                        dti);

        check(
                "TC03 Invalid Age (<18)",
                result,
                false);
    }


    // ============================================================
    // TC04 - INVALID SALARY
    // ============================================================

    static void testInvalidSalary() {

        boolean exceptionThrown = false;

        try {

            LoanProcessingSystem.calculateDTI(
                    -5000,
                    0);

        } catch (IllegalArgumentException e) {

            exceptionThrown = true;
        }

        check(
                "TC04 Invalid Salary",
                exceptionThrown,
                true);
    }


    // ============================================================
    // TC05 - POOR CREDIT SCORE
    // ============================================================

    static void testPoorCreditScore() {

        int age = 30;
        double salary = 50000;
        double existingLoan = 0;
        int creditScore = 500;
        double requestedLoan = 300000;

        double dti =
                LoanProcessingSystem.calculateDTI(
                        salary,
                        existingLoan);

        double eligibleLoan =
                LoanProcessingSystem.calculateEligibleLoan(
                        salary,
                        "Private");

        boolean result =
                LoanProcessingSystem.isApproved(
                        age,
                        salary,
                        existingLoan,
                        creditScore,
                        requestedLoan,
                        eligibleLoan,
                        dti);

        check(
                "TC05 Poor Credit Score",
                result,
                false);
    }


    // ============================================================
    // TC06 - EXISTING LOAN THRESHOLD
    // ============================================================

    static void testExistingLoanThreshold() {

        int age = 30;
        double salary = 50000;
        double existingLoan = 600000;
        int creditScore = 750;
        double requestedLoan = 300000;

        double dti =
                LoanProcessingSystem.calculateDTI(
                        salary,
                        existingLoan);

        double eligibleLoan =
                LoanProcessingSystem.calculateEligibleLoan(
                        salary,
                        "Private");

        boolean result =
                LoanProcessingSystem.isApproved(
                        age,
                        salary,
                        existingLoan,
                        creditScore,
                        requestedLoan,
                        eligibleLoan,
                        dti);

        check(
                "TC06 Existing Loan Threshold",
                result,
                false);
    }


    // ============================================================
    // TC07 - HIGH DTI
    // ============================================================

    static void testHighDTI() {

        int age = 30;
        double salary = 30000;
        double existingLoan = 900000;
        int creditScore = 750;
        double requestedLoan = 200000;

        double dti =
                LoanProcessingSystem.calculateDTI(
                        salary,
                        existingLoan);

        double eligibleLoan =
                LoanProcessingSystem.calculateEligibleLoan(
                        salary,
                        "Private");

        boolean result =
                LoanProcessingSystem.isApproved(
                        age,
                        salary,
                        existingLoan,
                        creditScore,
                        requestedLoan,
                        eligibleLoan,
                        dti);

        check(
                "TC07 High DTI",
                result,
                false);
    }


    // ============================================================
    // TC08 - GOVERNMENT EMPLOYMENT
    // ============================================================

    static void testGovernmentEmployment() {

        double salary = 50000;

        double eligibleLoan =
                LoanProcessingSystem.calculateEligibleLoan(
                        salary,
                        "Government");

        check(
                "TC08 Government Employment",
                eligibleLoan,
                1000000.0);
    }


    // ============================================================
    // TC09 - PRIVATE EMPLOYMENT
    // ============================================================

    static void testPrivateEmployment() {

        double salary = 50000;

        double eligibleLoan =
                LoanProcessingSystem.calculateEligibleLoan(
                        salary,
                        "Private");

        check(
                "TC09 Private Employment",
                eligibleLoan,
                750000.0);
    }


    // ============================================================
    // TC10 - SELF EMPLOYED
    // ============================================================

    static void testSelfEmployment() {

        double salary = 50000;

        double eligibleLoan =
                LoanProcessingSystem.calculateEligibleLoan(
                        salary,
                        "Self-Employed");

        check(
                "TC10 Self-Employed",
                eligibleLoan,
                600000.0);
    }


    // ============================================================
    // TC11 - BOUNDARY LOAN AMOUNT
    // ============================================================

    static void testBoundaryLoanAmount() {

        int age = 30;
        double salary = 50000;
        double existingLoan = 0;
        int creditScore = 750;

        // Government eligible loan = 50,000 × 20
        // = 1,000,000

        double requestedLoan = 1000000;

        double dti =
                LoanProcessingSystem.calculateDTI(
                        salary,
                        existingLoan);

        double eligibleLoan =
                LoanProcessingSystem.calculateEligibleLoan(
                        salary,
                        "Government");

        boolean result =
                LoanProcessingSystem.isApproved(
                        age,
                        salary,
                        existingLoan,
                        creditScore,
                        requestedLoan,
                        eligibleLoan,
                        dti);

        check(
                "TC11 Boundary Loan Amount",
                result,
                true);
    }


    // ============================================================
    // TC12 - EXCESS LOAN AMOUNT
    // ============================================================

    static void testExcessLoanAmount() {

        int age = 30;
        double salary = 50000;
        double existingLoan = 0;
        int creditScore = 750;

        // Private eligible loan = 750,000
        // Requesting 1,000,000 should be rejected

        double requestedLoan = 1000000;

        double dti =
                LoanProcessingSystem.calculateDTI(
                        salary,
                        existingLoan);

        double eligibleLoan =
                LoanProcessingSystem.calculateEligibleLoan(
                        salary,
                        "Private");

        boolean result =
                LoanProcessingSystem.isApproved(
                        age,
                        salary,
                        existingLoan,
                        creditScore,
                        requestedLoan,
                        eligibleLoan,
                        dti);

        check(
                "TC12 Excess Loan Amount",
                result,
                false);
    }


    // ============================================================
    // TC13 - EMI CALCULATION ACCURACY
    // ============================================================

    static void testEMIAccuracy() {

        double loanAmount = 500000;
        double interestRate = 7.5;
        int tenure = 60;

        double actualEMI =
                LoanProcessingSystem.calculateEMI(
                        loanAmount,
                        interestRate,
                        tenure);

        // Expected EMI calculated using
        // the same financial formula

        double monthlyRate =
                interestRate / (12 * 100);

        double expectedEMI =
                (loanAmount * monthlyRate
                        * Math.pow(
                                1 + monthlyRate,
                                tenure))
                /
                (Math.pow(
                        1 + monthlyRate,
                        tenure) - 1);

        boolean result =
                Math.abs(
                        actualEMI - expectedEMI)
                < 0.01;

        check(
                "TC13 EMI Calculation Accuracy",
                result,
                true);

        System.out.printf(
                "    Expected EMI : %.2f%n",
                expectedEMI);

        System.out.printf(
                "    Actual EMI   : %.2f%n",
                actualEMI);
    }


    // ============================================================
    // TC14 - INVALID INPUT
    // ============================================================

    static void testInvalidInput() {

        boolean exceptionThrown = false;

        try {

            LoanProcessingSystem.calculateEMI(
                    -500000,
                    7.5,
                    60);

        } catch (IllegalArgumentException e) {

            exceptionThrown = true;
        }

        check(
                "TC14 Invalid Input",
                exceptionThrown,
                true);
    }


    // ============================================================
    // TC15 - EXCEPTION HANDLING
    // ============================================================

    static void testExceptionHandling() {

        boolean exceptionThrown = false;

        try {

            LoanProcessingSystem.calculateEMI(
                    500000,
                    7.5,
                    0);

        } catch (IllegalArgumentException e) {

            exceptionThrown = true;
        }

        check(
                "TC15 Exception Handling",
                exceptionThrown,
                true);
    }


    // ============================================================
    // DOUBLE VALUE CHECK
    // ============================================================

    static void check(
            String testName,
            double actual,
            double expected) {

        boolean result =
                Math.abs(actual - expected) < 0.01;

        if (result) {

            passed++;

            System.out.printf(
                    "%s : PASS%n",
                    testName);

        } else {

            failed++;

            System.out.printf(
                    "%s : FAIL%n",
                    testName);

            System.out.printf(
                    "    Expected : %.2f%n",
                    expected);

            System.out.printf(
                    "    Actual   : %.2f%n",
                    actual);
        }
    }
}

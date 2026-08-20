import java.io.File;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class LoanProcessingQA {

    static WebDriver driver;

    // Open local index.html
    static String URL =
            new File("index.html").toURI().toString();

    static int passed = 0;
    static int failed = 0;

    public static void main(String[] args) {

        System.setProperty(
                "webdriver.chrome.driver",
                "C:\\Selenium\\chromedriver-win64\\chromedriver.exe"
        );

        driver = new ChromeDriver();

        driver.manage().window().maximize();

        try {

            System.out.println("========================================");
            System.out.println(" BANKING LOAN APPROVAL - SELENIUM QA");
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

            testInvalidTenure();

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

                System.out.println("RESULT      : TESTS FAILED");
            }

            System.out.println("========================================");

        } catch (Exception e) {

            System.out.println();
            System.out.println("QA PROGRAM ERROR: " + e.getMessage());

        } finally {

            driver.quit();
        }
    }

    // ============================================================
    // COMMON FORM FILLING METHOD
    // ============================================================

    static void fillForm(
            String customerId,
            String age,
            String salary,
            String existingLoan,
            String creditScore,
            String employment,
            String requestedLoan,
            String tenure) {

        driver.get(URL);

        driver.findElement(
                By.id("customerId"))
                .sendKeys(customerId);

        driver.findElement(
                By.id("age"))
                .sendKeys(age);

        driver.findElement(
                By.id("salary"))
                .sendKeys(salary);

        driver.findElement(
                By.id("existingLoan"))
                .sendKeys(existingLoan);

        driver.findElement(
                By.id("creditScore"))
                .sendKeys(creditScore);

        // Employment is a SELECT element
        Select employmentSelect =
                new Select(
                        driver.findElement(
                                By.id("employment")));

        employmentSelect.selectByVisibleText(employment);

        driver.findElement(
                By.id("requestedLoan"))
                .sendKeys(requestedLoan);

        driver.findElement(
                By.id("tenure"))
                .sendKeys(tenure);

        driver.findElement(
                By.id("submit"))
                .click();
    }

    // ============================================================
    // GET STATUS
    // ============================================================

    static String getStatus() {

        return driver.findElement(
                By.id("status"))
                .getText()
                .trim();
    }

    // ============================================================
    // PRINT TEST RESULT
    // ============================================================

    static void printResult(
            String testName,
            boolean result) {

        if (result) {

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

        fillForm(
                "C001",
                "18",
                "50000",
                "0",
                "750",
                "Government",
                "500000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.equals("APPROVED");

        printResult(
                "TC01 Minimum Age (18)",
                result);
    }

    // ============================================================
    // TC02 - MAXIMUM AGE
    // ============================================================

    static void testMaximumAge() {

        fillForm(
                "C002",
                "60",
                "50000",
                "0",
                "750",
                "Government",
                "500000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.equals("APPROVED");

        printResult(
                "TC02 Maximum Age (60)",
                result);
    }

    // ============================================================
    // TC03 - INVALID AGE
    // ============================================================

    static void testInvalidAge() {

        fillForm(
                "C003",
                "17",
                "50000",
                "0",
                "750",
                "Government",
                "500000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.contains("REJECTED");

        printResult(
                "TC03 Invalid Age (<18)",
                result);
    }

    // ============================================================
    // TC04 - INVALID SALARY
    // ============================================================

    static void testInvalidSalary() {

        fillForm(
                "C004",
                "30",
                "-5000",
                "0",
                "750",
                "Private",
                "300000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.contains("REJECTED");

        printResult(
                "TC04 Invalid Salary",
                result);
    }

    // ============================================================
    // TC05 - POOR CREDIT SCORE
    // ============================================================

    static void testPoorCreditScore() {

        fillForm(
                "C005",
                "30",
                "50000",
                "0",
                "500",
                "Private",
                "300000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.contains("REJECTED");

        printResult(
                "TC05 Poor Credit Score",
                result);
    }

    // ============================================================
    // TC06 - EXISTING LOAN THRESHOLD
    // ============================================================

    static void testExistingLoanThreshold() {

        fillForm(
                "C006",
                "30",
                "50000",
                "600000",
                "750",
                "Private",
                "300000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.contains("REJECTED");

        printResult(
                "TC06 Existing Loan Threshold",
                result);
    }

    // ============================================================
    // TC07 - HIGH DTI
    // ============================================================

    static void testHighDTI() {

        fillForm(
                "C007",
                "30",
                "30000",
                "900000",
                "750",
                "Private",
                "200000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.contains("REJECTED");

        printResult(
                "TC07 High DTI",
                result);
    }

    // ============================================================
    // TC08 - GOVERNMENT EMPLOYMENT
    // ============================================================

    static void testGovernmentEmployment() {

        fillForm(
                "C008",
                "30",
                "50000",
                "0",
                "750",
                "Government",
                "500000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.equals("APPROVED");

        printResult(
                "TC08 Government Employment",
                result);
    }

    // ============================================================
    // TC09 - PRIVATE EMPLOYMENT
    // ============================================================

    static void testPrivateEmployment() {

        fillForm(
                "C009",
                "30",
                "50000",
                "0",
                "750",
                "Private",
                "500000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.equals("APPROVED");

        printResult(
                "TC09 Private Employment",
                result);
    }

    // ============================================================
    // TC10 - SELF EMPLOYMENT
    // ============================================================

    static void testSelfEmployment() {

        fillForm(
                "C010",
                "30",
                "50000",
                "0",
                "750",
                "Self-Employed",
                "500000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.equals("APPROVED");

        printResult(
                "TC10 Self-Employed",
                result);
    }

    // ============================================================
    // TC11 - BOUNDARY LOAN AMOUNT
    // ============================================================

    static void testBoundaryLoanAmount() {

        /*
         * Government salary = 50000
         *
         * Eligible loan = 50000 × 20
         *               = 1,000,000
         *
         * Requested loan = 1,000,000
         *
         * Exactly equal to eligible amount.
         */

        fillForm(
                "C011",
                "30",
                "50000",
                "0",
                "750",
                "Government",
                "1000000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.equals("APPROVED");

        printResult(
                "TC11 Boundary Loan Amount",
                result);
    }

    // ============================================================
    // TC12 - LOAN ABOVE ELIGIBLE LIMIT
    // ============================================================

    static void testExcessLoanAmount() {

        /*
         * Private salary = 50000
         *
         * Eligible loan = 50000 × 15
         *               = 750000
         *
         * Requested = 1000000
         *
         * Therefore REJECTED.
         */

        fillForm(
                "C012",
                "30",
                "50000",
                "0",
                "750",
                "Private",
                "1000000",
                "60"
        );

        String status = getStatus();

        boolean result =
                status.contains("REJECTED");

        printResult(
                "TC12 Excess Loan Amount",
                result);
    }

    // ============================================================
    // TC13 - EMI ACCURACY
    // ============================================================

    static void testEMIAccuracy() {

        fillForm(
                "C013",
                "30",
                "50000",
                "0",
                "750",
                "Government",
                "500000",
                "60"
        );

        String emiText =
                driver.findElement(
                        By.id("emi"))
                        .getText()
                        .trim();

        /*
         * Loan = 500000
         * Interest = 7.5%
         * Tenure = 60 months
         *
         * Expected EMI ≈ 10018.97
         */

        boolean result = false;

        try {

            String value =
                    emiText.replace(
                            "EMI:",
                            "")
                            .trim();

            double actualEMI =
                    Double.parseDouble(value);

            double expectedEMI =
                    10018.97;

            double tolerance =
                    1.00;

            result =
                    Math.abs(
                            actualEMI - expectedEMI)
                    <= tolerance;

        } catch (Exception e) {

            result = false;
        }

        printResult(
                "TC13 EMI Calculation Accuracy",
                result);
    }

    // ============================================================
    // TC14 - INVALID INPUT
    // ============================================================

    static void testInvalidInput() {

        /*
         * "abc" is not a valid age.
         *
         * HTML5 number input may reject this
         * before Selenium enters it.
         *
         * We therefore verify that the application
         * does NOT produce APPROVED.
         */

        fillForm(
                "C014",
                "abc",
                "50000",
                "0",
                "750",
                "Private",
                "300000",
                "60"
        );

        String status = getStatus();

        boolean result =
                !status.equals("APPROVED");

        printResult(
                "TC14 Invalid Input",
                result);
    }

    // ============================================================
    // TC15 - INVALID TENURE
    // ============================================================

    static void testInvalidTenure() {

        fillForm(
                "C015",
                "30",
                "50000",
                "0",
                "750",
                "Private",
                "300000",
                "0"
        );

        String status = getStatus();

        boolean result =
                status.contains("REJECTED");

        printResult(
                "TC15 Invalid Tenure",
                result);
    }
}

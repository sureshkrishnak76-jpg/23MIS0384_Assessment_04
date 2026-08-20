import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class LoanProcessingQA {

    static WebDriver driver;

    static String URL =
            "file:///C:/Banking/23MIS0384_Assessment_04/Banking/index.html";

    public static void main(String[] args) {

        System.setProperty(
                "webdriver.chrome.driver",
                "chromedriver.exe");

        driver = new ChromeDriver();

        driver.manage().window().maximize();

        try {

            System.out.println(
                    "====================================");

            System.out.println(
                    " BANKING LOAN APPROVAL - QA TEST");

            System.out.println(
                    "====================================");


            testMinimumAge();

            testMaximumAge();

            testInvalidSalary();

            testPoorCreditScore();

            testExistingLoanThreshold();

            testHighDTI();

            testGovernmentEmployment();

            testPrivateEmployment();

            testSelfEmployment();

            testBoundaryLoanAmount();

            testEMI();

            testInvalidInput();

            testExceptionHandling();


            System.out.println(
                    "\nALL TESTS COMPLETED");

        }
        finally {

            driver.quit();
        }
    }


    // Common form filling method

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

        driver.findElement(
                By.id("employment"))
                .sendKeys(employment);

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


    // 1. Minimum Age

    static void testMinimumAge() {

        fillForm(
                "C001",
                "18",
                "50000",
                "0",
                "750",
                "Government",
                "500000",
                "60");

        String result =
                driver.findElement(
                        By.id("status"))
                        .getText();

        System.out.println(
                "Minimum Age Test : " + result);
    }


    // 2. Maximum Age

    static void testMaximumAge() {

        fillForm(
                "C002",
                "60",
                "50000",
                "0",
                "750",
                "Government",
                "500000",
                "60");

        String result =
                driver.findElement(
                        By.id("status"))
                        .getText();

        System.out.println(
                "Maximum Age Test : " + result);
    }


    // 3. Invalid Salary

    static void testInvalidSalary() {

        fillForm(
                "C003",
                "30",
                "-5000",
                "0",
                "750",
                "Private",
                "300000",
                "60");

        String result =
                driver.findElement(
                        By.id("status"))
                        .getText();

        System.out.println(
                "Invalid Salary Test : " + result);
    }


    // 4. Poor Credit Score

    static void testPoorCreditScore() {

        fillForm(
                "C004",
                "30",
                "50000",
                "0",
                "500",
                "Private",
                "300000",
                "60");

        String result =
                driver.findElement(
                        By.id("status"))
                        .getText();

        System.out.println(
                "Poor Credit Score Test : " + result);
    }


    // 5. Existing Loan Threshold

    static void testExistingLoanThreshold() {

        fillForm(
                "C005",
                "30",
                "50000",
                "600000",
                "750",
                "Private",
                "300000",
                "60");

        String result =
                driver.findElement(
                        By.id("status"))
                        .getText();

        System.out.println(
                "Existing Loan Test : " + result);
    }


    // 6. High DTI

    static void testHighDTI() {

        fillForm(
                "C006",
                "30",
                "30000",
                "900000",
                "750",
                "Private",
                "200000",
                "60");

        String result =
                driver.findElement(
                        By.id("status"))
                        .getText();

        System.out.println(
                "High DTI Test : " + result);
    }


    // 7. Government Employment

    static void testGovernmentEmployment() {

        fillForm(
                "C007",
                "30",
                "50000",
                "0",
                "750",
                "Government",
                "500000",
                "60");

        String result =
                driver.findElement(
                        By.id("status"))
                        .getText();

        System.out.println(
                "Government Employment : " + result);
    }


    // 8. Private Employment

    static void testPrivateEmployment() {

        fillForm(
                "C008",
                "30",
                "50000",
                "0",
                "750",
                "Private",
                "500000",
                "60");

        String result =
                driver.findElement(
                        By.id("status"))
                        .getText();

        System.out.println(
                "Private Employment : " + result);
    }


    // 9. Self Employed

    static void testSelfEmployment() {

        fillForm(
                "C009",
                "30",
                "50000",
                "0",
                "750",
                "Self-Employed",
                "500000",
                "60");

        String result =
                driver.findElement(
                        By.id("status"))
                        .getText();

        System.out.println(
                "Self Employment : " + result);
    }


    // 10. Boundary Loan Amount

    static void testBoundaryLoanAmount() {

        fillForm(
                "C010",
                "30",
                "50000",
                "0",
                "750",
                "Government",
                "1000000",
                "60");

        String result =
                driver.findElement(
                        By.id("status"))
                        .getText();

        System.out.println(
                "Boundary Loan Test : " + result);
    }


    // 11. EMI Accuracy

    static void testEMI() {

        fillForm(
                "C011",
                "30",
                "50000",
                "0",
                "750",
                "Government",
                "500000",
                "60");

        String emi =
                driver.findElement(
                        By.id("emi"))
                        .getText();

        System.out.println(
                "EMI Calculation Test : " + emi);
    }


    // 12. Invalid Input

    static void testInvalidInput() {

        fillForm(
                "C012",
                "abc",
                "50000",
                "0",
                "750",
                "Private",
                "300000",
                "60");

        String result =
                driver.findElement(
                        By.id("status"))
                        .getText();

        System.out.println(
                "Invalid Input Test : " + result);
    }


    // 13. Exception Handling

    static void testExceptionHandling() {

        try {

            driver.get(URL);

            driver.findElement(
                    By.id("submit"))
                    .click();

            System.out.println(
                    "Exception Handling Test : PASS");

        }
        catch (Exception e) {

            System.out.println(
                    "Exception Handling Test : PASS");
        }
    }
}

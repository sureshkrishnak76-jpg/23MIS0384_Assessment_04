import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class LoanProcessingQA {

    static WebDriver driver;

    static String URL =
        "file:///C:/YOUR_PATH/23MIS0384_Assessment_04/index.html";


    public static void main(String[] args) {

        System.setProperty(
            "webdriver.chrome.driver",
            "chromedriver.exe"
        );

        driver = new ChromeDriver();

        driver.manage().window().maximize();

        int passed = 0;
        int failed = 0;

        try {

            System.out.println(
                "========================================"
            );

            System.out.println(
                " BANKING LOAN APPROVAL - SELENIUM QA"
            );

            System.out.println(
                "========================================"
            );


            if (testMinimumAge()) passed++;
            else failed++;

            if (testMaximumAge()) passed++;
            else failed++;

            if (testInvalidAge()) passed++;
            else failed++;

            if (testInvalidSalary()) passed++;
            else failed++;

            if (testPoorCreditScore()) passed++;
            else failed++;

            if (testExistingLoan()) passed++;
            else failed++;

            if (testHighDTI()) passed++;
            else failed++;

            if (testGovernmentEmployment()) passed++;
            else failed++;

            if (testPrivateEmployment()) passed++;
            else failed++;

            if (testSelfEmployment()) passed++;
            else failed++;

            if (testBoundaryLoan()) passed++;
            else failed++;

            if (testExcessLoan()) passed++;
            else failed++;

            if (testEMI()) passed++;
            else failed++;

            if (testInvalidInput()) passed++;
            else failed++;

            if (testInvalidTenure()) passed++;
            else failed++;


            System.out.println(
                "\n========================================"
            );

            System.out.println(
                "TOTAL TESTS : " + (passed + failed)
            );

            System.out.println(
                "PASSED      : " + passed
            );

            System.out.println(
                "FAILED      : " + failed
            );

            if (failed == 0) {

                System.out.println(
                    "RESULT      : ALL TESTS PASSED"
                );

            } else {

                System.out.println(
                    "RESULT      : TESTS FAILED"
                );
            }

            System.out.println(
                "========================================"
            );

        } finally {

            driver.quit();
        }
    }


    // Common method

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


    static String getStatus() {

        return driver.findElement(
            By.id("status"))
            .getText();
    }


    // TC01

    static boolean testMinimumAge() {

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

        boolean pass =
            getStatus().equals("APPROVED");

        print("TC01 Minimum Age", pass);

        return pass;
    }


    // TC02

    static boolean testMaximumAge() {

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

        boolean pass =
            getStatus().equals("APPROVED");

        print("TC02 Maximum Age", pass);

        return pass;
    }


    // TC03

    static boolean testInvalidAge() {

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

        boolean pass =
            getStatus().contains("REJECTED");

        print("TC03 Invalid Age", pass);

        return pass;
    }


    // TC04

    static boolean testInvalidSalary() {

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

        boolean pass =
            getStatus().contains("REJECTED");

        print("TC04 Invalid Salary", pass);

        return pass;
    }


    // TC05

    static boolean testPoorCreditScore() {

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

        boolean pass =
            getStatus().contains("REJECTED");

        print("TC05 Poor Credit Score", pass);

        return pass;
    }


    // TC06

    static boolean testExistingLoan() {

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

        boolean pass =
            getStatus().contains("REJECTED");

        print("TC06 Existing Loan Threshold", pass);

        return pass;
    }


    // TC07

    static boolean testHighDTI() {

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

        boolean pass =
            getStatus().contains("REJECTED");

        print("TC07 High DTI", pass);

        return pass;
    }


    // TC08

    static boolean testGovernmentEmployment() {

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

        boolean pass =
            getStatus().equals("APPROVED");

        print("TC08 Government Employment", pass);

        return pass;
    }


    // TC09

    static boolean testPrivateEmployment() {

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

        boolean pass =
            getStatus().equals("APPROVED");

        print("TC09 Private Employment", pass);

        return pass;
    }


    // TC10

    static boolean testSelfEmployment() {

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

        boolean pass =
            getStatus().equals("APPROVED");

        print("TC10 Self-Employed", pass);

        return pass;
    }


    // TC11

    static boolean testBoundaryLoan() {

        // Government eligible loan =
        // 50000 × 20 = 1,000,000

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

        boolean pass =
            getStatus().equals("APPROVED");

        print("TC11 Boundary Loan Amount", pass);

        return pass;
    }


    // TC12

    static boolean testExcessLoan() {

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

        boolean pass =
            getStatus().contains("REJECTED");

        print("TC12 Excess Loan Amount", pass);

        return pass;
    }


    // TC13

    static boolean testEMI() {

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

        String emi =
            driver.findElement(
                By.id("emi"))
                .getText();

        boolean pass =
            emi.startsWith("EMI:");

        print("TC13 EMI Calculation", pass);

        return pass;
    }


    // TC14

    static boolean testInvalidInput() {

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

        boolean pass =
            getStatus().contains("REJECTED");

        print("TC14 Invalid Input", pass);

        return pass;
    }


    // TC15

    static boolean testInvalidTenure() {

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

        boolean pass =
            getStatus().contains("REJECTED");

        print("TC15 Invalid Tenure", pass);

        return pass;
    }


    static void print(
        String testName,
        boolean passed) {

        if (passed) {

            System.out.println(
                testName + " : PASS");

        } else {

            System.out.println(
                testName + " : FAIL");
        }
    }
}

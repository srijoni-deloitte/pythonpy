import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.MediaEntityBuilder;
import com.aventstack.extentreports.Status;
import com.aventstack.extentreports.reporter.ExtentHtmlReporter;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Listeners;

@Listeners(Listener.class)
public class Method_container {
    public Logger log;
    static WebDriver driver;
    static int new_client_id;
    static String FirstName;
    static String LastName;
    static String PinCode;
    static String deposit;
    static String withdraw;
    private static ExtentTest test;
    private ExtentReports extent;
    static int number=1;
    int cur_temp=0;
    List<String> added_prods=new ArrayList<String>();
    int cartTotal=0;



    public static void initialSetup(ExtentTest test,Logger log) throws Exception
    {
        //Loading CSV
        System.out.println("Q:A :- Open Website");
        test.log(Status.INFO,"Starting of test cases Q:A :- Open Website");
        log.info("Q:A :- Open Website");
        System.setProperty("webdriver.chrome.driver", "C:\\\\Users\\\\srijochakraborty\\\\Documents\\\\chromedriver.exe");
        test.pass("Web driver is initialized successfully");
        driver = new ChromeDriver();
        driver.get("https://automatedhuallocation-ui-urtjok3rza-wl.a.run.app");
        Thread.sleep(1000);
        driver.manage().window().maximize();
        log.info("Website is opened and window is Maximized");
        test.pass("Web pages is opened and maximized");

    }
    public void get_temp(ExtentTest test,Logger log) throws Exception{
        WebDriverWait wait = new WebDriverWait(driver, 10);
        test.info("login_using username and password");
        System.out.println("Q:B :- get the login username and password");
        log.info("Q:B :- get the login username and password");
        //Clicked "bank manager login"
        Thread.sleep(2000);
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/div[1]/div/div[1]/div[3]/div[2]"))).click();

        Thread.sleep(2000);
        WebElement email = driver.findElement(By.xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/input"));
        email.sendKeys("gheavens2");
        WebElement pass = driver.findElement(By.xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/form/div[2]/div[2]/div/div/span/input"));
        pass.sendKeys("password");
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/form/div[3]/div/div/div/button"))).click();

        test.pass("logging in");
        log.info("Successfully logged in");
        System.out.println("Successfully logged it");

    }
    public void checkthebutton(ExtentTest test,Logger log) throws Exception{
        WebDriverWait wait = new WebDriverWait(driver, 10);
        test.info("login_using username and password");
        System.out.println("Q:B :- get the login username and password");
        log.info("Q:B :- get the login username and password");

        Thread.sleep(5000);
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[contains(text(),'Section Lead Insights')]"))).click();

        Thread.sleep(2000);
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[contains(text(),'Grades Achieved')]"))).click();

        Thread.sleep(3000);
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[contains(text(),'Marks Alloted')]"))).click();



        JavascriptExecutor jse = (JavascriptExecutor)driver;
        //jse.executeScript("window.scrollBy(0,300)");
        Thread.sleep(2000);
        //jse.executeScript("window.scrollBy(300,0)");

    }
    public  static void checkthepreferencebutton(ExtentTest test,Logger log) throws Exception{
        // Click "Home
        WebDriverWait wait = new WebDriverWait(driver, 10);
        test.info("Q:D :- clicking on preference button" );
        System.out.println("Q:D :- clicking on preference button");
        log.info("Q:D :- clicking on preference button");
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[contains(text(),'Preference Form')]"))).click();
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[contains(text(),'Product Month Preference')]"))).click();
        // Choice 2
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"vertical-tabpanel-1\"]/div/p/div/div[1]/button[2]"))).click();
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[contains(text(),'Survey tool')]"))).click();

        // Choice 1
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"vertical-tabpanel-1\"]/div/p/div/div[1]/button[1]"))).click();
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[contains(text(),'SWIPE')]"))).click();


        // Choice 3
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"vertical-tabpanel-1\"]/div/p/div/div[1]/button[3]"))).click();
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[contains(text(),'Profind')]"))).click();


        //Loggedin as new User
        test.pass("Read Info:- ");
        log.debug("Read Info:- ");
        System.out.println("Read Info:- ");

    }




    public static WebDriver closing(ExtentTest test,Logger log)
    {
        test.info("Browser is closed");
        log.info("Browser is getting closed");
        driver.close();
        extentController.extent.flush();
        return null;
    }
}

import com.aventstack.extentreports.ExtentReports;
import org.apache.logging.log4j.Logger;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterTest;
import org.testng.annotations.Listeners;
import org.testng.annotations.Test;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
@Listeners(Listener.class)
public class AppTest extends Method_container
    {
        Logger log = extentController.log;
        ExtentReports extent = extentController.extent;
        @Test(priority = 1)
        public void A_openTheWebsite() throws Exception {
            ExtentTest Test = extent.createTest("T1");
            initialSetup(Test,log);
        }
        @Test(priority = 2)
        public void get_temper() throws Exception
        {
            ExtentTest Test = extent.createTest("T2");
            get_temp(Test,log);
        }
        @Test(priority=3)
        public void checkthebutton1() throws Exception{
            ExtentTest Test=extent.createTest("T3");
            checkthebutton(Test,log);

        }
        @Test(priority = 4)
        public void checkthepreferencebutton1() throws Exception{
            ExtentTest Test=extent.createTest("T3");
            checkthepreferencebutton(Test,log);

        }



    }


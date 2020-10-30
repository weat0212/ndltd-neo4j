import org.neo4j.driver.AuthTokens;
import org.neo4j.driver.Driver;
import org.neo4j.driver.GraphDatabase;

import java.util.Scanner;

/**
 * @author weat0212@gmail.com
 * @project Thesis
 * @package authentication
 * @date 2020/8/28 下午 05:22
 */
public class BasicAuth implements AutoCloseable{
    private final Driver driver;

    public BasicAuth(String uri){
        System.out.print("Password:");
        Scanner scn = new Scanner(System.in);
        String password = scn.nextLine();
        driver = new <Driver>BasicAuth("neo4j://localhost:7687","neo4j", password).getDriver();
    }

    public BasicAuth(String uri, String user, String password){
        driver = GraphDatabase.driver(uri, AuthTokens.basic(user, password));
    }

    @Override
    public void close() throws Exception {
        driver.close();
    }

    public Driver getDriver(){
        return driver;
    }
}

package transaction;

/**
 * @author weat0212@gmail.com
 * @project Thesis
 * @package dbms.txmanager
 * @date 2020/8/29 下午 01:38
 */

import authentication.BasicAuth;
import org.neo4j.driver.*;

import java.util.Scanner;

import static org.neo4j.driver.Values.parameters;

public class ReadWriteTx {

    private final Driver driver;

    public ReadWriteTx(){
        this.driver = new BasicAuth("neo4j://localhost:7687").getDriver();
    }

    /*Modified to read cypher query*/

    public long addPerson(final String name) {
        try (Session session = driver.session()) {
            session.writeTransaction(new TransactionWork<Void>() {
                @Override
                public Void execute(Transaction tx) {
                    return createPersonNode(tx, name);
                }
            });
            return session.readTransaction(new TransactionWork<Long>() {
                @Override
                public Long execute(Transaction tx) {
                    return matchPersonNode(tx, name);
                }
            });
        }
    }

    private static Void createPersonNode(Transaction tx, String name) {
        tx.run("CREATE (a:Person {name: $name})", parameters("name", name));
        return null;
    }

    private static long matchPersonNode(Transaction tx, String name) {
        Result result = tx.run("MATCH (a:Person {name: $name}) RETURN id(a)", parameters("name", name));
        return result.single().get(0).asLong();
    }
}

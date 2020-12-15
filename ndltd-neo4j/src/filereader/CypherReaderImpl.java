package filereader;

import java.io.FileNotFoundException;
import java.io.IOException;

/**
 * @author I-Chung, Wang
 * @date 2020/12/15 下午 02:09
 */
public class CypherReaderImpl {
    public static void main(String[] args) throws FileNotFoundException, IOException {

        String cypher;
        // Type in the location of cypher file
        CypherReader cypherReader = new CypherReader("C:\\Users\\Andy\\eclipse-workspace\\NDLTD-Neo4j\\cypherscript\\loadcsv.cypher");
        cypher = cypherReader.read();
        System.out.println(cypher);
    }
}

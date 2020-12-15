package filereader;

import java.io.*;

/**
 * @author I-Chung, Wang
 * @date 2020/12/15 下午 01:29
 */


public class CypherReader {

    private String filePath;
    private String cypher = "";

    public CypherReader(String filePath) throws FileNotFoundException {
        this.filePath = filePath;
    }

    public String read() throws IOException {
        String str;

        File file = new File(filePath);
        BufferedReader br = new BufferedReader(new FileReader(file));

        while ((str = br.readLine()) != null) {
            cypher = cypher + str;
        }

        return cypher;
    }

    public String getFilePath() {
        return filePath;
    }

    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }
}


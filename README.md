# NDLTD-Neo4j

1. Python指令負責擷取台灣博碩士論文加值系統中指定的論文，儲存成csv檔
2. csv檔必須放在 {neo4j_home}/import 之下，才可以cypher指令取得
3. 輸入cypher指令約束，單次執行單行
4. 執行讀檔cypher指令

Neo4j讀取檔案成功後，將會以下圖呈現:
![image](https://github.com/weat0212/NDLTD-Neo4j/blob/main/graph.png)

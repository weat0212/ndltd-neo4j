LOAD CSV WITH HEADERS FROM 'file:///MISCCU2.csv' AS row
WITH row WHERE row.Author IS NOT NULL
MERGE (author:Author{authorName:row.Author, authorEngName:row.Author_Eng, degree:row.degree, institution:row.Institution,
        department:row.Department, graduated_academic_year:row.Graduated_Academic_Year}) -
    [:WRITE] ->
    (thesis:Thesis{title:row.Title, title_eng:row.Title_Eng, publication_year:row.Publication_Year, language:row.language,
     number_of_pages:row.number_of_pages, keyword_chi:row.keyword_chi, hits:row.Hits,
     download:row.Download, fav:row.Fav, abstract:row.Abstract, cited:row.Cited, thesis_URL:row.Thesis_URL})

// Professor
MERGE (author) <- [:INSTRUCT] - (professor:Professor{professor_name:row.Advisor})

// Oral_Defense_Committee need split
WITH row, author, professor, thesis
UNWIND split(row.Oral_Defense_Committee, '、') AS odc
MERGE (committee:Professor{professor_name:odc}) - [:ORAL_DEFENSE] -> (thesis)

RETURN author, thesis, professor, committee;

//*****BUG:Professor Reply****
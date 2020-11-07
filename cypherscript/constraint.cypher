// Command should be committed separately
CREATE CONSTRAINT ON (a:Author) ASSERT a.author_name IS UNIQUE;
CREATE CONSTRAINT ON (p:Professor) ASSERT p.professor_name IS UNIQUE;
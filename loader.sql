DROP TABLE PAPERS;

CREATE TABLE PAPERS (
  Title longtext ,
  Ind    INT,
  Venue longtext,
  Year INT,
  WrittenBy longtext,
  Abstract longtext
);
-- insert PAPERS.sql in the given space below

-- fetch desired values
SELECT * FROM PAPERS
Lines = LOAD '/mydata/pig/wordcount/input_data/*.txt' AS (line:chararray);
Words = FOREACH Lines GENERATE FLATTEN(TOKENIZE(line)) As word;
Groups = GROUP Words BY word;
Counts = FOREACH Groups GENERATE group, COUNT(Words);
STORE Counts INTO '/mydata/pig/wordcount/output_data/CountsOozie';
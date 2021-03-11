CREATE TABLE teste(
	testeID SERIAL PRIMARY KEY,
	texto VARCHAR NOT NULL
);
INSERT INTO teste(texto) VALUES ('Teste de texto 1'),('Teste de texto 2');

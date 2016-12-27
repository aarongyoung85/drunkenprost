USE drunkenprost;

CREATE TABLE IF NOT EXISTS `topics` (
	id CHAR(36) NOT NULL,
	topic VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
);

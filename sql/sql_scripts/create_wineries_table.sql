USE drunkenprost;

CREATE TABLE IF NOT EXISTS `wineries` (
	id CHAR(36) NOT NULL DEFAULT '00000000-0000-0000-0000-000000000000',
	winery VARCHAR(100) DEFAULT NULL,
	PRIMARY KEY (id)
);


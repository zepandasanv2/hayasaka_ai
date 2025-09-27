CREATE TABLE IF NOT EXISTS anime (
    id                              INTEGER     PRIMARY KEY AUTOINCREMENT,
    titre                           TEXT        NOT NULL,
    saison                          TEXT,
    episodes                        INTEGER,
    studio                          TEXT
);
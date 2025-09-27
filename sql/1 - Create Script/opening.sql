CREATE TABLE IF NOT EXISTS opening (
    id                                                  INTEGER PRIMARY KEY AUTOINCREMENT,
    anime_id                                            INTEGER NOT NULL,
    numero                                              TEXT,
    titre                                               TEXT,
    artiste                                             TEXT,
    link_url                                            TEXT,
    FOREIGN KEY (anime_id) REFERENCES anime(id)
);
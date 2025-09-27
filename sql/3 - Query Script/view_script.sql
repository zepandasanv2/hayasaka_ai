-- Voir tous les animés
SELECT * FROM anime;

-- Voir tous les openings
SELECT * FROM opening;

-- Voir les animés avec leurs openings
SELECT a.titre AS Anime, o.numero AS Opening, o.titre AS Chanson, o.artiste, o.link_url
FROM opening o
JOIN anime a ON o.anime_id = a.id;

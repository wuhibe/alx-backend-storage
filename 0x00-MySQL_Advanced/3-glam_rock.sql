-- 3. Old school band
-- script that lists all bands with Glam rock as their main style
SELECT DISTINCT band_name, IFNULL(split, 2022) - formed as lifespan
FROM metal_bands WHERE style = 'Glam Rock' ORDER BY lifespan DESC;

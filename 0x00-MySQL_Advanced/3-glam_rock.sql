-- lists all bands with Glam rock as their main style
SELECT band_name , (2022 - formed) AS life_span FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY life_span DESC;

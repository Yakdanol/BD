
car_catalog_Select_All = """
SELECT
--    cc.id_car AS "VIN",
    cc.car_brand AS "Brand",
    cc.car_model AS "Model",
    cc.year_release AS "Year release",
    coc.colour_name AS "Colour",
    cc.car_price AS "Car price",
    cc.car_type AS "Type of car",
    cc.car_condition AS "Car condition",
    cc.car_range AS "Range"
FROM
    car_catalog cc
JOIN
    colour_of_car coc ON cc.id_colour = coc.id_colour
ORDER BY id_car;
"""

dvs_car_Select_All = """
SELECT
--    cc.id_car AS "VIN",
    cc.car_brand AS "Brand",
    cc.car_model AS "Model",
--    cc.year_release AS "Year release",
    cc.car_price AS "Car price",
--    cc.car_type AS "Type of car",
    cc.car_condition AS "Car condition",
    cc.car_range AS "Range",
    dvs.power AS "Power",
    dvs.engine_capacity AS "Engine Capacity",
    dvs.fuel_type AS "Fuel type",
    dvs.ecological_class AS "Ecological class"
FROM
    dvs_car dvs
JOIN
    car_catalog cc ON cc.id_car = dvs.id_car
ORDER BY dvs.id_car;
"""


electric_car_Select_All = """
SELECT *
FROM "electric_car"
"""

hybrid_car_Select_All = """
SELECT *
FROM "hybrid_car"
"""

colour_of_car_Select_All = """
SELECT *
FROM "colour_of_car"
"""

deals_Select_All = """
SELECT *
FROM "deals"
"""

buyers_Select_All = """
SELECT *
FROM "buyers"
"""

all_car_options_Select_All = """
SELECT *
FROM "general_car_options"
"""

options_Select_All = """
SELECT *
FROM "options"
"""
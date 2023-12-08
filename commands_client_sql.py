
car_catalog_Select_All = """
SELECT
    cc.id_car AS "VIN",
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

def find_car_catalog_brand_and_model(brand, model):
     return f"""
    SELECT
        cc.id_car AS "VIN",
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
    WHERE
        car_brand = '{brand}' and car_model = '{model}' 
    
    ORDER BY id_car;
"""

def find_car_catalog_brand(brand):
     return f"""
    SELECT
        cc.id_car AS "VIN",
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
    WHERE
        car_brand = '{brand}'
    
    ORDER BY id_car;
"""

def find_car_catalog_model(model):
     return f"""
    SELECT
        cc.id_car AS "VIN",
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
    WHERE
        car_model = '{model}'
    
    ORDER BY id_car;
"""


dvs_car_Select_All = """
SELECT
    cc.id_car AS "VIN",
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
SELECT
    cc.id_car AS "VIN",
    cc.car_brand AS "Brand",
    cc.car_model AS "Model",
--    cc.year_release AS "Year release",
    cc.car_price AS "Car price",
--    cc.car_type AS "Type of car",
    cc.car_condition AS "Car condition",
    cc.car_range AS "Range",
    elcar.power_electric_engine AS "Power",
    elcar.battery_capacity AS "Battery Capacity"
FROM
    electric_car elcar
JOIN
    car_catalog cc ON cc.id_car = elcar.id_car
ORDER BY elcar.id_car;
"""


hybrid_car_Select_All = """
SELECT
    cc.id_car AS "VIN",
    cc.car_brand AS "Brand",
    cc.car_model AS "Model",
--    cc.year_release AS "Year release",
    cc.car_price AS "Car price",
--    cc.car_type AS "Type of car",
    cc.car_condition AS "Car condition",
    cc.car_range AS "Range",
    hbcar.power_electric_engine AS "Power",
    hbcar.battery_capacity AS "Battery capacity",
    hbcar.power_engine AS "Power engine",
    hbcar.engine_capacity AS "Engine capacity"
FROM
    hybrid_car hbcar
JOIN
    car_catalog cc ON cc.id_car = hbcar.id_car
ORDER BY hbcar.id_car;
"""

def options_select_car (param):
    return f"""
    SELECT
        o.description AS "Option",
        gco.id_option AS "Id option"
    FROM 
        general_car_options gco
    INNER JOIN 
        options o ON gco.id_option = o.id_option
    WHERE gco.id_car = {param};
    """


colour_of_car_Select_All = """
SELECT
colour_name AS "Colour"
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
SELECT 
    options.id_option AS "Number",
    options.description AS "Name of option"
FROM "options"
"""

insert_into_table = """
INSERT INTO
"""

get_price_of_car = """
SELECT car_price
FROM car_catalog
WHERE id_car = 
"""
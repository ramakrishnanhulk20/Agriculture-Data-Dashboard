select *
from agriculture_data;

-- 1.Year-wise Trend of Rice Production Across States (Top 3)

select `State Name`, sum(`RICE PRODUCTION (1000 tons)`) as pro
from agriculture_data
group by `State Name`
order by pro desc
limit 3; 

select `Year`, `State Name`, sum(`RICE PRODUCTION (1000 tons)`) as pro
from agriculture_data
where `State Name` in ("West Bengal", "Uttar Pradesh", "Punjab")
group by `State Name`, `Year`
order by `Year` desc, `State Name`;


-- 2.Top 5 Districts by Wheat Yield Increase Over the Last 5 Years

select `Dist Name`, sum(`WHEAT YIELD (Kg per ha)`) as total_wheat_yield
from agriculture_data
group by `Dist Name`;
-- Ludhiana Sangrur Patiala Jalandhar Ferozpur

select `Dist Name`, `Year`, sum(`WHEAT YIELD (Kg per ha)`) as total_wheat_yield
from agriculture_data
where `Dist Name` in ("Ludhiana", "Sangrur", "Patiala", "Jalandhar", "Ferozpur") and `Year` between 2013 and 2017
group by `Dist Name`, `Year`
order by `Year` desc, `Dist Name`;

-- 3.States with the Highest Growth in Oilseed Production (5-Year Growth Rate)

select `State Name`, `Year`, sum(`OILSEEDS PRODUCTION (1000 tons)`) as total_oil_seed_production
from agriculture_data
where `Year` between 2013 and 2017
group by `State Name`, `Year`
order by `Year` asc, `State Name`;

-- 4.District-wise Correlation Between Area and Production for Major Crops (Rice, Wheat, and Maize)

select 
  `Dist Name`,
  (COUNT(*) * SUM(`RICE AREA (1000 ha)` * `RICE PRODUCTION (1000 tons)`) -- Pearon Correlation Formula
   - SUM(`RICE AREA (1000 ha)`) * SUM(`RICE PRODUCTION (1000 tons)`)) 
  / 
  SQRT(
    (COUNT(*) * SUM(POWER(`RICE AREA (1000 ha)`, 2)) - POWER(SUM(`RICE AREA (1000 ha)`), 2)) *
    (COUNT(*) * SUM(POWER(`RICE PRODUCTION (1000 tons)`, 2)) - POWER(SUM(`RICE PRODUCTION (1000 tons)`), 2))
  ) as Rice_Area_Vs_Production_Correlation,
  (COUNT(*) * SUM(`WHEAT AREA (1000 ha)` * `WHEAT PRODUCTION (1000 tons)`) 
   - SUM(`WHEAT AREA (1000 ha)`) * SUM(`WHEAT PRODUCTION (1000 tons)`)) 
  / 
  SQRT(
    (COUNT(*) * SUM(POWER(`WHEAT AREA (1000 ha)`, 2)) - POWER(SUM(`WHEAT AREA (1000 ha)`), 2)) *
    (COUNT(*) * SUM(POWER(`WHEAT PRODUCTION (1000 tons)`, 2)) - POWER(SUM(`WHEAT PRODUCTION (1000 tons)`), 2))
  ) as Wheat_Area_Vs_Production_Correlation,
  (COUNT(*) * SUM(`MAIZE AREA (1000 ha)` * `MAIZE PRODUCTION (1000 tons)`) 
   - SUM(`MAIZE AREA (1000 ha)`) * SUM(`MAIZE PRODUCTION (1000 tons)`)) 
  / 
  SQRT(
    (COUNT(*) * SUM(POWER(`MAIZE AREA (1000 ha)`, 2)) - POWER(SUM(`MAIZE AREA (1000 ha)`), 2)) *
    (COUNT(*) * SUM(POWER(`MAIZE PRODUCTION (1000 tons)`, 2)) - POWER(SUM(`MAIZE PRODUCTION (1000 tons)`), 2))
  ) as Maize_Area_Vs_Production_Correlation
from agriculture_data
group by `Dist Name`;

-- 5.Yearly Production Growth of Cotton in Top 5 Cotton Producing States

select `State Name`, sum(`COTTON PRODUCTION (1000 tons)`) as total_cotton_production
from agriculture_data
group by `State Name`; 
-- Gujarat Maharashtra Punjab Haryana Telangana

select `State Name`, `Year`, sum(`COTTON PRODUCTION (1000 tons)`) as total_cotton_production
from agriculture_data
where `State Name` in ("Gujarat", "Maharashtra", "Punjab", "Haryana", "Telangana")
group by `Year`, `State Name`
order by `Year` desc, `State Name`;

-- 6.Districts with the Highest Groundnut Production in 2020

select `Dist Name`, SUM(`GROUNDNUT PRODUCTION (1000 tons)`) AS total_groundnut_production
from agriculture_data
where `Year` = 2020
group by `Dist Name`
order by total_groundnut_production desc; -- Returns an empty table cause we don't have data for the year 2020

-- 7.Annual Average Maize Yield Across All States

select `State Name`, `Year`, avg(`MAIZE YIELD (Kg per ha)`) as avg_maize_yield
from agriculture_data
group by `State Name`, `Year`
order by `Year` desc;

-- 8.Total Area Cultivated for Oilseeds in Each State

select `State Name`, sum(`OILSEEDS AREA (1000 ha)`) as total_area_oilseeds
from agriculture_data
group by `State Name`
order by total_area_oilseeds desc;

-- 9.Districts with the Highest Rice Yield

select `Dist Name`, sum(`RICE YIELD (Kg per ha)`) as total_rice_yield
from agriculture_data
group by `Dist Name`
order by total_rice_yield desc;

-- 10.Compare the Production of Wheat and Rice for the Top 5 States Over 10 Years

select `State Name`, SUM(`WHEAT PRODUCTION (1000 tons)`), SUM(`RICE PRODUCTION (1000 tons)`), SUM(`WHEAT PRODUCTION (1000 tons)` + `RICE PRODUCTION (1000 tons)`) as total
from agriculture_data
where `Year` between 2007 and 2017
group by `State Name`
order by total desc;
-- Uttar Pradesh Punjab Madhya Pradesh West Bengal Haryana

select `State Name`, `Year`, sum(`RICE PRODUCTION (1000 tons)`) as total_rice_production, sum(`WHEAT PRODUCTION (1000 tons)`) as total_wheat_production
from agriculture_data
where `State Name` in ("Uttar Pradesh", "Punjab", "Madhya Pradesh", "West Bengal", "Haryana") and `Year` between 2007 and 2017
group by `State Name`, `Year`
order by `Year` desc, `State Name`;










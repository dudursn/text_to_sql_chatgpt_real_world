ALTER TABLE borders ADD CONSTRAINT borders_country_fk FOREIGN KEY (country1) REFERENCES country(code)

ALTER TABLE borders ADD CONSTRAINT borders_country_fk FOREIGN KEY (country2) REFERENCES country(code)

ALTER TABLE ethnicgroup ADD CONSTRAINT ethnicgroup_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE airport ADD CONSTRAINT airport_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE city ADD CONSTRAINT city_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE citylocalname ADD CONSTRAINT citylocalname_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE cityothername ADD CONSTRAINT cityothername_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE citypops ADD CONSTRAINT citypops_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE countrylocalname ADD CONSTRAINT countrylocalname_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE countryothername ADD CONSTRAINT countryothername_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE countrypops ADD CONSTRAINT countrypops_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE economy ADD CONSTRAINT economy_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE encompasses ADD CONSTRAINT encompasses_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE geo_desert ADD CONSTRAINT geo_desert_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE geo_estuary ADD CONSTRAINT geo_estuary_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE geo_island ADD CONSTRAINT geo_island_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE geo_lake ADD CONSTRAINT geo_lake_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE geo_mountain ADD CONSTRAINT geo_mountain_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE geo_river ADD CONSTRAINT geo_river_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE geo_sea ADD CONSTRAINT geo_sea_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE geo_source ADD CONSTRAINT geo_source_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE ismember ADD CONSTRAINT ismember_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE language ADD CONSTRAINT language_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE located ADD CONSTRAINT located_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE locatedon ADD CONSTRAINT locatedon_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE organization ADD CONSTRAINT organization_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE politics ADD CONSTRAINT politics_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE population ADD CONSTRAINT population_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE province ADD CONSTRAINT province_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE provincelocalname ADD CONSTRAINT provincelocalname_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE provinceothername ADD CONSTRAINT provinceothername_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE provpops ADD CONSTRAINT provpops_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE religion ADD CONSTRAINT religion_country_fk FOREIGN KEY (country) REFERENCES country(code)

ALTER TABLE airport ADD CONSTRAINT airport_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE city ADD CONSTRAINT city_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE citylocalname ADD CONSTRAINT citylocalname_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE cityothername ADD CONSTRAINT cityothername_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE citypops ADD CONSTRAINT citypops_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE geo_desert ADD CONSTRAINT geo_desert_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE geo_estuary ADD CONSTRAINT geo_estuary_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE geo_island ADD CONSTRAINT geo_island_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE geo_lake ADD CONSTRAINT geo_lake_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE geo_mountain ADD CONSTRAINT geo_mountain_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE geo_river ADD CONSTRAINT geo_river_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE geo_sea ADD CONSTRAINT geo_sea_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE geo_source ADD CONSTRAINT geo_source_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE located ADD CONSTRAINT located_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE locatedon ADD CONSTRAINT locatedon_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE organization ADD CONSTRAINT organization_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE provincelocalname ADD CONSTRAINT provincelocalname_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE provinceothername ADD CONSTRAINT provinceothername_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE provpops ADD CONSTRAINT provpops_province_country_fk FOREIGN KEY(province, country) REFERENCES province (name, country)

ALTER TABLE airport ADD CONSTRAINT airport_city_province_fk FOREIGN KEY(city, province, country) REFERENCES city (name, province, country) 

ALTER TABLE citylocalname ADD CONSTRAINT citylocalname_city_province_fk FOREIGN KEY(city, province, country) REFERENCES city (name, province, country) 

ALTER TABLE cityothername ADD CONSTRAINT cityothername_city_province_fk FOREIGN KEY(city, province, country) REFERENCES city (name, province, country) 

ALTER TABLE citypops ADD CONSTRAINT citypops_city_province_fk FOREIGN KEY(city, province, country) REFERENCES city (name, province, country) 

ALTER TABLE located ADD CONSTRAINT located_city_province_fk FOREIGN KEY(city, province, country) REFERENCES city (name, province, country) 

ALTER TABLE locatedon ADD CONSTRAINT locatedon_city_province_fk FOREIGN KEY(city, province, country) REFERENCES city (name, province, country) 

ALTER TABLE organization ADD CONSTRAINT organization_city_province_fk FOREIGN KEY(city, province, country) REFERENCES city (name, province, country) 

ALTER TABLE mergeswith ADD CONSTRAINT mergeswith_sea1_fk FOREIGN KEY (sea1) REFERENCES sea(name);

ALTER TABLE mergeswith ADD CONSTRAINT mergeswith_sea2_fk FOREIGN KEY (sea2) REFERENCES sea(name);

ALTER TABLE ismember ADD CONSTRAINT ismember_organization_fk FOREIGN KEY (organization) REFERENCES organization(abbreviation)

ALTER TABLE islandin ADD CONSTRAINT islandin_sea_fk FOREIGN KEY(sea) REFERENCES sea(name)

ALTER TABLE river ADD CONSTRAINT river_sea_fk FOREIGN KEY(sea) REFERENCES sea(name)

ALTER TABLE geo_sea ADD CONSTRAINT geo_sea_sea_fk FOREIGN KEY(sea) REFERENCES sea(name)

ALTER TABLE located ADD CONSTRAINT located_sea_fk FOREIGN KEY(sea) REFERENCES sea(name)

ALTER TABLE islandin ADD CONSTRAINT islandin_river_fk FOREIGN KEY(river) REFERENCES river(name)

ALTER TABLE lake ADD CONSTRAINT lake_river_fk FOREIGN KEY(river) REFERENCES river(name)

ALTER TABLE riveronisland ADD CONSTRAINT riveronisland_river_fk FOREIGN KEY(river) REFERENCES river(name)

ALTER TABLE riverthrough ADD CONSTRAINT riverthrough_river_fk FOREIGN KEY(river) REFERENCES river(name)

ALTER TABLE geo_estuary ADD CONSTRAINT geo_estuary_river_fk FOREIGN KEY(river) REFERENCES river(name)

ALTER TABLE geo_river ADD CONSTRAINT geo_river_river_fk FOREIGN KEY(river) REFERENCES river(name)

ALTER TABLE geo_source ADD CONSTRAINT geo_source_river_fk FOREIGN KEY(river) REFERENCES river(name)

ALTER TABLE located ADD CONSTRAINT located_river_fk FOREIGN KEY(river) REFERENCES river(name)

ALTER TABLE mountainonisland ADD CONSTRAINT mountainonisland_mountain_fk FOREIGN KEY(mountain) REFERENCES mountain(name)

ALTER TABLE geo_mountain ADD CONSTRAINT geo_mountain_mountain_fk FOREIGN KEY(mountain) REFERENCES mountain(name)

ALTER TABLE islandin ADD CONSTRAINT islandin_lake_fk FOREIGN KEY(lake) REFERENCES lake(name)

ALTER TABLE lakeonisland ADD CONSTRAINT lakeonisland_lake_fk FOREIGN KEY(lake) REFERENCES lake(name)

ALTER TABLE river ADD CONSTRAINT river_lake_fk FOREIGN KEY(lake) REFERENCES lake(name)

ALTER TABLE riverthrough ADD CONSTRAINT riverthrough_lake_fk FOREIGN KEY(lake) REFERENCES lake(name)

ALTER TABLE geo_lake ADD CONSTRAINT geo_lake_lake_fk FOREIGN KEY(lake) REFERENCES lake(name)

ALTER TABLE located ADD CONSTRAINT located_lake_fk FOREIGN KEY(lake) REFERENCES lake(name)

ALTER TABLE geo_desert ADD CONSTRAINT geo_desert_desert_fk FOREIGN KEY(desert) REFERENCES desert(name)

ALTER TABLE encompasses ADD CONSTRAINT encompasses_continent_fk FOREIGN KEY(continent) REFERENCES continent(name)

ALTER TABLE islandin ADD CONSTRAINT islandin_island_fk FOREIGN KEY(island) REFERENCES island(name)

ALTER TABLE lakeonisland ADD CONSTRAINT lakeonisland_island_fk FOREIGN KEY(island) REFERENCES island(name)

ALTER TABLE mountainonisland ADD CONSTRAINT mountainonisland_island_fk FOREIGN KEY(island) REFERENCES island(name)

ALTER TABLE riveronisland ADD CONSTRAINT riveronisland_island_fk FOREIGN KEY(island) REFERENCES island(name)

ALTER TABLE airport ADD CONSTRAINT airport_island_fk FOREIGN KEY(island) REFERENCES island(name)

ALTER TABLE geo_island ADD CONSTRAINT geo_island_island_fk FOREIGN KEY(island) REFERENCES island(name)

ALTER TABLE locatedon ADD CONSTRAINT locatedon_island_fk FOREIGN KEY(island) REFERENCES island(name)


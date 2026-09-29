# Heat Risk Mapping - Turin case study <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/Mole_Antonelliana_(Torino)_10.jpg%22 }-->
####
 
## Authors: Francesco Mezza¹, Sona Guliyeva², Filippos Kostikiadis³, and Sophia Dolla³
> ¹ Polytechnic University of Milan ² Polytechnic University of Turin  ³ Aristotle University of Thessaloniki
 
*This story is based on results from the Science Hub Challenge organised and hosted by ESA's ESRIN Science Hub in September 2026. The scope of the challenge was to develop a framework to identify urban areas that are potentially most vulnerable to heat exposure during heatwave events combining Earth Observation data with geospatial information. The method was implemented on the AVL platform by a team of a PhD candidate and Master students from the Polytechnic University of Milan, the Polytechnic University of Turin and Aristotle University of Thessaloniki. The data and code are made openly available.*
 
## 
<p align="center">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRykXzo6XdIiDH7WzjEsW9AwJ6HNyaLZ0fDqJoJExBiZOHf7FN_rZqcggo&s=10%22 alt="ESA Logo" height="120" style="margin: 0 15px;"/>
<img src="https://lanuovacopisteria.it/wp-content/uploads/2026/01/politecnico-di-torino-polito.jpg" alt="Politecnico di Torino" height="120" style="margin: 0 15px;"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/89/Aristotle_University_of_Thessaloniki_logo.svg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original%22 alt="Aristotle University of Thessaloniki" height="120" style="margin: 0 15px;"/>
</p>
 
## Introduction
As extreme heat becomes a climate threat to European cities, we can no longer rely on simple weather forecasts to protect our most vulnerable citizens. That’s why we performed a dynamic, EO-based Thermal Risk Analysis for Turin.
 
Our index proves that heat vulnerability isn't just about the weather—it's a structural crisis driven by concrete and aging populations. This tool empowers city planners to pinpoint exact 'thermal traps', transforming broad climate goals into targeted, life-saving, actions exactly where they are needed most.
 
## Heat exposure and vulnerability
Heat exposure refers to the presence of people, ecosystems, infrastructure or other assets in areas affected by excessive heat. It is influenced by temperature, humidity, wind, solar radiation and local geographical and urban characteristics. In urban areas, factors such as building materials, land cover, vegetation and the urban heat island (UHI) effect can create substantial spatial differences in heat exposure.
 
Vulnerability describes the susceptibility of individuals or populations to adverse effects from heat. It is influenced by physiological, demographic, social and socioeconomic factors, as well as housing conditions and access to cooling, healthcare and other essential services. Certain groups, such as older adults, children and outdoor workers, may be particularly susceptible to heat-related impacts.
 
Torino's geographic setting in the Po Valley basin creates a physical microclimate prone to atmospheric stagnation, weak ventilation, and pollutant entrapment. Enclosed by the Alpine arc to the west and north, the basin acts as a thermal trap during persistent heat domes. In the summer of 2026, as an African anticyclone pushed temperatures across Italy past 40°C, Turin's eight districts did not all suffer equally. A resident of a low-density neighborhood and a resident of a paved, high-density one lived through the same heatwave in very different modalities.
 
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Torino%20sentinel.png?raw=true" width="400"/></p>
 
This study delivers a spatialized framework for mapping urban heat exposure and social vulnerability across Torino's administrative districts (circoscrizioni), linking satellite observations with climate analysis and demographic vulnerability.
 
According to the climate risk framework, risk results from the interaction between hazard, exposure and vulnerability. Thus, a heatwave represents the hazard, while heat exposure and vulnerability determine how strongly individuals and populations may be affected.
 
## Method and datasets
The core question addressed was whether EO data could be combined with geospatial information to locate urban areas experiencing heightened heat stress during heatwave events. To achieve this, the used datasets were:
- **Sentinel-3 SLSTR (Land Surface Temperature - LST)**:  a European Earth Observation satellite mission developed to support Copernicus ocean, land, atmospheric, emergency, security, and cryospheric applications.The primary goal of the Sentinel-3 mission is to measure sea surface topography, sea and land surface temperature, and ocean and land surface color with high accuracy and reliability.
 
<p align="center"><img src="https://sentinels.copernicus.eu/documents/4634164/9bbb4317-7cb9-1c8b-a382-3ad82b6a28e4" width="400"/></p>
<p align="center" style="font-size: 0.85em; color: #666;"><em>Sentinel-3 satellite, ESA.</em></p>
 
 
- **High Resolution Layer Imperviousness**: The High Resolution Layer (HRL) Imperviousness by the Copernicus Land Monitoring Service (CLMS) captures the spatial distribution and change over time of artificially sealed and built-up areas in high-resolution and harmonized manner over entire 
Europe. The contained datasets offer valuable insights for a variety of domains and applications – from infrastructure planning, urban management and environmental monitoring to disaster preparedness, real estate and tourism.
 
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Torino%20-%20Imperviousness%202024.png?raw=true%22 width="400"/></p>
 
- **District and Population Data (Municipality of Torino)**: Vector files to define the official administrative boundaries of the city (the 8 "circoscrizioni" or districts) and the number and age of the inhabitants in each district. They were used to aggregate the raster data and calculate statistics for each one. People aged 65 years or older are more at risk during extreme heat due to physiological changes associated with aging.
 
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Vulnerability%20Map%20%20Over%2065%20by%20District%20(Turin).png?raw=true%22 width="400"/></p>
 
- **Green Areas Data (Municipality of Torino Open Data)**: Vector files retrieved from the city's official open data portal, mapping the precise polygons of public green spaces across the urban area (including parks, gardens, and tree-lined avenues). Green areas can lower local temperatures by 1°C to 7°C through natural shade and plant cooling.
 
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Urban%20green%20areas.png?raw=true" width="400"/></p>
 
## Heat risk from Earth Observation
The team's methodology included the following steps and expected outcomes:
 
**1. Data Retrieval & Anomaly Mapping**
 
Selecting a time series over Turin between August 1-15, 2026 and retrieving Sentinel-3 Land Surface Temperature (LST) observations for the period to understand the temperature pattern.
 
 
**2. Deriving Spatial Indicators**
 
Using additional datasets (such as green cover by Comune di Torino and Copernicus High Resolution Layer Imperviousness) to describe the urban environment through indicators like vegetation cover, impervious surfaces, and built-up density.
 
**3. Heat Risk Index**
 
Defining an index that combines thermal intensity with exposure indicators to map and rank the most exposed urban districts.
Hazard, exposure, and vulnerability are the key drivers of physical climate risk. 
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/climate-change_v2.jpg?raw=true" width="1000"/></p>
 
The risk index ranges from 0-1, and is calculated based on:
 
- Surface heat (nightly Sentinel-3 LST)
 
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Nighttime%20LST%20Evolution%20-%20Turin%20Districts%20.png?raw=true%22 width="1000"/></p>
 
- Age vulnerability (% population over 65)
 
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/05_age_distribution_dashboard.png?raw=true%22 width="1200"/></p>
 
- Lack of greenery (inverse of green cover per district)
 
- Imperviousness (soil sealing)
 
The risk index is therefore calculated as the average of all of these factors (each one normalized between 0-1).
 
## Analysis <!--{ as="eox-map" mode="tour" position="right" }-->
 
### <!--{ zoom=11 center=[7.6869,45.0703] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}},{"type… animationOptions='{"duration":500}' }-->
#### Turin Overview
An overview of the city of Turin, showcasing the urban landscape and surrounding geography.
 
### <!--{ zoom=14 center=[7.68,45.07] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Historical Center
Focusing on the highly dense historical center where heat trapping is most prominent.
 
### <!--{ zoom=13 center=[7.63,45.04] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Industrial South-West
Examining the industrial belt which experiences significant soil sealing.
 
### <!--{ zoom=13 center=[7.71,45.05] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### Borgo Po Green Buffer
The green hills providing a natural cooling buffer effect for the city.
 
### <!--{ zoom=13 center=[7.68,45.1] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Northern Districts
Areas with lower heat vulnerability due to younger population demographics.
 
### <!--{ zoom=13 center=[7.68,45.1] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Heat Risk Index
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/06_heat_exposure_index_map.png?raw=true%22 width="1400"/></p>
 
### <!--{ animationOptions='{"duration":500}' }-->
#### Daily Risk Ranking
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/07_daily_vulnerability_ranking%20(1).png?raw=true%22 width="1000"/></p>
 
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/percentages.png?raw=true" width="1000"/></p>
 
### <!--{ animationOptions='{"duration":500}' }-->
#### Critical Facilities
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/09_critical_facilities_map.png?raw=true%22 width="1000"/></p>
 
## Conclusions
Turin's heat vulnerability is structurally dictated by urban morphology and demographics, not daily weather. The historical center and south-western industrial belt form extreme-risk zones due to severe soil sealing, lack of vegetation, and aging populations.
 
Conversely, Borgo Po's vast forested hills demonstrate a green buffer effect that drastically lowers thermal risk. Meanwhile, northern districts show lower vulnerability simply because their younger populations are statistically less heat-sensitive.
 
Ultimately, the city's most impermeable, concrete-dense environments perfectly align with its oldest demographics, creating persistent thermal traps.
 
To mitigate urban heat, the city must prioritize de-paving wide avenues and planting shade trees to reduce surface temperatures. In the dense historical center, micro-interventions like green roofs and highly reflective materials are essential to cool narrow streets.
 
To protect the aging population, the city should establish accessible cooling centers and implement early warning systems. Additionally, deploying mobile health units and strengthening neighborhood networks will ensure isolated elderly residents stay safe during extreme heatwaves.
 
## Open Science
| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| --- | --- | --- | --- |
| **[Sentinel-3 SLSTR L2 LST](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-slstr/product-types/level-2-lst)** | Dataset | Copernicus / ESA | Daily (nighttime-pass) Land Surface Temperature, 1–15 Aug 2026 — the core heat-hazard layer of the index |
| **Sentinel-2 MSI L2A (`COPERNICUS/S2_SR_HARMONIZED`)** | Dataset | Copernicus, via [Google Earth Engine](https://earthengine.google.com/) | Cloud-masked median composite used for NDVI/NDBI |
| **[Imperviousness HRL 2024](https://land.copernicus.eu/en/products/high-resolution-layer-imperviousness)** | Dataset | Copernicus Land Monitoring Service | Soil sealing %, one of the 4 index components |
| **[ThermalTrace](https://thermaltrace.climate.copernicus.eu/)** | Dataset / Tool | Copernicus C3S / ECMWF | ERA5 / UTCI daily temperature, used to select and corroborate the heatwave window |
| **[Geoportale Piemonte](https://www.geoportale.piemonte.it/geonetwork/srv/api/records/c_l219:f71649ef-0855-4f16-abc6-9c6c0a4e4658)** | Dataset | Città di Torino open geodata (CC BY 4.0) | District boundaries, urban green areas, population by age and district |
| **OpenStreetMap** | Dataset | OSM contributors, via Overpass API / [osmnx](https://osmnx.readthedocs.io/) | Hospitals, schools, elderly-care facility locations |
| **[EO Dashboard](https://eodashboard.org/explore/?x=7.6869&y=45.0703&z=10.0000&datetime=2026-08-13&template=expert)** | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Base layers and visualization tools for interactive exploration |
 
## References
### Earth Observation data
* Sentinel-3 SLSTR Level-2 LST — Copernicus / ESA
* Sentinel-2 MSI Level-2A (COPERNICUS/S2_SR_HARMONIZED) — Copernicus, via Google Earth Engine
* Imperviousness High Resolution Layer 2024 — Copernicus Land Monitoring Service
 
### Meteorological context
* ThermalTrace — daily air / UTCI feels-like temperature, ERA5, Copernicus C3S / ECMWF
* Beretta, S. “Meteo oggi 4 agosto: bollino rosso in 25 città su 27, punte di 41°C”, Quotidiano Motori, 4 Aug 2026 — nationwide red-alert heatwave, corroborating the analysis window
 
### Geospatial Information (Città di Torino, via Geoportale Piemonte)
* District boundaries (circoscrizioni) and urban green areas — Comune di Torino open geodata, e.g. Geoportale Piemonte catalog record (CC BY 4.0)
* Population by age and district (“B1 Pop per età annuale e circoscrizione 2025”) — Comune di Torino open data
* https://dutchclimaterisk.nl/climate-risk/risk-assessment-guidance/
* https://heat.gov/who-is-most-at-risk-to-extreme-heat/at-risk-older-adults/
* https://www.sciencedirect.com/science/article/pii/S2212096325000452
 
### Points of interest
* OpenStreetMap contributors — hospitals, schools, elderly-care facilities, queried via Overpass API / osmnx
 
## Contributors
- Francesco Mezza — Coding and data processing
- Sona Guliyeva — Project lead and supervision
- Sophia Dolla — Theoretical framework
- Filippos Kostikiadis — Theoretical framework
# Heat Risk Mapping - Turin case study <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/Mole_Antonelliana_(Torino)_10.jpg" }-->
####
 
## Authors: Francesco Mezza¹, Sona Guliyeva², Filippos Kostikiadis³, and Sophia Dolla³
> ¹ Polytechnic University of Milan ² Polytechnic University of Turin  ³ Aristotle University of Thessaloniki
 
*This story is based on results from the Science Hub Challenge organised and hosted by ESA's ESRIN Science Hub in September 2026. The scope of the challenge was to develop a framework to identify urban areas that are potentially most vulnerable to heat exposure during heatwave events combining Earth Observation data with geospatial information. The method was implemented on the AVL platform by a team of a PhD candidate and Master students from the Polytechnic University of Milan, the Polytechnic University of Turin and Aristotle University of Thessaloniki. The data and code are made openly available.*
 
## 
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/b/bd/European_Space_Agency_logo.svg" alt="European Space Agency" height="60" style="margin: 0 20px;"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/0/00/Politecnico_di_Milano_-_wordmark_%28Italy%2C_2024%29.svg" alt="Politecnico di Milano" height="50" style="margin: 0 20px;"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Politecnico_di_Torino_-_wordmark_%28Italy%2C_2021%29.svg" alt="Politecnico di Torino" height="60" style="margin: 0 20px;"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/89/Aristotle_University_of_Thessaloniki_logo.svg" alt="Aristotle University of Thessaloniki" height="90" style="margin: 0 20px;"/>
</p>
 
## Introduction
As extreme heat becomes one of the main climate threats to European cities, weather forecasts alone cannot tell us who is most at risk. That’s why we combined Earth Observation, urban and demographic data into a district-level heat risk index for Turin.
 
Our results show that heat risk in Turin is not only a matter of weather: sealed surfaces, a lack of green space and an ageing population shape where heat hurts most. The index helps city planners find the districts where cooling measures and health services are needed first.
 
## Heat exposure and vulnerability
Heat exposure refers to the presence of people, ecosystems, infrastructure or other assets in areas affected by excessive heat. It is influenced by temperature, humidity, wind, solar radiation and local geographical and urban characteristics. In urban areas, factors such as building materials, land cover, vegetation and the urban heat island (UHI) effect can create substantial spatial differences in heat exposure.
 
Vulnerability describes the susceptibility of individuals or populations to adverse effects from heat. It is influenced by physiological, demographic, social and socioeconomic factors, as well as housing conditions and access to cooling, healthcare and other essential services. Certain groups, such as older adults, children and outdoor workers, may be particularly susceptible to heat-related impacts.
 
Torino's geographic setting in the Po Valley basin creates a physical microclimate prone to atmospheric stagnation, weak ventilation, and pollutant entrapment. Enclosed by the Alpine arc to the west and north, the basin acts as a thermal trap during persistent heat domes. In the summer of 2026, as an African anticyclone pushed temperatures across Italy past 40°C, Turin's eight districts did not all suffer equally. A resident of a low-density neighborhood and a resident of a paved, high-density one lived through the same heatwave in very different modalities.
 
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/Torino%20sentinel.png" width="400"/></p>
 
This study delivers a spatialized framework for mapping urban heat exposure and social vulnerability across Torino's administrative districts (circoscrizioni), linking satellite observations with climate analysis and demographic vulnerability.
 
According to the climate risk framework, risk results from the interaction between hazard, exposure and vulnerability. Thus, a heatwave represents the hazard, while heat exposure and vulnerability determine how strongly individuals and populations may be affected.
 
## Method and datasets
The core question addressed was whether EO data could be combined with geospatial information to locate urban areas experiencing heightened heat stress during heatwave events. To achieve this, the used datasets were:
- **Sentinel-3 SLSTR (Land Surface Temperature - LST)**:  the Sea and Land Surface Temperature Radiometer on board Sentinel-3A and 3B measures land surface temperature at about 1 km resolution. We used the night-time overpasses (around 22:30–23:30 local time) from 1–15 August 2026; 14 of the 15 days were available. Night-time surface temperature shows how much heat the city stores and releases after sunset. That is the core of the urban heat island effect, and it matters most for health, because the body cannot recover when nights stay hot.
 
<p align="center"><img src="https://sentinels.copernicus.eu/documents/4634164/9bbb4317-7cb9-1c8b-a382-3ad82b6a28e4" width="400"/></p>
<p align="center" style="font-size: 0.85em; color: #666;"><em>Sentinel-3 satellite, ESA.</em></p>
 
 
- **High Resolution Layer Imperviousness**: the Copernicus Land Monitoring Service HRL Imperviousness 2024 is a 10 m map of the share of each pixel covered by artificial, sealed surfaces such as asphalt, concrete and buildings. Sealed surfaces absorb solar radiation during the day and release it at night, and they leave no room for vegetation or evaporative cooling.
 
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/Torino%20-%20Imperviousness%202024.png" width="400"/></p>
 
- **District and Population Data (Municipality of Torino)**: Vector files to define the official administrative boundaries of the city (the 8 "circoscrizioni" or districts) and the number and age of the inhabitants in each district. They were used to aggregate the raster data and calculate statistics for each one. People aged 65 years or older are more at risk during extreme heat due to physiological changes associated with aging.
 
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/Vulnerability%20Map%20%20Over%2065%20by%20District%20(Turin).png" width="400"/></p>
 
- **Green Areas Data (Municipality of Torino Open Data)**: Vector files retrieved from the city's official open data portal, mapping the precise polygons of public green spaces across the urban area (including parks, gardens, and tree-lined avenues). Parks and tree cover can lower local temperatures by several degrees through shade and evapotranspiration.
 
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/Urban%20green%20areas.png" width="400"/></p>
 
- **Sentinel-2 MSI Level-2A**: a cloud-masked median composite for 1–15 August 2026 was used to compute NDVI (vegetation health) and NDBI (built-up intensity) at 10–20 m. These layers give visual context; they are not part of the index.
 
## Heat risk from Earth Observation
The methodology follows three steps:
 
**1. Data retrieval and heatwave characterisation**
 
Selecting a time series over Turin between August 1-15, 2026 and retrieving Sentinel-3 Land Surface Temperature (LST) observations for the period to understand the temperature pattern.
 
 
**2. Deriving Spatial Indicators**
 
Using additional datasets (such as green cover by Comune di Torino and Copernicus High Resolution Layer Imperviousness) to describe the urban environment through indicators like vegetation cover, impervious surfaces, and built-up density.
 
**3. Heat Risk Index**
 
Defining an index that combines thermal intensity with exposure indicators to map and rank the most exposed urban districts.
Hazard, exposure, and vulnerability are the key drivers of physical climate risk. 
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/climate-change_v2.jpg" width="1000"/></p>
 
The risk index ranges from 0-1, and is calculated based on:
 
- Surface heat (nightly Sentinel-3 LST)
 
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/Nighttime%20LST%20Evolution%20-%20Turin%20Districts%20.png" width="1000"/></p>
 
- Age vulnerability (% population over 65)
 
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/05_age_distribution_dashboard.png" width="1200"/></p>
 
- Lack of greenery (inverse of the green area per district)
 
- Imperviousness (soil sealing)
 
The risk index is the equally weighted mean of the four components, each scaled to 0–1:

**Risk = ¼ · Heat + ¼ · Age + ¼ · Lack of green + ¼ · Imperviousness**

- **Heat:** mean night-time Sentinel-3 LST per district, scaled between 15 °C and 42 °C
- **Age:** share of residents aged 65 or older, divided by the highest district share
- **Lack of green:** 1 − green area of the district ÷ (1.3 × the largest district value)
- **Imperviousness:** mean soil sealing per district

The index was calculated for five nights (1, 4, 7, 10 and 13 August 2026) and averaged.
 
## Analysis <!--{ as="eox-map" mode="tour" position="right" }-->
 
### <!--{ zoom=11 center=[7.6869,45.0703] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### Turin Overview
An overview of the city of Turin, showcasing the urban landscape and surrounding geography.
 
### <!--{ zoom=14 center=[7.68,45.07] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Historical Center
Centro – Crocetta (C.1) has the highest heat risk in the city (0.65): dense buildings, the least green space and the warmest nights of all districts.
 
### <!--{ zoom=13 center=[7.635,45.065] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Western Districts
San Paolo – Pozzo Strada (C.3) ranks second (0.63): dense housing, little green space and the highest soil sealing in the city. Further south, the former industrial area of Santa Rita – Mirafiori (C.2) ranks fifth.
 
### <!--{ zoom=13 center=[7.71,45.05] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### The Green Hill Buffer
The Turin hill and the Po riverbanks (C.7 and C.8) have the lowest risk in the city: their parks and woods act as a natural cooling buffer.
 
### <!--{ zoom=13 center=[7.70,45.10] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Barriera di Milano
Barriera di Milano – Rebaudengo (C.6) has the lowest share of residents aged 65 or older in Turin. Its lower risk (0.43) comes mainly from its younger population rather than from a cooler environment.
 
### <!--{ zoom=12 center=[7.6869,45.0703] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### Heat Risk Index
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/06_heat_exposure_index_map.png" width="1400"/></p>
 
### <!--{ animationOptions='{"duration":500}' }-->
#### Daily Risk Ranking
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/07_daily_vulnerability_ranking%20(1).png" width="1000"/></p>
 
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/percentages.png" width="1000"/></p>
 
### <!--{ animationOptions='{"duration":500}' }-->
#### Critical Facilities
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/09_critical_facilities_map.png" width="1000"/></p>
 
## Limitations
- Sentinel-3 LST has about 1 km resolution, coarse compared with Turin's districts, so street-level hot spots are smoothed out.
- The index uses five nights; 14 August was missing.
- Green space is measured as total area per district, not as a share of the district's area, so large districts that include the hill score as greener.
- All four components carry equal weight; other weightings would change the ranking.
- Age is the only vulnerability indicator. Income, living alone or housing quality could be added in a next iteration.
 
## Conclusions
Across the five sampled nights, **Centro – Crocetta (C.1, 0.65)** and **San Paolo – Pozzo Strada (C.3, 0.63)** show the highest heat risk, followed by San Donato – Parella, Borgo Vittoria – Lucento and Santa Rita – Mirafiori (0.53–0.56). These districts combine the least green space with the most sealed surfaces, while the share of residents aged 65 or older is high in all eight districts.
 
The lowest risk is found in **Aurora – Vanchiglia (C.7, 0.39)** and **San Salvario – Lingotto – Borgo Po (C.8, 0.41)**, which include the Turin hill and the Po riverbanks: their parks and woods act as a green buffer. **Barriera di Milano – Rebaudengo (C.6, 0.43)** scores low mainly because it has the youngest population of all districts.
 
Age differs little between districts, and night-time surface temperature varies by only a few degrees at 1 km resolution. The ranking is therefore driven mostly by green space and soil sealing, which are exactly the parts of heat risk that urban planning can change.
 
To mitigate urban heat, the city should prioritize de-paving wide avenues and planting shade trees to reduce surface temperatures. In the dense historical center, micro-interventions like green roofs and highly reflective materials are essential to cool narrow streets.
 
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
| **[Analysis notebook](https://github.com/FrancescoMezza/torino-heat-exposure)** | Code | Team 4 | Reproducible Python workflow developed on the AVL platform |
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
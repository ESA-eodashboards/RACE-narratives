# Heat Risk Mapping - Turin case study <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/Mole_Antonelliana_(Torino)_10.jpg" }-->
####
 
## Authors: Francesco Mezza¹, Sona Guliyeva², Filippos Kostikiadis³, and Sophia Dolla³
> ¹ Polytechnic University of Milan ² Polytechnic University of Turin  ³ Aristotle University of Thessaloniki
 
*This story is based on results from the Science Hub Challenge organised and hosted by ESA's ESRIN Science Hub in September 2026. The scope of the challenge was to develop a framework to identify urban areas that are potentially most vulnerable to heat exposure during heatwave events combining Earth Observation data with geospatial information. The method was implemented on the AVL platform by a team of a PhD candidate and Master students from the Polytechnic University of Milan, the Polytechnic University of Turin and Aristotle University of Thessaloniki. The data and code are made openly available.*
 
## 
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/b/bd/European_Space_Agency_logo.svg" alt="European Space Agency" height="55" style="margin: 10px 20px;"/>
<img src="https://www.polimi.it/_assets/4b51f00386267395f41e0940abbcd656/Images/logo.svg" alt="Politecnico di Milano" height="60" style="margin: 10px 20px;"/>
<img src="https://www.polito.it/themes/custom/polito_customizations/polito_logo_desktop.svg" alt="Politecnico di Torino" height="70" style="margin: 10px 20px;"/>
<img src="https://www.auth.gr/wp-content/uploads/banner-horizontal-default-en-1.png" alt="Aristotle University of Thessaloniki" height="70" style="margin: 10px 20px;"/>
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
 
<p align="center"><img src="https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/imperviousness_map.png" width="500"/></p>
 
- **District and Population Data (Municipality of Torino)**: Vector files to define the official administrative boundaries of the city (the 8 "circoscrizioni" or districts) and the number and age of the inhabitants in each district. They were used to aggregate the raster data and calculate statistics for each one. People aged 65 years or older are more at risk during extreme heat due to physiological changes associated with aging. In Turin their share ranges from 23.2% in Barriera di Milano – Rebaudengo (C.6) to 28.6% in Santa Rita – Mirafiori (C.2).
 
<p align="center"><img src="https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/over65_map.png" width="500"/></p>
 
- **Green Areas Data (Municipality of Torino Open Data)**: Vector files retrieved from the city's official open data portal, mapping the precise polygons of public green spaces across the urban area (including parks, gardens, and tree-lined avenues). Parks and tree cover can lower local temperatures by several degrees through shade and evapotranspiration.
 
<p align="center"><img src="https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/green_areas_map.png" width="500"/></p>
 
- **Sentinel-2 MSI Level-2A**: a cloud-masked median composite for 1–15 August 2026 was used to compute NDVI (vegetation health) and NDBI (built-up intensity) at 10–20 m. These layers give visual context; they are not part of the index. The hill districts are by far the greenest (mean NDVI 0.57 in C.7 and 0.49 in C.8), while the historical centre is the least green (0.23).
 
<p align="center"><img src="https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/ndvi_ndbi_map.png" width="900"/></p>
<p align="center" style="font-size: 0.85em; color: #666;"><em>Left: vegetation (NDVI), right: built-up intensity (NDBI), Sentinel-2 median composite, 1–15 August 2026.</em></p>
 
## The heatwave, night by night
Sentinel-3 passed over Turin every night between 1 and 15 August 2026 (the 14 August product is missing). The maps below show the night-time surface temperature for each overpass, around 22:30–23:30 local time.
 
<p align="center"><img src="https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/lst_nights_1-15aug.png" width="1000"/></p>
 
On clear nights such as 3, 4, 6, 7, 11 and 12 August, the city stayed between roughly 22 and 30 °C at the surface, with the densely built centre and western districts warmest and the green hill east of the Po coolest. On other nights, clouds covered much of the city: the satellite then measures the colder top of the clouds, not the ground, which is why some panels look dark. The cloud mask below shows which parts of the city were cloud-covered on each night.
 
<p align="center"><img src="https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/cloud_cover_1-15aug.png" width="1000"/></p>
 
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
 
- Age vulnerability (% population over 65)
 
<p align="center"><img src="https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/age_distribution.png" width="1200"/></p>
 
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
 
### <!--{ zoom=12 center=[7.6869,45.0703] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"WebGLTile","properties":{"id":"lst04","title":"Night-time LST 4 Aug 2026"},"opacity":0.8,"source":{"type":"GeoTIFF","normalize":false,"sources":[{"url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/lst_night_2026-08-04.tif"}]},"style":{"color":["case",["==",["band",2],0],["color",0,0,0,0],["<",["band",1],15],["color",170,170,170,0.7],["interpolate",["linear"],["band",1],18.0,[0,0,4,1],20.0,[40,11,84,1],22.0,[101,21,110,1],24.0,[159,42,99,1],26.0,[212,72,66,1],28.0,[245,125,21,1],30.0,[250,193,39,1],32.0,[252,255,164,1]]]}}]' animationOptions='{"duration":500}' }-->
#### Night of 4 August: a clear heatwave night
Night-time surface temperature from Sentinel-3 (dark purple ≈ 18 °C, yellow ≈ 32 °C). Even after sunset the densely built centre and western districts stay warmest, while the hill east of the Po cools down.
 
### <!--{ zoom=12 center=[7.6869,45.0703] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"WebGLTile","properties":{"id":"lst07","title":"Night-time LST 7 Aug 2026"},"opacity":0.8,"source":{"type":"GeoTIFF","normalize":false,"sources":[{"url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/lst_night_2026-08-07.tif"}]},"style":{"color":["case",["==",["band",2],0],["color",0,0,0,0],["<",["band",1],15],["color",170,170,170,0.7],["interpolate",["linear"],["band",1],18.0,[0,0,4,1],20.0,[40,11,84,1],22.0,[101,21,110,1],24.0,[159,42,99,1],26.0,[212,72,66,1],28.0,[245,125,21,1],30.0,[250,193,39,1],32.0,[252,255,164,1]]]}}]' animationOptions='{"duration":500}' }-->
#### Night of 7 August
Another clear night: the same pattern repeats, with the built-up plain warmer than the green hill.
 
### <!--{ zoom=12 center=[7.6869,45.0703] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"WebGLTile","properties":{"id":"lst10","title":"Night-time LST 10 Aug 2026"},"opacity":0.8,"source":{"type":"GeoTIFF","normalize":false,"sources":[{"url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/lst_night_2026-08-10.tif"}]},"style":{"color":["case",["==",["band",2],0],["color",0,0,0,0],["<",["band",1],15],["color",170,170,170,0.7],["interpolate",["linear"],["band",1],18.0,[0,0,4,1],20.0,[40,11,84,1],22.0,[101,21,110,1],24.0,[159,42,99,1],26.0,[212,72,66,1],28.0,[245,125,21,1],30.0,[250,193,39,1],32.0,[252,255,164,1]]]}}]' animationOptions='{"duration":500}' }-->
#### Night of 10 August: clouds
Most of the city was under clouds. Grey areas are values below 15 °C: the satellite saw the cold cloud tops, not the ground. Nights like this one have to be removed before computing the heat index.
 
### <!--{ zoom=13 center=[7.6869,45.0703] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"WebGLTile","properties":{"id":"imp","title":"Imperviousness 2024"},"opacity":0.85,"source":{"type":"GeoTIFF","normalize":false,"sources":[{"url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/imperviousness_2024.tif"}]},"style":{"color":["case",["any",["==",["band",2],0],["==",["band",1],255],["<",["band",1],5]],["color",0,0,0,0],["interpolate",["linear"],["band",1],5.0,[255,245,240,1],28.75,[252,187,161,1],52.5,[251,106,74,1],76.25,[203,24,29,1],100.0,[103,0,13,1]]]}}]' animationOptions='{"duration":500}' }-->
#### Sealed surfaces
Copernicus imperviousness: dark red means almost completely sealed ground (asphalt, concrete, roofs). Sealing is highest in the historical centre, the western districts and the industrial areas in the south-west and north.
 
### <!--{ zoom=14 center=[7.68,45.07] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"WebGLTile","properties":{"id":"imp_c","title":"Imperviousness 2024"},"opacity":0.75,"source":{"type":"GeoTIFF","normalize":false,"sources":[{"url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/imperviousness_2024.tif"}]},"style":{"color":["case",["any",["==",["band",2],0],["==",["band",1],255],["<",["band",1],5]],["color",0,0,0,0],["interpolate",["linear"],["band",1],5.0,[255,245,240,1],28.75,[252,187,161,1],52.5,[251,106,74,1],76.25,[203,24,29,1],100.0,[103,0,13,1]]]}}]' animationOptions='{"duration":500}' }-->
#### Historical Center
Centro – Crocetta (C.1) has the highest heat risk in the city (0.65): dense buildings, the least green space and the warmest nights of all districts.
 
### <!--{ zoom=13 center=[7.635,45.065] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Western Districts
San Paolo – Pozzo Strada (C.3) ranks second (0.63): dense housing, little green space and the highest soil sealing in the city. Further south, the former industrial area of Santa Rita – Mirafiori (C.2) ranks fifth.
 
### <!--{ zoom=13 center=[7.71,45.05] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}},{"type":"WebGLTile","properties":{"id":"ndvi","title":"NDVI 1-15 Aug 2026"},"opacity":0.8,"source":{"type":"GeoTIFF","normalize":false,"sources":[{"url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/ndvi_2026-08-01_15.tif"}]},"style":{"color":["case",["==",["band",2],0],["color",0,0,0,0],["interpolate",["linear"],["band",1],-0.1,[165,0,38,1],0.08,[244,109,67,1],0.26,[254,224,139,1],0.44,[217,239,139,1],0.62,[102,189,99,1],0.8,[0,104,55,1]]]}}]' animationOptions='{"duration":500}' }-->
#### The Green Hill Buffer
The Turin hill and the Po riverbanks (C.7 and C.8) have the lowest risk in the city: their parks and woods act as a natural cooling buffer. On the map, dark green shows dense vegetation (Sentinel-2 NDVI).
 
### <!--{ zoom=13 center=[7.70,45.10] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Barriera di Milano
Barriera di Milano – Rebaudengo (C.6) has the lowest share of residents aged 65 or older in Turin (23.2%). Its lower risk (0.43) comes mainly from its younger population rather than from a cooler environment.
 
### <!--{ zoom=11.4 center=[7.675,45.07] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"risk_avg","title":"Heat Risk Index: average of the five nights"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/districts_heat_risk.geojson","format":"GeoJSON"},"style":{"fill-color":["interpolate",["linear"],["get","risk_avg"],0.35,[255,255,178,0.8],0.43,[254,217,118,0.8],0.51,[254,178,76,0.8],0.59,[253,141,60,0.8],0.67,[240,59,32,0.8],0.75,[189,0,38,0.8]],"stroke-color":"#333333","stroke-width":1.2,"text-value":["get","label_avg"],"text-font":"bold 13px sans-serif","text-fill-color":"#111111","text-stroke-color":"#ffffff","text-stroke-width":3,"text-overflow":true}}]' animationOptions='{"duration":500}' }-->
#### Heat Risk Index: average of the five nights
Centro – Crocetta (C.1, 0.65) and San Paolo – Pozzo Strada (C.3, 0.63) have the highest average risk; the hill districts C.7 and C.8 the lowest. Colours go from light yellow (risk ≈ 0.35) to dark red (≈ 0.75); each district shows its score. Keep scrolling to see how the index changes from night to night.
 
### <!--{ zoom=11.4 center=[7.675,45.07] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"risk_01","title":"1 August"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/districts_heat_risk.geojson","format":"GeoJSON"},"style":{"fill-color":["interpolate",["linear"],["get","risk_01"],0.35,[255,255,178,0.8],0.43,[254,217,118,0.8],0.51,[254,178,76,0.8],0.59,[253,141,60,0.8],0.67,[240,59,32,0.8],0.75,[189,0,38,0.8]],"stroke-color":"#333333","stroke-width":1.2,"text-value":["get","label_01"],"text-font":"bold 13px sans-serif","text-fill-color":"#111111","text-stroke-color":"#ffffff","text-stroke-width":3,"text-overflow":true}}]' animationOptions='{"duration":500}' }-->
#### 1 August
Centro – Crocetta leads (0.65). San Paolo – Pozzo Strada scores lower (0.58) only because clouds over the western districts gave cold, unrealistic surface temperatures that night.
 
### <!--{ zoom=11.4 center=[7.675,45.07] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"risk_04","title":"4 August: a clear, hot night"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/districts_heat_risk.geojson","format":"GeoJSON"},"style":{"fill-color":["interpolate",["linear"],["get","risk_04"],0.35,[255,255,178,0.8],0.43,[254,217,118,0.8],0.51,[254,178,76,0.8],0.59,[253,141,60,0.8],0.67,[240,59,32,0.8],0.75,[189,0,38,0.8]],"stroke-color":"#333333","stroke-width":1.2,"text-value":["get","label_04"],"text-font":"bold 13px sans-serif","text-fill-color":"#111111","text-stroke-color":"#ffffff","text-stroke-width":3,"text-overflow":true}}]' animationOptions='{"duration":500}' }-->
#### 4 August: a clear, hot night
With a clear sky the whole city heats up. San Paolo – Pozzo Strada (0.74) overtakes the centre (0.69), followed by San Donato – Parella (0.64).
 
### <!--{ zoom=11.4 center=[7.675,45.07] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"risk_07","title":"7 August: clear night"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/districts_heat_risk.geojson","format":"GeoJSON"},"style":{"fill-color":["interpolate",["linear"],["get","risk_07"],0.35,[255,255,178,0.8],0.43,[254,217,118,0.8],0.51,[254,178,76,0.8],0.59,[253,141,60,0.8],0.67,[240,59,32,0.8],0.75,[189,0,38,0.8]],"stroke-color":"#333333","stroke-width":1.2,"text-value":["get","label_07"],"text-font":"bold 13px sans-serif","text-fill-color":"#111111","text-stroke-color":"#ffffff","text-stroke-width":3,"text-overflow":true}}]' animationOptions='{"duration":500}' }-->
#### 7 August: clear night
The same pattern as on 4 August: San Paolo – Pozzo Strada (0.70), Centro – Crocetta (0.66) and San Donato – Parella (0.60) are the most exposed districts.
 
### <!--{ zoom=11.4 center=[7.675,45.07] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"risk_10","title":"10 August: cloudy night"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/districts_heat_risk.geojson","format":"GeoJSON"},"style":{"fill-color":["interpolate",["linear"],["get","risk_10"],0.35,[255,255,178,0.8],0.43,[254,217,118,0.8],0.51,[254,178,76,0.8],0.59,[253,141,60,0.8],0.67,[240,59,32,0.8],0.75,[189,0,38,0.8]],"stroke-color":"#333333","stroke-width":1.2,"text-value":["get","label_10"],"text-font":"bold 13px sans-serif","text-fill-color":"#111111","text-stroke-color":"#ffffff","text-stroke-width":3,"text-overflow":true}}]' animationOptions='{"duration":500}' }-->
#### 10 August: cloudy night
Clouds hide the ground and the heat component drops almost everywhere; the ranking is then driven only by age, green space and soil sealing.
 
### <!--{ zoom=11.4 center=[7.675,45.07] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"risk_13","title":"13 August: cloudy night"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/districts_heat_risk.geojson","format":"GeoJSON"},"style":{"fill-color":["interpolate",["linear"],["get","risk_13"],0.35,[255,255,178,0.8],0.43,[254,217,118,0.8],0.51,[254,178,76,0.8],0.59,[253,141,60,0.8],0.67,[240,59,32,0.8],0.75,[189,0,38,0.8]],"stroke-color":"#333333","stroke-width":1.2,"text-value":["get","label_13"],"text-font":"bold 13px sans-serif","text-fill-color":"#111111","text-stroke-color":"#ffffff","text-stroke-width":3,"text-overflow":true}}]' animationOptions='{"duration":500}' }-->
#### 13 August: cloudy night
Again largely cloudy: all scores fall (0.36–0.61), which pulls down the five-night average.
 
### <!--{ animationOptions='{"duration":500}' }-->
#### Daily Risk Ranking
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/07_daily_vulnerability_ranking%20(1).png" width="1000"/></p>
 
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/percentages.png" width="1000"/></p>
 
### <!--{ animationOptions='{"duration":500}' }-->
#### Critical Facilities
<p align="center"><img src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/09_critical_facilities_map.png" width="1000"/></p>
 
## Does cloud cover change the ranking?
Drag the slider to compare the index averaged over all five nights (left) with the index computed from the two clear nights only, 4 and 7 August (right). Without cloud-affected nights, San Paolo – Pozzo Strada (0.72) becomes the most heat-exposed district, ahead of Centro – Crocetta (0.67), and all scores rise by 0.02–0.09. The order of the other districts stays the same.
 
<eox-map-compare style="height:520px;display:block">
<eox-map slot="first" zoom="11.4" center="[7.675,45.07]" layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"risk_avg","title":"All five nights"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/districts_heat_risk.geojson","format":"GeoJSON"},"style":{"fill-color":["interpolate",["linear"],["get","risk_avg"],0.35,[255,255,178,0.8],0.43,[254,217,118,0.8],0.51,[254,178,76,0.8],0.59,[253,141,60,0.8],0.67,[240,59,32,0.8],0.75,[189,0,38,0.8]],"stroke-color":"#333333","stroke-width":1.2,"text-value":["get","label_avg"],"text-font":"bold 13px sans-serif","text-fill-color":"#111111","text-stroke-color":"#ffffff","text-stroke-width":3,"text-overflow":true}}]'></eox-map>
<eox-map slot="second" zoom="11.4" center="[7.675,45.07]" layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"risk_clear","title":"Clear nights only"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/SonaGuliyeva/turin-heat-risk-story/main/districts_heat_risk.geojson","format":"GeoJSON"},"style":{"fill-color":["interpolate",["linear"],["get","risk_clear"],0.35,[255,255,178,0.8],0.43,[254,217,118,0.8],0.51,[254,178,76,0.8],0.59,[253,141,60,0.8],0.67,[240,59,32,0.8],0.75,[189,0,38,0.8]],"stroke-color":"#333333","stroke-width":1.2,"text-value":["get","label_clear"],"text-font":"bold 13px sans-serif","text-fill-color":"#111111","text-stroke-color":"#ffffff","text-stroke-width":3,"text-overflow":true}}]'></eox-map>
</eox-map-compare>

<p style="font-size: 0.85em; color: #666;"><em>Left: average of 1, 4, 7, 10 and 13 August. Right: average of the clear nights 4 and 7 August. Daily values were recomputed from the night-time LST maps with the same formula as the notebook.</em></p>
 
## Limitations
- Sentinel-3 LST has about 1 km resolution, coarse compared with Turin's districts, so street-level hot spots are smoothed out.
- The index uses five nights (1, 4, 7, 10 and 13 August). The cloud mask shows that 10 and 13 August, and part of 1 August, were largely cloud-covered, so the heat component for those nights reflects cloud tops rather than the ground. A next version should use only the clear nights (3, 4, 6, 7, 11 and 12 August).
- Green space is measured as total area per district, not as a share of the district's area, so large districts that include the hill score as greener.
- All four components carry equal weight; other weightings would change the ranking.
- Age is the only vulnerability indicator. Income, living alone or housing quality could be added in a next iteration.
 
## Conclusions
Across the five sampled nights, **Centro – Crocetta (C.1, 0.65)** and **San Paolo – Pozzo Strada (C.3, 0.63)** show the highest heat risk, followed by San Donato – Parella, Borgo Vittoria – Lucento and Santa Rita – Mirafiori (0.53–0.56). These districts combine the least green space with the most sealed surfaces, while the share of residents aged 65 or older is high in all eight districts (23–29%).
 
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
| **[Story data](https://github.com/SonaGuliyeva/turin-heat-risk-story)** | Data | Team 4 | Cloud-Optimized GeoTIFFs (night-time LST, NDVI, imperviousness), map styles and figures used in this story |
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
- **Francesco Mezza** — Master's student in Telecommunications Engineering, Politecnico di Milano — Coding and data processing
- **Sona Guliyeva** — PhD candidate in Urban and Regional Development, Politecnico di Torino — Project lead and supervision
- **Sophia Dolla** — Master's student in Environmental Physics, Aristotle University of Thessaloniki — Theoretical framework
- **Filippos Kostikiadis** — Master's student in Environmental Physics, Aristotle University of Thessaloniki — Theoretical framework
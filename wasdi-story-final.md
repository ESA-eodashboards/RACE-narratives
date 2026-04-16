---
cover-image: https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/stories/Floodings/Hochwasser_Gars_am_Kamp_2024_03.jpg

date: 2025-01-01
theme: climate
tags: floods,earth-observation,wasdi
collections: WASDI_FLOOD
 
---    

# Mapping the 2024 Central European Floods with Satellite Technology <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/stories/Floodings/Hochwasser_Gars_am_Kamp_2024_03.jpg" }-->
### Using remote sensing data and WASDI workflows to monitor flood evolution in open and urban areas <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## The 2024 Central European Floods
Throughout much of 2024, numerous European countries were affected by severe floods caused by prolonged heavy rains. Several were catastrophic, causing deaths and widespread damage due to overflowing river basins and landslides.
In response to the floods, the [Copernicus Emergency Management Service](https://mapping.emergency.copernicus.eu/) has been activated to produce detailed maps of the affected areas across several countries, including Poland, Germany, Slovakia, Austria, Germany and Italy.

<figure style="text-align: center;">
    <img src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2024/10/valencia_flood_disaster/26405663-2-eng-GB/Valencia_flood_disaster_pillars.jpg" 
         alt="  " 
         style="display: block; margin: 0 auto;"
         width="400">
       US Landsat-8 satellite from 8 October and 30 October showing the dramatic transformation of the landscape.Credit: 
        <a href="https://www.esa.int/ESA_Multimedia/Images/2024/10/Valencia_flood_disaster" target="_blank">
             USGS, processed by ESA
        </a>.
</figure>

Emergency response required detailed and timely mapping of the flooded areas. This situation highlighted the critical role of satellite Earth Observation (EO) technologies in monitoring, mapping, and responding to natural disasters. 

## Earth Observations of floods
Earth observation (EO) techniques offer the opportunity to monitor and map catastrophic events, providing support that would be impossible to achieve through ground-based observations alone, especially in inaccessible areas after a disaster occurs. Different EO sensors onboard satellite missions allow retrieval of different but complementary information:

* **Optical satellites**, such as Copernicus Sentinel-2, Landsat, and MODIS, capture multispectral imagery that clearly distinguishes water from land, taking advantage of water’s unique spectral signature, which strongly absorbs radiation in the near-infrared and shortwave infrared bands.

* **Radar satellites**, equipped with synthetic aperture radar (SAR), such as Copernicus Sentinel-1, RADARSAT, and TerraSAR-X, operate independently of illumination or cloud cover, allowing monitoring of the surface after flooding events and becoming an indispensable tool for flood mapping.
While optical and radar satellite data provide complementary insights for flood detection and mapping, efficiently processing these large volumes of EO data can be challenging, particularly for timely disaster response. 

This is where dedicated platforms and tools, such as [WASDI](https://www.wasdi.cloud/), come into play, streamlining access, processing, and analysis of satellite imagery for practical flood monitoring applications.

## The WASDI Platform
**Streamlining flood analysis**

The [WASDI platform](https://www.wasdi.cloud/) represents a significant advancement in EO data processing for flood monitoring. WASDI is a cloud-based workspace designed to simplify access, processing, and analysis of satellite data for environmental applications, including flood management. The method used to produce flood maps over an open area is integrated into an app called [SAR Flood Archive Generator 3.3.4](https://wasdi.readthedocs.io/en/latest/WasdiApplications/SARArchiveGenerator.html). This automated application processes the Sentinel-1 GRD archive for a specified Area of Interest (AoI), compiling historical flood maps. 
 
 <figure style="text-align: center;">
    <img src="https://wascia.ssl.telespazio.com/media/images/wasdi11.max-1600x1600.format-webp.webp" 
         alt="  " 
         style="display: block; margin: 0 auto;"
         width="700">
        <a href="https://www.wasdi.cloud/" target="_blank">
             WASDI Platform
        </a>
</figure>

The dataset can be acquired via the [Network of Resources (NoR)](https://nor-discover.org/en/news/) request. NoR provides a unique environment for both commercial and non-commercial users to discover, via the NoR Portfolio, a list of European cloud services and estimates of the associated costs to make full use of Earth Observation data. [ESA offers sponsorship](https://nor-discover.org/en/sponsorship/) to eligible entities to cover the costs of trying out these services.

 <figure style="text-align: center;">
    <img src="https://eo4society.esa.int/wp-content/uploads/2023/05/NOR-new-header-with-text.jpg" 
         alt="  " 
         style="display: block; margin: 0 auto;"
         width="300">
        <a href="https://nor-discover.org/" target="_blank">
             Explore the NoR Portal
        </a>
</figure>





##  Datasets and Uses cases <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"WASDI_FLOOD-2024-11-30T00:00:00Z"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"WASDI_FLOOD","styles":"","format":"image/png","time":"2024-11-30T00:00:00Z"}}},{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="10.5255513921666" center=[-0.7699145674963137,39.41517882926112] animationOptions={duration:500}}-->
##### Flood Monitoring in Open Areas  
The method used to produce flood maps over **open areas** is integrated in the  [SAR Flood Archive Generator 3.3.4](https://wasdi.readthedocs.io/en/latest/WasdiApplications/SARArchiveGenerator.html). This automated application processes the Sentinel-1 GRD archive for the specific area, compiling historical flood maps. The application generates maps for every day for which a [Sentinel-1 GRD](https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel1.html) image is available over the Area of Interest. Flood detection is then performed by analysing intensity values and the output showes **flooded (red)** and **permanent water (blue)**.

<figure style="text-align: center;">
    <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/collections/WASDI_FLOOD/cm_legend.png" 
         alt=" " 
         style="display: block; margin: 0 auto;"
         width="500">
</figure>

**Image from 2024-11-30**

### <!--{ layers='[{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"WASDI_FLOOD-2024-11-30T00:00:00Z"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"WASDI_FLOOD","styles":"","format":"image/png","time":"2024-11-30T00:00:00Z"}}},{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="11.709821919636315" center=[-0.3296633376550024,39.310304807645764] animationOptions={duration:500}}-->
#### Valencia, Spain 
On 29 October 2024, torrential rain caused by an isolated low-pressure area at high levels brought over a year's worth of precipitation to several areas in eastern Spain, including the Valencian Community, Castilla–La Mancha, and Andalusia.
<figure style="text-align: center;">
    <img src="https://scx2.b-cdn.net/gfx/news/hires/2024/valencia-floods-our-wa.jpg" 
         alt=" " 
         style="display: block; margin: 0 auto;"
         width="500">
    <figcaption>
         Rain and floods caused by the DANA in Valencia on 29 October 2024. Credit:
        <a href="https://x.com/VOSTcvalenciana/status/1851265104735580259" target="_blank">
             VOST Comunitat Valenciana
        </a>.
    </figcaption>
</figure>

According to Spain’s national weather agency, [Aemet](https://www.aemet.es/en/portada), on 29 October 2024, Valencia received a year’s worth of rain in just eight hours. This deluge caused devastating flash floods, turning streets into rivers, destroying homes, and sweeping away vehicles. The resulting floodwaters caused the deaths of about 232 people, with three more missing[1] and substantial property damage [2][3]. It is one of the deadliest natural disasters in Spanish history [4].




### <!--{ layers='[{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"WASDI_FLOOD-2024-11-30T00:00:00Z"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"WASDI_FLOOD","styles":"","format":"image/png","time":"2024-11-30T00:00:00Z"}}},{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="10.802153687126457" center=[16.0058194604704,48.33099126051039] animationOptions={duration:500}}-->
#### Urban Flood Mapping
Concerning **urban areas**, a different method is applied. It relies on the information contained in the phase, rather than the intensity used for open area. Flood is detected analyzing the difference of coherence between a pair of 2 pre-event Sentinel-1 SLC images and a pair of 1 pre-event Sentinel-1 SLC image and 1 post-event Sentinel-1 SLC image. This application, named Urban Flood, available in the WASDI platform, needs as a prerequisite the availability of a building map, to constrain the areas where to look for differences of coherence.

<figure style="text-align: center;">
    <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/collections/WASDI_FLOOD/cm_legend.png" 
         alt=" " 
         style="display: block; margin: 0 auto;"
         width="500">
</figure>

**Image from 2024-11-30**

### <!--{ layers='[{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"WASDI_FLOOD-2024-11-30T00:00:00Z"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"WASDI_FLOOD","styles":"","format":"image/png","time":"2024-11-30T00:00:00Z"}}},{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="11.602153687126457" center=[16.0058194604704,48.33099126051039] animationOptions={duration:500}}-->
#### St Pölten, Austria
During September 2024, a large weather event affected multiple Central European countries, with Austria's eastern region, including St. Pölten (located in Lower Austria) and Vienna taking a particularly hard hit. The water level of the Wien Riever, in the western part of Vienna rose from 50 centimeters to 2.26 metetrs in the course of a day, leading to the flooding of trails, restaurants, streets and river banks. Electricity was cut off in some districts and subway lines were partially closed as result [5](https://www.dw.com/en/europe-floods-parts-of-vienna-without-power-as-river-rises/live-70220078). The Austrian province surrounding Vienna has been declared a disaster area, with its leaders speaking of "an unprecedented extreme situation" [6](https://www.bbc.com/news/live/cdrjjl3mmy8t).
<figure style="text-align: center;">
    <img src="https://ichef.bbci.co.uk/ace/standard/800/cpsprodpb/vivo/live/images/2024/9/15/1d9752ba-15c7-46f8-b0a8-34facf64ba0e.jpg.webp" 
         alt=" " 
         style="display: block; margin: 0 auto;"
         width="500">
    <figcaption>
         The flooded Wienfluss river in Vienna. Credit:
        <a href="https://www.bbc.com/news/live/cdrjjl3mmy8t" target="_blank">
             BBC News
        </a>.
    </figcaption>
</figure>

##  Impacts in Urban areas
##### Extracting furhter information: temporal evolution
Using WASDI flood maps, it is possible to conduct further analysis and extract more insights and information on the impacts and extension of the floods. Taking for example St Pölten, in Austria, the temporal evolution was estimated based on the flood dataset, enabling to understand the temporal evolution of the floods. For each date, the total flooded area (red pixels) was estimating by summing all the flooded pixels which were converted into square meters. By comparing these values over time, the date with the largest flooded area, **2024-09-20** was identified as the most flooded day in the dataset.
<figure style="text-align: center;">
    <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/stories/Floodings/Temporal%20evolution%20of%20flooded%20and%20permanent%20water%20areas.png"
         alt=" " 
         style="display: block; margin: 0 auto;"
         width="500">
    <figcaption>
       Temporal evolution of floods
    </figcaption>
</figure>


 
##### Relative Road Flood Risk Map: a proxy to understand infrastructure vulnerability
Based on the **most flooded date**, a relative flood risk map can generated, providing a proxy to which roads are potentially most exposed to flooding, based on their proximity to flooded areas, through an estimated risk score. 

Taking again as example St Pölten, more specifically, Tulln an der Donau area. The road network (extracted from OSM), was converted into a raster grid, and then aligned with the urban flood map for the most flooded date. For each road pixel, the distance to the nearest flooded area was calculated. The road pixels closer to floods were assigned higher risk scores, while those farther away received lower scores. 

Finally, these scores were normalized between 0 (low risk) and 1 (high risk) and visualized with a gradient from **green (low risk)** to **dark red (high risk)**, highlighting areas where **flooding can most affect road infrastructure**.
<figure style="text-align: center;">
    <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/stories/Floodings/relative_risk_score_map.png" 
         alt=" " 
         style="display: block; margin: 0 auto;"
         width="500">
    <figcaption>
         Risk Score map based on the most flooded date
    </figcaption>
</figure>



## Open Science
#### Explore Flooding extensions Jupyter Notebooks 
You can further explore an example of WASDI dataset relative to the last example,  the floods over St Pölten, Austria, and gather a further insight over this particular area and event, interacting directly with the dataset though the [notebook below](https://github.com/eurodatacube/notebooks/tree/master/notebooks/curated). 
In this example, the notebook allows to get further insight from WASDI data, which (as some of the examples in this story). The notebook shows how to  overlay flood data on optical imagery (from Copernicus Sentinel-2) allowing for  intuituve **visual interpretation** of the extent and impacts of the floods; the **temporal analysis of floods** and estimation of **flooded areas**, as well as a workflow to generate a **relative road risk flood map**. 
<iframe width="100%" height="600" src="https://esa-eodashboards.github.io/RACE-notebooks/notebooks/flooding-analysis-with-wasdi-data/" frameborder="0"></iframe>

Besides [acceessing  the notebook](https://esa-eodashboards.github.io/RACE-notebooks/notebooks/flooding-analysis-with-wasdi-data/) you can also crosscompare multiyear data over particular locations impacted by floods in 2024 exploring the [Flood mapping indicator](https://esa-eodashboards.github.io/RACE-client/explore/?x=15.7954&y=48.4066&z=10.1201&datetime=2024-10-01&template=expert&indicator=WASDI_FLOOD&poi=St_Polten_Vienna) available at RACE dashboard.

#### Open datasets and platforms used in this story

 | **Name**                                                                                                                                       | **Type**            | **Agency / Provider**                     | **Description / Usage**                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Sentinel-1 GRD and SLC](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-1)**                                        | Dataset             | Copernicus / ESA               | C-band SAR Ground Range Detected (GRD) and Single Look Complex (SLC) data used for flood mapping in open areas and urban areas, processed in WASDI’s SAR Flood Archive Generator and WASDI Urban Flood application.                            |
| **[Sentinel-2 MSI](https://doi.org/10.1016/j.rse.2016.01.019)**                                                                                       | Dataset | Copernicus / ESA                        | Multispectral optical imagery used to visualize flood extents and to overlay WASDI flood masks in notebooks..                                    |
| **[Landsat-8/9 OLI](https://www.usgs.gov/landsat-missions)**                                          | Dataset     | USGS / NASA               | Multispectral imagery showing pre- and post-flood landscape changes; used for visual flood assessment.                                                     |
| **[Copernicus Emergency Management Service (CEMS)](https://mapping.emergency.copernicus.eu/)**                          | Platform / Service | European Commission | Provides emergency satellite-derived flood maps for affected Central European regions.                                            |
| **[WASDI Platform](https://www.wasdi.cloud/)**                          | Cloud Platform | WASDI / ESA NoR | Cloud-based environment enabling access, processing, and analysis of EO data, hosting multiple flood-mapping workflows.                                               |
| **[Network of Resources (NoR)](https://www.wasdi.cloud/)**                          | Access Framework | ESA | Provides access to cloud EO services and funds eligible users to acquire & process Sentinel-1 data for WASDI workflows.                                               |
| **[Euro Data Cube Curated Notebooks](https://github.com/eurodatacube/notebooks/tree/master/notebooks/curated)**                          | Analysis Environment | ESA / EOX / EDC | Jupyter notebooks enabling flood-data visualization, time-series analysis, extent estimation, and GIF generation.                                              |
| **[RACE - Flood Mapping Indicator](https://esa-eodashboards.github.io/RACE-client/explore/?x=15.7954&y=48.4066&z=10.1201&datetime=2024-10-01&template=expert&indicator=WASDI_FLOOD&poi=St_Polten_Vienna)**                          | Data Product / Platform | ESA / European Commission | Multi-year flood indicator enabling comparison of flood evolution across different years and regions.                                       |

#### References

*  "Actualización de datos del Gobierno de España" [Spanish Government data update]. La Moncloa (in Spanish). 4 January 2025. Retrieved 4 January 2025.
*  Evans, Holly; Cobham, Tara; Croft, Alex (2 November 2024). "Spain floods latest: 5,000 more soldiers deployed as satellite photos show extent of devastation". The Independent. Retrieved 2 November 2024.
*  Jones, Sam (2 November 2024). "Spain floods: 10,000 troops and police drafted in to deal with disaster". The Guardian. Retrieved 2 November 2024.
*  Mates, James (1 November 2024). "Spain's deadliest floods in decades: Death toll reaches 205 as temporary morgue opens". ITVX. Retrieved 1 November 2024.
* Chini, M., Pelich, R., Pulvirenti, L., Pierdicca, N., Hostache, R., Matgen, P., 2019. Sentinel-1 InSAR coherence to detect floodwater in urban areas: Houston and Hurricane Harvey as a test case. Remote Sensing, 11(2), p.107.
* [WASDI platform](https://www.wasdi.cloud/)
* [Copernicus Emergency Management Service](https://mapping.emergency.copernicus.eu/)  
*  [SAR Flood Archive Generator 3.3.4](https://wasdi.readthedocs.io/en/latest/WasdiApplications/SARArchiveGenerator.html)


#### Contributors
* WASDI – Data providers
* Sara Aparício (Solenix) – Notebook use case development; story editing and content development
* Diego Moglioni (Starion) – Dataset integration

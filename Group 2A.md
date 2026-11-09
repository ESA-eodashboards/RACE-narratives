# Unsupervised Mapping of Urban Thermal Environments in the Milan and Monza-Brianza area <!--{ as="img" mode="hero" src="https://images.unsplash.com/photo-1773160063998-d4f9560ae5ad?q=80&w=1632&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" }-->
#### <small>Authors: Thomas Martinoli¹ , Yiyi Cen¹ , Sara Reffinetti¹ <br><sub style='font-size:0.7em'>¹ Politecnico of Milan</sub></small>

## 
*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in September 2026. It was developed by a team from the Politecnico of Milan.*

## 
<p align="center" style="margin-top:-20px; margin-bottom:-20px;">
  <img src=https://www.policollege.polimi.it/wp-content/uploads/2026/04/logo-polimi-scaled.png alt="Politecnico di Milano" height="120"/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://th.bing.com/th/id/R.023cad37e1b2bd876572ba2bd38432f7?rik=MFEIeBOIq6ojVQ&amp;pid=ImgRaw&amp;r=0" alt="ESA" height="120"/>
</p>

## Challenge
Urban environments are not spatially uniform. Vegetation, buildings, impervious surfaces, bare soil and water often occur within short distances and influence surface temperature in different ways. As a result, different parts of the same city can exhibit clearly different thermal conditions.

Urban environments are often described using predefined land-cover classes, such as built-up areas, vegetation or water. While these classifications are useful, real urban surfaces tend to vary continuously and often overlap or mix with one another. Fixed classes may therefore not fully capture this complexity.

This leads to our main research question:

**Can distinct urban thermal environments be identified directly from multi-variable Earth Observation data without defining the classes in advance?**

## Objective
The objective of this study is to use multi-variable Earth Observation data and unsupervised learning to develop a data-driven characterisation of urban environments in the Milan–Monza area.

By combining information related to temperature, vegetation and built-up characteristics, we use clustering to identify urban areas with similar environmental properties and then interpret their surface and thermal characteristics. Finally, the resulting clusters are compared with existing land-cover products and Local Climate Zones to understand how these data-driven urban types relate to established classification systems.

## Dataset
The analysis focused on the **provinces of Milan and Monza-Brianza**, leveraging Earth Observation data from **June to August 2021** to capture thermal variations.

| Data source | Product | Variables | Spatial resolution |
| :---: | :---: | :---: | :---: |
| **Landsat 8** | Collection 2 Level-2 | Land Surface Temperature (LST) | 30 m\* |
| **Sentinel-2** | MSI Level-2A | NDVI, NDRE, NDBI, BSI, MNDWI, Albedo | 20 m |
| **Copernicus CLMS**\*\* | Tree Cover Density 2021 | Tree canopy cover | 10 m |
| **Copernicus CLMS**\*\* | Imperviousness Density 2021 | Impervious surfaces | 10 m |
| **Global LCZ map**\*\*\* | Demuzere et al. (2022) | Local Climate Zones (reference only) | 100 m |

\* Distributed at 30 m; the thermal band (TIRS) has a native resolution of 100 m.  
\*\* CLMS: Copernicus Land Monitoring Service.  
\*\*\* Used only as an external reference for comparison, not as a clustering input.

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ zoom=10 center=[9.02,45.5268] layers='[{"type":"Tile","properties":{"id":"terrain-light","title":"Terrain Light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"study-area","title":"Study Area"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/AOI_Milan_Monza%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":"rgba(255,255,255,0.03)","stroke-color":"#d7191c","stroke-width":3}}]' animationOptions='{"duration":500}' }-->
#### Milan and Monza-Brianza Area
The study focuses on the Milan and Monza-Brianza area in northern Italy. The region includes highly urbanised city centres, residential areas, industrial and commercial zones, green spaces and peri-urban areas.

These different urban environments are closely interwoven within a relatively compact area, providing rich spatial variation for comparing different urban surface characteristics.

### <!--{ zoom=10 center=[9.02,45.5268] layers='[{"type":"Tile","properties":{"id":"terrain-light","title":"Terrain Light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"tree-cover","title":"Tree Cover Density 2021"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/TCD_2021_100m_classes%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":["match",["get","class_id"],1,"rgba(198,233,192,0.60)",2,"rgba(77,175,74,0.70)",3,"rgba(0,100,0,0.85)","rgba(0,0,0,0)"]}},{"type":"Vector","properties":{"id":"study-area","title":"Study Area"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/AOI_Milan_Monza%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":"rgba(255,255,255,0)","stroke-color":"#d7191c","stroke-width":2}}]' animationOptions='{"duration":500}' }-->
#### Tree Cover Density
Tree Cover Density is one of the variables used to describe urban vegetation structure. The map shows clear spatial differences in tree canopy cover across the study area, ranging from areas with very limited tree cover to much greener zones.

This map is presented as one example of the input variables used in the analysis. The full analysis also includes multiple Sentinel-2 spectral indices and other surface characteristics.

### <!--{ zoom=10 center=[9.02,45.5268] layers='[{"type":"Tile","properties":{"id":"terrain-light","title":"Terrain Light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"imperviousness","title":"Imperviousness Density 2021"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/Imperviousness_2021_100m_classes%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":["match",["get","class_id"],1,"rgba(245,220,180,0.60)",2,"rgba(230,130,80,0.72)",3,"rgba(170,30,30,0.85)","rgba(0,0,0,0)"]}},{"type":"Vector","properties":{"id":"study-area","title":"Study Area"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/AOI_Milan_Monza%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":"rgba(255,255,255,0)","stroke-color":"#d7191c","stroke-width":2}}]' animationOptions='{"duration":500}' }-->
#### Imperviousness Density
Imperviousness Density describes the proportion of buildings, roads and other artificial sealed surfaces, providing an indication of urban built-up intensity.

Spatially, high imperviousness is mainly concentrated in the urban core of Milan and other continuously urbanised areas. Towards the urban fringe, imperviousness generally decreases, revealing a gradual transition from densely built-up areas to lower-density and more open environments.

## Methodology workflow
The analysis followed a systematic processing pipeline:

- **1- Select and composite data:** The study focused on the Milan and Monza-Brianza area during summer 2021 (June–August). Sentinel-2 Level-2A images were selected based on acquisition date and cloud cover. Six surface indicators—NDVI, NDRE, NDBI, BSI, MNDWI and Albedo—were derived, and a pixel-wise temporal median was calculated using valid observations. Tree Cover Density and Imperviousness Density were taken from the corresponding 2021 annual products, while LST was represented by the summer composite.

<table style="width:100%; border-collapse:collapse;">
<thead>
<tr>
<th style="text-align:center;">Variable</th>
<th style="text-align:center;">Formula / computation</th>
<th style="text-align:center;">Environmental information</th>
</tr>
</thead>

<tbody>

<tr>
<td style="text-align:center;"><b>NDVI</b></td>
<td style="text-align:center;">
<span style="display:inline-block; text-align:center;">
<span style="display:block; border-bottom:1px solid; padding:0 6px;">
B<sub>8A</sub> − B<sub>04</sub>
</span>
<span style="display:block; padding:0 6px;">
B<sub>8A</sub> + B<sub>04</sub>
</span>
</span>
</td>
<td style="text-align:center;">Vegetation greenness</td>
</tr>


<tr>
<td style="text-align:center;"><b>NDRE</b></td>
<td style="text-align:center;">
<span style="display:inline-block; text-align:center;">
<span style="display:block; border-bottom:1px solid; padding:0 6px;">
B<sub>8A</sub> − B<sub>05</sub>
</span>
<span style="display:block; padding:0 6px;">
B<sub>8A</sub> + B<sub>05</sub>
</span>
</span>
</td>
<td style="text-align:center;">Red-edge vegetation condition</td>
</tr>


<tr>
<td style="text-align:center;"><b>NDBI</b></td>
<td style="text-align:center;">
<span style="display:inline-block; text-align:center;">
<span style="display:block; border-bottom:1px solid; padding:0 6px;">
B<sub>11</sub> − B<sub>8A</sub>
</span>
<span style="display:block; padding:0 6px;">
B<sub>11</sub> + B<sub>8A</sub>
</span>
</span>
</td>
<td style="text-align:center;">Built-up characteristics</td>
</tr>


<tr>
<td style="text-align:center;"><b>BSI</b></td>
<td style="text-align:center;">
<span style="display:inline-block; text-align:center;">
<span style="display:block; border-bottom:1px solid; padding:0 6px;">
(B<sub>11</sub> + B<sub>04</sub>) − (B<sub>8A</sub> + B<sub>02</sub>)
</span>
<span style="display:block; padding:0 6px;">
(B<sub>11</sub> + B<sub>04</sub>) + (B<sub>8A</sub> + B<sub>02</sub>)
</span>
</span>
</td>
<td style="text-align:center;">Bare soil and built-up surfaces</td>
</tr>


<tr>
<td style="text-align:center;"><b>MNDWI</b></td>
<td style="text-align:center;">
<span style="display:inline-block; text-align:center;">
<span style="display:block; border-bottom:1px solid; padding:0 6px;">
B<sub>03</sub> − B<sub>11</sub>
</span>
<span style="display:block; padding:0 6px;">
B<sub>03</sub> + B<sub>11</sub>
</span>
</span>
</td>
<td style="text-align:center;">Water detection and masking</td>
</tr>


<tr>
<td style="text-align:center;"><b>Albedo</b></td>
<td style="text-align:center;">
Derived from six Sentinel-2 spectral bands
</td>
<td style="text-align:center;">Surface reflectivity</td>
</tr>

</tbody>
</table>

- **2- Aggregate and align datasets:** All variables were aligned to a common **100 m spatial grid** using the Sentinel-2 100 m grid as the reference (EPSG:32632). The original 10 m Tree Cover Density and Imperviousness Density products were aggregated to 100 m using area-weighted averaging, while LST was aligned to the same grid. The resulting feature raster contained nine variables.

- **3- Mask invalid and water cells:** Only grid cells with valid values for all input variables were retained, with no missing-value imputation applied. Water cells were identified using MNDWI and cells with **MNDWI > 0.2** were excluded from the analysis.

- **4- Assess correlations and normalize:** Correlations between variables were examined to identify potential redundancy. Each variable was then clipped to its 1st–99th percentile range and rescaled to **0–1** to reduce the influence of extreme values and differences in scale.

- **5- PCA:** Principal Component Analysis (PCA) was applied to the normalized variables. MNDWI was excluded because it had already been used for water masking. The minimum number of principal components explaining at least **90% of the total variance** was retained; the first three components reached this threshold.

- **6- K-means clustering:** K-means clustering was applied in the PCA-reduced feature space for **k = 4–15**. Different evaluation criteria suggested different optimal solutions.The Silhouette Score is highest at k = 4, indicating the clearest separation between clusters. In contrast, the Calinski–Harabasz Index reaches its maximum at k = 9, suggesting a more detailed clustering structure. We also included k = 6 as an intermediate solution between these two levels of clustering, so we could compare a broader, intermediate and more detailed representation.

<p align="center">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/307316d228fa0050e18127b7c0f9c93e3b65c077/assets/yiyilv/IMG2006-1789684437359.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Evaluation of different numbers of K-means clusters using Inertia, Silhouette Score and the Calinski–Harabasz Index. The different criteria highlighted k = 4 and 9 as candidate solutions for further analysis.</em>
</p>

- **7- Cluster interpretation:** Each cluster was characterised using the mean normalized values of the input variables. The cluster labels were then mapped back onto the original 100 m grid to examine their spatial distribution and environmental differences.
- **8- Comparison:** The **k = 4, 6 and 9** clustering solutions were compared in terms of their spatial patterns, cluster profiles and correspondence with **Local Climate Zones (LCZ)**. LCZ was used as an external reference to assess how the data-driven clusters relate to established urban climate types.

## Results
Different clustering evaluation metrics suggested different numbers of clusters, so we further compared three solutions: **k = 4, 6 and 9**. These can be interpreted as different levels of detail within the same urban environmental structure: 
- **k = 4** captures broader environmental types; 
- **k = 6** provides an intermediate level of subdivision;  
- **k = 9** describes finer-scale environmental differences. 
 
Cluster labels are independent across different values of k, so the comparison is based mainly on their characteristics and spatial patterns.

#### Clustering structure in PCA space

We first compared the three solutions in PCA feature space. The first two principal components capture most of the dominant variation in the data, with PC1 explaining **76.8%** of the total variance and PC2 explaining **8.1%**. Based on the PCA loadings, the negative direction of PC1 is mainly associated with vegetation-related variables such as NDVI and NDRE, while the positive direction is more strongly related to NDBI, BSI, Imperviousness and LST. PC2 is largely influenced by Tree Cover Density.

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/fb5278e891629cc2a381df21d1ef8ffd4368513f/assets/yiyilv/pcaclustersk4-1789687251614.png" style="width: 90%;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/59ef6ffd718502d8644fb992bbd2f762095f42da/assets/yiyilv/pcaclustersk6-1789687261059.png" style="width: 90%;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/9c2e21e9395e7d7df171813647b68d62481e777c/assets/martinolithomas-ui/pcaclustersk9-1789689006480.png" style="width: 90%;">
</div>


*Figure 2. K-means clustering results for k = 4, 6 and 9 projected onto the first two principal components. Colours represent different clusters and crosses indicate cluster centroids.*

All three solutions show a similar overall structure. Rather than forming several completely separated groups, the data follow a relatively continuous environmental gradient. Moving from the left to the right side of the PCA space broadly corresponds to a transition from more vegetated and less built-up surfaces towards more built-up and warmer urban environments.

With **k = 4**, this continuous gradient is divided into four broad regions, producing the simplest clustering structure. <br> With **k = 6**, some of these broader regions are further subdivided, particularly within intermediate built-up and transitional environments.<br> With **k = 9**, the same gradient is divided into finer groups, revealing more local differences.

Overall, increasing k does not substantially change the underlying structure of the data, but progressively provides a finer subdivision of the same environmental gradient.
#### Cluster profiles and environmental characteristics

Each profile shows the mean normalised value (0–1) of the eight variables entering the PCA, computed for each cluster. Values are relative within the study area, not physical units, and are used to interpret each cluster in terms of vegetation, built-up intensity, tree cover and relative surface temperature.

![profili_B0_k4.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/9c2f2331019fcc9120c0e9a520d8b54e7e1712c7/assets/yiyilv/profiliB0k4-1789687647016.png)

<p align="center">
  <em>Figure 3. Cluster profiles for k = 4: mean normalised value (0–1) of each variable per cluster.</em>
</p>

**C2 (grey)** represents the **built-up type** and covers 27% of the analysed cells. It is characterised by the lowest NDVI/NDRE (~0.25), the highest NDBI/BSI (~0.8), high imperviousness (0.71) and the highest LST (0.77). **C3 (dark green)** covers 8% of the area and corresponds to **tree cover**. It shows high NDVI (0.90) and Tree Cover Density (0.73), the lowest albedo and the lowest LST (0.25). **C1 (light green)** covers 31% of the area and represents **non-woody vegetation**, with NDVI comparable to C3 (0.87) but near-zero tree cover. **C0 (ochre)** covers 34% of the area and is **intermediate**: moderate NDVI (0.57) and relatively high NDBI/BSI (~0.6) combined with low imperviousness (0.17), indicating bare or sparsely vegetated, largely unsealed surfaces rather than built-up areas.

With **k = 6**, the same overall structure as **k = 4** is preserved. **Tree cover (C1, dark green, 7%)** and **non-woody vegetation (C4, green, 23%)** remain essentially unchanged.
![profili_B0_k6 1.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/b189c5764ed92432c0457fcef60a2eea7c1117af/assets/yiyilv/profiliB0k6-1-1789687654701.png)
<p align="center">
  <em>Figure 4. Cluster profiles for k = 6: mean normalised value (0–1) of each variable per cluster.</em>
</p>

The remaining clusters can be interpreted as a finer subdivision of the built-up and intermediate types of **k = 4**. The built-up domain appears as a **dense type** (C5, dark grey, 15%); imperviousness 0.83, LST 0.81) and an **intermediate type** (C2, light grey, 18%); imperviousness 0.52, LST 0.69). Unsealed surfaces appear as **bare/sparsely vegetated** (C0, brown, 16%); LST 0.56) and **partially vegetated** (C3, ochre, 21%); LST 0.43).

With **k = 9**, the same behaviour is observed, and the additional clusters can be interpreted as further detail at both ends of the gradient. 

![profili_B0_k9.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/a96a09713bd649adc3c98e1a9ddbe2f105634e01/assets/martinolithomas-ui/profiliB0k9-1789688732488.png)

<p align="center">
  <em>Figure 5. Cluster profiles for k = 9: mean normalised value (0–1) of each variable per cluster.</em>
</p>

The built-up domain is resolved into **three levels of imperviousness** (0.39, 0.61, 0.87), with LST increasing accordingly (0.62, 0.72, 0.83). The vegetated domain includes **dense tree cover** (C3, dark green, 5%); lowest LST 0.18), **mixed tree–open vegetation** (C8, olive, 6%), and **two non-woody vegetation types of different density**(C7 and C1). Partial tree cover (C8, LST 0.38) is not cooler than dense non-woody vegetation (C7, LST 0.21).

Across all three solutions, the same pattern emerges: **surface temperature rises as the landscape becomes more built-up and falls as vegetation increases**. Vegetated areas are consistently the coolest, whether or not they are tree-covered. At **k = 4**, tree cover and non-woody vegetation reach almost the same LST (0.25 vs 0.28), and at k = 9 areas with partial tree cover are even warmer than dense grassland or cropland. At 100 m resolution, **what keeps a surface cool is how densely it is vegetated, not whether that vegetation is trees**. Albedo, by contrast, changes little between clusters (0.37–0.48) and plays only a minor role.


#### Spatial distribution
The clusters follow a **clear spatial pattern**. At **k = 4**, the **built-up cluster** covers Milan's urban core and extends north into the Monza-Brianza conurbation and along the main radial roads. The south is mostly **non-woody vegetation**, corresponding to the agricultural plain. **Tree cover** is concentrated in narrow corridors along the western and eastern edges, in line with the Ticino and Adda river valleys, plus a few patches in the north. The **intermediate cluster** is scattered across farmland and the urban fringe, where bare, cultivated and built surfaces are mixed at fine scale.
![map_b0_k4.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/eca453f839766d09967f956ae7d05e4baa445b04/assets/martinolithomas-ui/mapb0k4-1789689699736.png)
<p align="center">
  <em>Figure 6.Spatial distribution of the k = 4 clusters on the 100 m grid over the Milan and Monza-Brianza area.</em>
</p>


At **k = 6** and **k = 9** the pattern does not change. 

![map_b0_k6.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/b32fa2c0b2e2420a7a78c5b212d1b8909b424c9e/assets/yiyilv/mapb0k6-1789687722581.png)

<p align="center">
  <em>Figure 7.Spatial distribution of the k = 6 clusters on the 100 m grid over the Milan and Monza-Brianza area.</em>
</p>

![map_b0_k9.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e654446fd8d4b84c9b04b55db7aa398dd77d59ef/assets/martinolithomas-ui/mapb0k9-1789688920085.png)

<p align="center">
  <em>Figure 8.Spatial distribution of the k = 9 clusters on the 100 m grid over the Milan and Monza-Brianza area.</em>
</p>

The extra clusters mainly subdivide the **built-up area** into a **dense core** and **less sealed surrounding zones and towns**, while the **agricultural south** and the **river corridors** stay largely the same. Gaps within the study area are **masked water bodies**.


#### Qualitative comparison of clustering resolutions
We compared the clusters with the **global 100 m Local Climate Zone (LCZ) map** (Demuzere et al., 2022). The two systems are built differently: **LCZ describes urban form**, such as building height and density, while **our clusters describe surface properties only**. We therefore don't expect a one-to-one match, but we do expect a meaningful one.


![lcz_vs_cluster_maps_k4.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/95991599905188b5293e002dc8c3f6f7342b22f6/assets/martinolithomas-ui/lczvsclustermapsk4-1789709512834.png)
<p align="center">
  <em>Figure 9. Local Climate Zones (Demuzere et al., 2022; left) and k-means clusters (right) for k = 4 on the 100 m grid over the Milan and Monza-Brianza area.</em>
</p>


At **k = 4**, the built-up cluster (C2) captures almost all the compact LCZ classes (LCZ 1–3, ~96%) and heavy industry (LCZ 10, 89%), as well as most large lowrise (LCZ 8) and open midrise (LCZ 5). Dense trees (LCZ 11) fall almost entirely in the tree-cover cluster (C3, 94%), and low plants (LCZ 14) mostly in non-woody vegetation (C1, 66%). More open built areas behave differently. About half of open lowrise (LCZ 6) and sparsely built (LCZ 9) falls in the intermediate cluster C0, because at 100 m these areas contain enough gardens and unsealed ground to look more peri-urban than urban. The match is less clean the other way round. Each cluster mixes several LCZ types with similar surface properties; only **C1 is largely homogeneous (75% LCZ 14)**.

![sankey_cluster_lcz_K4.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/1a4e343ff56526ba896b8f9a86f9026acdf923f9/assets/martinolithomas-ui/sankeyclusterlczK4-1789709685932.png)
<p align="center">
  <em>Figure 10. Correspondence between the k = 4 clusters (left) and Local Climate Zones (right). Link width is proportional to the number of 100 m cells shared by each cluster–LCZ pair.</em>
</p>

At **k = 6**, the subdivision of the built-up domain is consistent with the LCZ distinction between compact and open built forms. The dense built-up cluster (C5) includes most of the compact classes (LCZ 1–3, 81–85%), heavy industry (LCZ 10, 89%) and approximately half of large lowrise (LCZ 8). The intermediate built-up cluster (C2) is instead associated with open built forms (LCZ 4–6). At **k = 9**, this subdivision extends to three levels: compact classes and large lowrise (C2), open midrise and highrise (C6), and open lowrise (C0).

![lcz_vs_cluster_maps_k6.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/fb7ac03c1b1dd28850ea0803817532af6010d26c/assets/martinolithomas-ui/lczvsclustermapsk6-1789709535499.png)
<p align="center">
  <em>Figure 11. Local Climate Zones (Demuzere et al., 2022; left) and k-means clusters (right) for k = 6 on the 100 m grid over the Milan and Monza-Brianza area.</em>
</p>



![sankey_cluster_lcz_K6.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/aca123d1d7acf105cfe9e5cbd1aebd02b3e03724/assets/martinolithomas-ui/sankeyclusterlczK6-1789709707668.png)
<p align="center">
  <em>Figure 12. Correspondence between the k = 6 clusters (left) and Local Climate Zones (right). Link width is proportional to the number of 100 m cells shared by each cluster–LCZ pair.</em>
</p>

At **k = 9**, the vegetated clusters also show a closer correspondence with LCZ. Dense tree cover (C3) is mainly associated with dense trees (LCZ 11), while mixed tree–open vegetation (C8) is mainly associated with scattered trees (LCZ 12).

![lcz_vs_cluster_maps_k9.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/8b8fa7bd630829e3ed885bcd19771cb0f7d4c0ec/assets/martinolithomas-ui/lczvsclustermapsk9-1789709628806.png)
<p align="center">
  <em>Figure 13. Local Climate Zones (Demuzere et al., 2022; left) and k-means clusters (right) for k = 9 on the 100 m grid over the Milan and Monza-Brianza area.</em>
</p>

![sankey_cluster_lcz_K9.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/8d6e8de3814240f037352f052cb4b214b9bbd62f/assets/martinolithomas-ui/sankeyclusterlczK9-1789709749868.png)

<p align="center">
  <em>Figure 14. Correspondence between the k = 9 clusters (left) and Local Climate Zones (right). Link width is proportional to the number of 100 m cells shared by each cluster–LCZ pair.</em>
</p>

**Low plants (LCZ 14)** show the opposite behaviour. Rather than corresponding to a single cluster, this class is divided into three clusters at **k = 6** and four at **k = 9**. These range from dense vegetation to bare or sparsely vegetated surfaces and differ in relative surface temperature. This represents the main contribution of the clustering with respect to LCZ: a single "low plants" class, covering most of the southern plain, includes surfaces with distinct thermal conditions.
#### Cluster–LCZ correspondence matrices

To compare the three clustering resolutions more directly, we also examined the normalised correspondence between clusters and LCZ classes. Each row is normalised to 100%, so the matrices show the **LCZ composition within each cluster**, rather than classification accuracy.

![cluster_lcz_correspondence.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/0d5c7852eabd3fc572afdc69e509ef32e4854a17/assets/yiyilv/clusterlczcorrespondence-1790598013607.png)

<p align="center">
  <em>Figure 15. Normalised Cluster–LCZ correspondence matrices for k = 4, 6 and 9. Each row represents the LCZ composition within one cluster and sums to 100%. Darker colours indicate a higher share of a given LCZ class within that cluster.</em>
</p>

The matrices confirm the main patterns observed in the maps and Sankey diagrams. At **k = 4**, the clustering produces relatively broad surface types: the non-woody vegetation cluster is strongly dominated by **LCZ 14 (low plants)**, while the tree-cover cluster is mainly associated with **LCZ 11–12 (dense and scattered trees)**. Built-up and intermediate clusters contain a broader mixture of urban LCZ classes.

As the number of clusters increases, these broad groups are progressively subdivided. At **k = 6**, different built-up clusters show distinct combinations of compact, open and large low-rise LCZ classes, while vegetation remains separated into tree-covered and non-woody types. At **k = 9**, the correspondence becomes more detailed, with additional clusters distinguishing different built-up forms and vegetation structures.

A particularly important result is that **LCZ 14 appears across several different clusters at higher k**. This supports the earlier observation that the broad LCZ "low plants" class contains surfaces with different vegetation density, exposed soil and thermal characteristics. The clustering therefore does not simply reproduce LCZ classes, but reveals additional variability within them.

## Conclusions
This study set out to test whether distinct urban thermal environments can be identified directly from multi-variable Earth Observation data, without defining classes in advance. For the Milan and Monza-Brianza area, the answer is largely positive. Combining Sentinel-2 spectral indices, Copernicus tree cover and imperviousness, and Landsat surface temperature, unsupervised clustering produced a small set of surface types that are physically interpretable and clearly organised in space.

The data do not fall into sharply separated groups. They follow a continuous gradient from vegetated to built-up surfaces, and the clusters are best understood as segments of that gradient. Surface temperature follows the same direction: it rises with imperviousness and falls with vegetation density. The k = 4, 6 and 9 solutions describe the same structure at increasing levels of detail. The simplest solution already captures the main distinctions, while higher k mainly resolves intermediate built-up conditions and differences in vegetation density.

The profiles also show that, at 100 m resolution, how densely a surface is vegetated matters more for its relative temperature than whether the vegetation consists of trees. Non-woody vegetation can be as cool as tree cover, and areas with partial tree cover are not necessarily cooler than dense crops or grassland. Albedo contributes little to the separation between clusters.

The comparison with Local Climate Zones shows that the two approaches are complementary rather than equivalent. Compact and heavily built LCZ classes fall consistently within the densest built-up clusters, and dense tree cover is well matched. As k increases, the built-up clusters progressively reproduce the LCZ distinction between compact and open built forms. The main added value of the clustering lies in the low-plants class (LCZ 14), which covers most of the southern agricultural plain. There, the clusters separate densely vegetated fields from bare or sparsely vegetated ones with markedly different surface temperatures, which LCZ treats as a single class.

These results come with limitations. The analysis covers a single summer and a single 100 m grid, so fine-scale urban heterogeneity is averaged out. Temperature is expressed in relative, normalised terms, and the thermal differences between clusters still need to be quantified in physical units. Spectral indices such as NDBI do not fully separate bare soil from built-up surfaces, and some narrow water features may not be removed by the water mask at this resolution. The LCZ comparison is descriptive and based on cell-level correspondence; a formal quantitative assessment is left for future work.

Future developments include expressing cluster temperatures in degrees Celsius, extending the analysis to multiple years to test the stability of the clusters, and applying the same workflow to other metropolitan areas. Overall, the study shows that a simple, fully data-driven workflow based on open EO data can characterise urban surface–thermal environments, and can complement established classification systems by revealing thermal variability they do not explicitly represent. These spatial differences can provide useful information for urban planners, local authorities and environmental agencies when designing heat-mitigation strategies, planning green infrastructure and identifying areas where changes in vegetation cover or soil sealing may improve local thermal conditions.

## Lessons Learned

- **Unsupervised clustering identified physically meaningful urban environments** in the Milan and Monza-Brianza area without predefined classes, using open EO data (Sentinel-2, Copernicus CLMS, Landsat 8).
- **The data form a continuous gradient** from vegetated to built-up surfaces rather than separate groups. The k = 4, 6 and 9 solutions describe the same structure at increasing levels of detail.
- **Relative surface temperature follows this gradient.** It rises with imperviousness and falls with vegetation density.
- **At 100 m, vegetation density matters more than vegetation type.** Non-woody vegetation can be as cool as tree cover, and albedo plays only a minor role.
- **Clusters and Local Climate Zones are complementary.** Compact built-up classes and dense trees are well matched, and at higher k the built-up clusters progressively reproduce the LCZ distinction between compact and open forms.
- **The main added value lies in the LCZ "low plants" class (LCZ 14).** The clustering separates densely vegetated and bare or sparsely vegetated fields with different surface temperatures, which LCZ treats as a single class.
- **The analysis has limitations.** It covers a single summer at 100 m resolution, temperatures are relative rather than physical, NDBI partly confuses bare soil with built-up surfaces, and the LCZ comparison is descriptive only.









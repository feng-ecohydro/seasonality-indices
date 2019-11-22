# seasonality-indices
Global maps of hydroclimatic seasonality indices

The global distribution hydroclimatic seasonality was evaluated using seven existing metrics (Maps_seasonality_indices.pdf). Each .txt file contains the metric values calculated from the mean monthly climatological precipitation (P) and/or potential evapotranspiration (PET) data within the CRU TS dataset version 4.03 (Harris et al. 2014), at 0.5 degree grid resolution. More information on how each metric value was calculated can be found in the included Table_seasonality_indices.pdf. The Python code simulate_sinusoid_P_PET.py produces different synthetic variations of sinusoidal seasonal distributions of P and PET that vary in terms of their relative amplitudes and phases, and calculates their associated asynchronicity index values.

1. Asynchro.txt: the asynchronicity index proposed in Feng et al. (2019).
2. dCentroid: the centroid difference (in months) between the seasonal precipitation and PET pmfs (i.e., dCentroid)
3. WalshS.txt: seasonality index of Walsh & Lawler (1981)
4. MillyS.txt: seasonality index of Milly (1994)
5. dP*.txt: seasonality index of Woods (2009)
6. SI.txt: seasonality index of Feng et al. (2013)
7. Imr.txt: seasonality index of Knoben et al. (2018)

References:
Feng, X., Porporato, A., & Rodriguez-Iturbe, I. (2013). Changes in rainfall seasonality in the tropics. Nature Climate Change, 3(9), 811–815. https://doi.org/10.1038/nclimate1907

Feng, X. Thompson, S.E., Woods, R., & Porporato, I. (2019). Quantifying asynchronicity of precipitation and potential evapotranspiration in Mediterranean climates. Geophysical Research Letters.

Harris, I., Jones, P. D., Osborn, T. J., & Lister, D. H. (2014). Updated high-resolution grids of monthly climatic observations - the CRU TS3.10 Dataset. International Journal of Climatology, 34(3), 623–642. https://doi.org/10.1002/joc.3711

Knoben, W. J. M., Woods, R. A., & Freer, J. E. (2018). A Quantitative Hydrological Climate Classification Evaluated With Independent Streamflow Data. Water Resources Research, 54(7), 5088–5109. https://doi.org/10.1029/2018WR022913

Milly, P. C. D. C. D. (1994). Climate, interseasonal storage of soil water, and the annual water balance. Advances in Water Resources, 17(1–2), 19–24. https://doi.org/10.1016/0309-1708(94)90020-5

Walsh, R. P. D., & Lawler, D. M. (1981). Rainfall Seasonality: Description, Spatial Patterns and Change Through Time. Weather, 36(7), 201–208. https://doi.org/10.1002/j.1477-8696.1981.tb05400.x

Woods, R. A. (2009). Analytical model of seasonal climate impacts on snow hydrology: Continuous snowpacks. Advances in Water Resources, 32(10), 1465–1481. https://doi.org/10.1016/j.advwatres.2009.06.011

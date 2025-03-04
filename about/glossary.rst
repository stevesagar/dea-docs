.. _glossary:

Glossary
========

.. glossary::

   Acquisition
      An image captured by a satellite sensor.

   Advanced Land Observing Satellite
   ALOS
      A Japanese satellite launched in 2006. After five years of service, the satellite
      lost power and ceased communication with Earth, but remains in orbit.

   Advanced Spaceborne Thermal and Reflection radiometer
   ASTER
      An imaging instrument onboard Terra, the flagship satellite of NASA's Earth Observing
      System (EOS) launched in December 1999. ASTER data is used to create detailed maps of
      land surface temperature, reflectance, and elevation.

      For more information, see `NASA: ASTER. <https://asterweb.jpl.nasa.gov/>`_

   Advanced Very-High Resolution Radiometer
   AVHRR
      A radiation-detection sensor that can be used for remotely determining cloud cover
      and the surface temperature. AVHRR instruments are carried by the National Oceanic and
      Atmospheric Administration (NOAA) family of polar orbiting platforms and European MetOp
      satellites.

      For more information, see `ESA: AVHRR. <https://earth.esa.int/eogateway/missions/noaa>`_

   Aerosol optical depth
      Aerosol optical depth is a measure of the extinction of the solar beam by dust and haze.

   Albedo
      The fraction of light that a surface reflects. Albedo is measured on a scale of 0-1, with 1 indicating
      that all light has been reflected by the surface.

   Algorithm
      In the context of remote sensing, algorithms generally specify how to determine higher-level
      data products from lower-level source data. For example, algorithms prescribe how atmospheric
      temperature and moisture profiles are determined from a set of radiation observations originally
      sensed by satellite sounding instruments.

   Amazon Web Services
   AWS
      One of the two environments used for hosting Digital Earth Australia.
      Amazon Web Services is a commercial cloud computing provider. Used
      by Digital Earth Australia for our JupyterHub Sandbox and Web Mapping
      Services.

   Analysis Ready Data
   ARD
      Satellite data that has been processed to a minimum set of requirements and organised into a form
      that allows immediate analysis and interoperability through time and with other datasets.

   Application Programming Interface
   API
      A software intermediary that allows two applications to talk to each other. The :term:`Open Data Cube`
      API gives programmers full access to the capabilities of the Cube, allowing query and advanced data
      retrieval.

   Atmospheric correction
      The process of removing the effects of the atmosphere on the reflectance values of images taken by
      satellite or airborne sensors.

   Australian Geoscience Data Cube
   AGDC
      A collaborative prototype project between Geoscience Australia, :term:`CSIRO` and :term:`NCI`, which aimed to
      provide better public access to NASA’s extensive Landsat archive. The AGDC has since been superseded by
      :term:`Digital Earth Australia`.

   Australian Research Environment
   ARE
      The ARE is an interface for
      using the data and software available on the :term:`NCI`. It is a replacement for
      the old :term:`VDI` system.

      For more information, see `Australian Research Environment. <https://are.nci.org.au/>`_

   Azimuth
      The angle of an object’s position from true north.

   Azimuthal exiting (degrees)
      The angle between true north and the exiting direction in the slope geometry.

   Azimuthal incident (degrees)
      The angle between true north and the incident direction in the slope geometry.

   Band
      A discrete wavelength interval or range observed by a remote sensing instrument.

   Barest Earth
      An estimate of the spectra of the barest state (i.e. least vegetation) observed from
      imagery of the Australian continent collected by the Landsat 5, 7, and 8 satellites.

   Bidirectional Reflectance Distribution Function
   BRDF
      Bidirectional reflectance distribution function is a theoretical concept
      that describes the relationship between light and an opaque surface. It uses
      a target's irradiance geometry and the remote sensing system’s
      relative angle to the target.

   Bidirectional Reflectance Distribution Function (BRDF) / Albedo Parameter
      The Bidirectional Reflectance Distribution Function (BRDF)/Albedo parameters provide:

      * coefficients for mathematical functions that describe the BRDF of each pixel in the seven :term:`MODIS` 'Land' bands (1- 7); and

      * :term:`albedo` measurements derived simultaneously from the BRDF for bands 1-7 as well as three broad bands (0.4-0.7, 0.7-3.0, and 0.4- 3.0 micrometers).

      For more information see: `NASA <https://modis.gsfc.nasa.gov/data/dataprod/mod43.php>`_

   Cloud Optimised GeoTIFF
   COG
      A data file format optimised for efficient workflows on the cloud and partial file access.

   Collection
      All products downstream of the rawest form of the main input data (:term:`telemetry`), produced
      sequentially and processed with consistent algorithms/code/inputs/outputs.

   Collection 2
   C2
      Digital Earth Australia's second :term:`Collection` of Landsat data. Now
      superceded by :term:`Collection 3` (C3). Note that there was no DEA Collection 2 of Sentinel 2 products.
      
   Collection 3
   C3
      The third :term:`Collection` of Digital Earth Australia's Landsat or Sentinel 2 data,
      and the most up-to-date collection available.

   Collection upgrade
      The reproduction of the :term:`Collection`, including all downstream products, with the initial input being
      the rawest form (:term:`telemetry`). Collections are updated when there are fundamental changes and
      upgrades to the data suite that make it incompatible with the existing collection. Therefore a collection
      upgrade is more akin to a movie franchise reboot than a re-release.

   Committee on Earth Observations, Systems Engineering Office
   CEOS-SEO
      Established in 1984, CEOS is the primary forum for the international coordination of space-based
      Earth observations. The SEO performs historical coverage analyses using the data archives for the
      Landsat, Sentinel-1, and Sentinel-2 missions.
      
   Commonwealth Scientific and Industrial Research Organisation
   CSIRO
      An Australian federal government agency responsible for scientific research.

      For more information, see `CSIRO. <https://www.csiro.au/>`_

   Copernicus Australasia Regional Data Hub
      Copernicus Australasia is a regional hub supporting the :term:`Copernicus Programme`. The Copernicus
      Australasia Regional Data Hub provides free and open access to data from Europe's Sentinel satellite
      missions for the following South-East Asia and South Pacific region.

      For more information, see `Copernicus Australasia. <https://www.copernicus.gov.au/>`_

   Copernicus Programme
      The Copernicus Programme, established in 2014, is the European Union (EU)'s Earth observation programme
      coordinated and managed by the European Commission in partnership with the European Space Agency (ESA),
      the EU Member States and EU Agencies.

      For more information, see `Copernicus Programme. <https://www.copernicus.eu/en>`_

   Dataset
      A related set of files composed of separate elements that can be manipulated as a unit.
      It is an instantiation of a :term:`product`.

   Digital Earth Australia
   DEA
      A Program of :term:`Geoscience Australia` that uses spatial data and images
      recorded by satellites orbiting our planet to detect physical changes 
      across Australia. DEA prepares these vast volumes of Earth observation data and makes it available
      to governments and industry for easy use. DEA is the Australian implementation of
      the :term:`Open Data Cube`.

      For more information, see `the DEA website. <https://www.dea.ga.gov.au/>`_
      
   DEA Notebooks
      An open-source repository containing :term:`Jupyter notebooks`, tools and workflows for geospatial
      analysis with :term:`Open Data Cube` and :term:`xarray`.

      For more information, see `the GitHub repository. <https://github.com/GeoscienceAustralia/dea-notebooks>`_
      
   DEA Sandbox
      The Digital Earth Australia Sandbox is a learning and analysis environment for
      getting started with DEA and the :term:`Open Data Cube`. It includes sample data
      and :term:`Jupyter notebooks` that demonstrate the capability of the Open Data Cube.

      For more information, see `the getting started wiki. <https://github.com/GeoscienceAustralia/dea-notebooks/wiki>`_
      
   Digital Earth Africa
   DE Africa
      A sister project to Digital Earth Australia but for the African Continent.

      For more information, see `Digital Earth Africa <https://www.digitalearthafrica.org/>`_.

   Dynamic range
      The range between the maximum and minimum amount of input radiant energy that an instrument can measure.

   Earth Observation
   EO
      The process of acquiring observations of the Earth's surface via remote sensing instruments. These can
      include satellite-based observations, as well as drone or aerial images.

   Enhanced Thematic Mapper Plus
   ETM+
      The sensor aboard Landsat 7 that picks up solar radiation reflected by or emitted from the Earth.
      It is an enhanced version of the :term:`Thematic Mapper`.

      For more information, see `NASA Enhanced Thematic Mapper Plus. <https://landsat.gsfc.nasa.gov/etm-plus/>`_

   Ephemeris
      A table of satellite orbital locations for specific time intervals. The ephemeris data helps
      characterise the conditions under which remotely sensed data is collected and is commonly used to
      correct the sensor data before analysis.

   European Space Agency
   ESA
      The European Space Agency is a European intergovernmental collaboration focussed on the development of
      Europe's space capability. The ESA is a partner of the :term:`Copernicus Programme`.

   Exiting angle (degrees)
      The angle between a ray reflected from a surface and the line perpendicular to the surface at the
      point of emergence.

   Fractional Cover
   FC
      Fractional Cover (FC) is a DEA product that uses an algorithm to split the landscape into
      three parts, or fractions;

      * green (leaves, grass, and growing crops),

      * brown (branches, dry grass or hay, and dead leaf litter), and

      * bare ground (soil or rock).

      FC provides a representation of the proportions of living vegetation, dry and dying vegetation (including
      deciduous trees during autumn, dying grass, etc.), and bare soils across the Australian continent
      for any point in time in the Landsat archive since 1987.

      For more information, and for details of the methodology, see
      `DEA Fractional Cover. <https://www.dea.ga.gov.au/products/dea-fractional-cover>`_

   Gain
      A general term used to denote an increase in signal power in transmission from one point to another,
      usually expressed in decibels. It can also be used to represent the multiplier used to transform
      satellite image digital numbers to measures of at-sensor radiance.

   Geoscience Australia
   GA
      Geoscience Australia is the national public-sector geoscience organisation. It is the government’s
      technical advisor on all aspects of geoscience and is the custodian of geographic and geological data.
      :term:`Digital Earth Australia` is a program of Geoscience Australia.

      For more information, see `Geoscience Australia. <https://www.ga.gov.au/>`_
    
   Geomedian
      Geometric median is a robust high-dimensional statistic that maintains relationships between
      spectral bands, while producing a multi-dimensional median over a timeseries of satellite images.

      The Geometric Median provides information on the general conditions of a landscape over a timeseries.

      For more information, see `Geomedian. <https://doi.org/10.1109/TGRS.2017.2723896>`_

   Google Earth Engine
   GEE
      A Google-based platform for analysis and visualisation of geospatial datasets.
      
   Geographic Information System
   GIS
      A system that manages and visualises spatially referenced data.

   High and Low Tide Imagery
   HLTC
      Previously called High and Low Tide Composites. DEA High and Low Tide Imagery is a 
      Digital Earth Australia product providing cloud-free imagery mosaics of Australia's 
      coast, estuaries and reefs at low and high tide.

      For more information, see `DEA High and Low Tide Imagery. <https://www.dea.ga.gov.au/products/dea-high-low>`_

   High Performance Computing
   HPC
      The practice of aggregating computing power in a way that delivers much higher performance
      than one could get out of a typical desktop computer or workstation in order to solve large
      problems in science, engineering, or business.

   Incident angle (degrees)
      The angle between a ray incident on a surface and the line perpendicular to the surface at
      the point of incidence.

   Intertidal Elevation
      Previously called National Intertidal Digital Elevation Model (NIDEM). A DEA product derived 
      from DEA Intertidal Extents that maps the elevation of the Australian intertidal zone
      relative to Mean Sea Level.

      For more information, see `DEA Intertidal Elevation. <https://www.dea.ga.gov.au/products/dea-intertidal-elevation>`_

   Intertidal Extents
      Previously called Intertidal Extents Model (ITEM). DEA Intertidal Extents is a DEA product that maps the
      relative extent of the Australian intertidal zone at regular intervals of 
      the observed tidal range.

      For more information, see `DEA Intertidal Extents. <https://www.dea.ga.gov.au/products/dea-intertidal-extents>`_
      
   Jupyter notebooks
      A computational "notebook" that allows code to be run and presented alongside 
      explanatory documentation, figures, scientific notation etc.
      
   JupyterLab
      An interactive web-based user interface for editing and running Jupyter notebooks.
      JupyterLab is used as an analysis environment on both the :term:`DEA Sandbox` and the NCI's
      :term:`ARE`.

   Landsat
      A joint :term:`NASA`/:term:`USGS` program of medium resolution satellites that have been
      collecting publicly available Earth observation data continuously since 1972.

      For more information, see `Landsat Science <https://landsat.gsfc.nasa.gov/>`_.

   Land Cover Classification Scheme
   LCCS
      The Land Cover Classification Scheme was developed by the United Nations Food and Agriculture
      Organization to provide a consistent framework for the classification and mapping of land cover.

      For more information, see `LCCS. <https://www.fao.org/land-water/land/land-governance/land-resources-planning-toolbox/category/details/en/c/1036361/>`_
   
   Median Absolute Deviation
   MAD
      Median Absolute Deviation, used as a form of standard deviation for the geomedians.

      The Median Absolute Deviation provides information on how a landscape is changing over a
      timeseries.

      For more information, see `MAD. <https://doi.org/10.1109/IGARSS.2018.8518312>`_

   Moderate Resolution Imaging Spectroradiometer
   MODIS
      A sensor aboard NASA’s Terra and Aqua satellites. MODIS instruments view the entire Earth’s
      surface every 1-2 days, acquiring data in 36 spectral bands. It plays a vital role in the
      development of validated, global, interactive Earth system models which aim to accurately
      predict global change.

      For more information, see `NASA: MODIS. <https://modis.gsfc.nasa.gov/about/>`_

   MultiSpectral Instrument
   MSI
      The MSI is carried on the Sentinel-2 satellites. Light reflected up to the MSI instrument from
      the Earth and its atmosphere is collected by a three-mirror (M1, M2 and M3) telescope and
      focused, via a beam-splitter, onto two Focal Plane Assemblies: one for the ten very-near
      infrared wavelengths and one for the three shortwave infrared wavelengths.

      For more information see: `ESA missions - Sentinel-2. <https://sentinel.esa.int/web/sentinel/missions/sentinel-2>`_

   Multispectral Scanner
   MSS
      A line-scanning instrument carried by Landsat satellites that continually scans the Earth in a
      185 km swath and collects data over a variety of wavelengths.

      For more information, see `Landsat: Multispectral Scanner. <https://landsat.gsfc.nasa.gov/multispectral-scanner/>`_

   Nadir
      The point of the celestial sphere that is vertically downward from the observer and directly
      opposite the :term:`zenith`.

   Nadir-corrected :term:`BRDF` Adjusted Reflectance
   NBAR
      Surface reflectance data that has been corrected to remove the effects of topography and angular
      variation using bidirectional reflectance modelling.

   Nadir-corrected :term:`BRDF` Adjusted Reflectance with Terrain illumination correction
   NBART
      Surface reflectance data that has been corrected to remove the effects of topography and angular
      variation using bidirectional reflectance modelling, as well as corrected for the effects of terrain
      shadow.

   National Aeronautics and Space Administration
   NASA
      The United States of America's federal government's civil space, aeronautics and space research agency.
   
   National Computational Infrastructure
   NCI
      A national facility that provides world-class, high-end computing services to Australian researchers,
      including those working in the data-intensive areas of climate and Earth system science.

      For more information, see `National Computational Infrastructure <https://www.nci.org.au/>`_

   National Oceanic and Atmospheric Administration
   NOAA
      A scientific agency within the United States Department of Commerce that focuses on the conditions of
      the oceans, major waterways and atmosphere.

      For more information, see `NOAA. <https://www.noaa.gov/>`_

   Normalised Burn Ratio
   NBR
      Calculated from near-infrared (:term:`NIR`) and short wave infrared (:term:`SWIR`).

   Normalised Difference Vegetation Index
   NDVI
      Calculated from visible and near-infrared (:term:`NIR`) light reflected by vegetation.

   Near Infrared
   NIR
      Radiation just beyond the visible light spectrum. In Landsat and Sentinel 2 Earth observation
      satellites, it refers to radiation between 0.7 - 0.9 micrometers.

   Near-real time
   NRT
      NRT data is a less refined/calibrated dataset, which is available much sooner after satellite
      acquisition than standard :term:`ARD` data.

      For more information, see `DEA dataset maturity. <https://docs.dea.ga.gov.au/reference/dataset_maturity_guide.html>`_

   Open Data Cube
   ODC
      An open source geospatial data management and analysis software project. It is a global initiative
      to increase the value and use of satellite data by providing users with access to free and open
      data management technologies and analysis platforms.

      At its core, ODC is a set of Python libraries and a :term:`PostgreSQL` database that allows you to work
      with geospatial raster data.

      For more information, see `Open Data Cube. <https://www.opendatacube.org>`_

   Operational Land Imager
   OLI
      The Operational Land Imager is carried by the Landsat 8 satellite. It measures in the visible,
      near infrared (:term:`NIR`), and short wave infrared (:term:`SWIR`) portions of the spectrum. Its images
      have 15-meter (49 ft.) :term:`panchromatic` and 30-meter multi-spectral spatial resolutions along a 185 km
      (115 miles) wide swath.

      For more information, see `Landsat 8. <https://landsat.gsfc.nasa.gov/satellites/landsat-8/>`_

   Operational Land Imager 2
   OLI2
      The OLI-2 instrument is carried by the Landsat 9 satellite. It provides visible and near infrared
      / shortwave infrared (VNIR/:term:`SWIR`) imagery consistent with previous Landsat spectral, spatial, radiometric
      and geometric qualities.

      The OLI-2 instrument includes an optical telescope, Focal Plane Array / Focal Plane Electronics,
      calibration hardware, and instrument support electronics. OLI-2 provides data for nine spectral bands with a
      maximum ground sampling distance (GSD), both in-track and cross track, of 30 m (98 ft) for all bands
      except the panchromatic band, which has a 15 m (49 ft) GSD.

      For more information, see `Landsat 9 instruments. <https://landsat.gsfc.nasa.gov/satellites/landsat-9/landsat-9-instruments/>`_

   Panchromatic band
      A band that measures a wide range of light at high resolution, compared to standard multispectral
      bands that measure a narrow range of light at lower resolution. On Landsat 7, 8, and 9, the
      panchromatic band can be used to "sharpen" 30 metre visible bands to higher 15 metre resolution.

      For more information, see `Pansharpening Landsat. <https://docs.dea.ga.gov.au/notebooks/How_to_guides/Pansharpening.html>`_

   Pixel
      The minimum size area on the ground detectable by a remote sensing device. The size varies depending
      on the type of sensor.

   Pixel quality
   PQ
     A categorical assessment of the quality of an observation at the pixel level.

   Polar orbit
      An orbit with an orbital inclination of near 90 degrees where the satellite ground track will cross
      both polar regions once during each orbit. The term describes the near-polar orbits of a spacecraft.

   PostgreSQL
      Also known as Postgres, it is an open source object-relational database management system with an
      emphasis on extensibility and standards compliance. It is a high performance database engine used as
      both a relational and document database by the :term:`Open Data Cube`.

   Process
      The generation of some form of output as the result of a set of actions, which may include sub-processes.

   Product
      A categorical term applied to describe the output from a process. Typically, a product has
      an associated product definition which contains the product description and specification.

   Python
      The programming language used to develop the :term:`Open Data Cube` and most of
      :term:`Digital Earth Australia`. It is an easy to use language, which also provides simple
      access to high performance processing capabilities.

      For more information, see `Python. <https://www.python.org/>`_

   Radiance
      The amount of light directly detected by remote sensing instruments.

   Radiometer
       A device that detects and measures electromagnetic radiation.

   Radiometric
      Relating to, using, or measured by a :term:`radiometer`. The measurement of radiation.

   Raster data
      An abstraction of the real world where spatial data is expressed as a matrix of cells or :term:`pixel`s,
      with spatial position implicit in the ordering of the pixels. With the raster data model, spatial
      data is not continuous but divided into discrete units. This makes raster data particularly suitable
      for certain types of spatial operations (e.g. overlays or area calculations). Unlike :term:`vector data`,
      there are no implicit topological relationships.

   Raw data
      Numerical values representing the direct observations output by a measuring instrument. The values
      are transmitted as a bit stream in the order they were obtained.

   Real time
      The time in which reporting on events or recording of events is simultaneous with the events. For
      example, the real time of a satellite is the time in which it simultaneously reports its environment
      as it encounters it.

   Reflectance
      The measure of the proportion of light or other radiation striking a surface which is reflected off it.

   Relative azimuth (degrees)
      The relative :term:`azimuth` angle between the sun and view directions.

   Relative slope (degrees)
      The relative :term:`azimuth` angle between the incident and exiting directions in the slope geometry.

   Remote sensing
      The measurement or acquisition of information about some property of an object or phenomenon, by a
      recording device that is not in physical or intimate contact with the object or phenomenon under study.

   Resampling
      Modifying the geometry of an image, which may be from either a remotely sensed or map data source.
      This process usually involves rectification and/or registration.

   Resolution
      A measure of the amount of detail that can be seen in an image; i.e. the size of the smallest object
      recognisable using the detector.

      In remotely sensed imagery, resolution is significant in four measurement dimensions: spectral, spatial,
      radiometric and temporal.

   Satellite azimuth (degrees)
      The angle of the satellite’s position from true north; i.e. the angle between true north and a
      vertical circle passing through the satellite and the point being imaged on Earth.

   Satellite view or satellite zenith (degrees)
      The angle between the zenith and the satellite.

   Saturation
      The intensity of a colour. A highly saturated colour is vivid and brilliant. To dull a colour and
      decrease its saturation, add small amounts of its complement, making it closer to grey.

   Scene
      A defined portion of the continuous strips of data collected by satellites. Satellite data is broken up
      into scenes for ease in handling and cataloguing.

   Secure Shell
   SSH
      SSH or Secure Shell is a means to access remote computers using a text based
      terminal interface. It comes build in with Linux, but requires additional software
      to use it from Windows computers.

   Sentinel
      A program of satellites from Europe that collect publicly available Earth
      observation data. Each satellite has a different purpose or capability, and together, they address six
      thematic areas: land, marine, atmosphere, climate change, emergency management and security.

      For more information, see `Copernicus: Discover our satellites. <https://www.copernicus.eu/en/about-copernicus/infrastructure-overview/discover-our-satellites>`_

   Short-Wave Infrared
   SWIR
      Radiation beyond the visible light spectrum. In Landsat and Sentinel 2 Earth observation
      satellites, it refers to radiation between 1.5 - 2.4 micrometers.

   Solar azimuth (degrees)
      The angle of the sun’s position from true north; i.e. the angle between true north and a vertical
      circle passing through the sun and the point being imaged on Earth.

   Solar irradiance
      The solar irradiance is the output of light energy from the entire disk of the Sun, measured at
      the Earth.

   Solar zenith (degrees)
      The angle between the :term:`zenith` and the centre of the sun’s disc.

   Solar Zenith Angle (SZA)
      The angle between the local :term:`zenith` (i.e. directly above the point on the ground) and
      the line of sight from that point to the sun.

   Spatial resolution
      The area on the ground that an imaging system, such as a satellite sensor, can distinguish.

      See also :term:`resolution`.

   Spectral response
      The ratio of the relative amplitude of the response of a detector and the frequency of
      incident electromagnetic radiation.

   Spectrometer
      An optical instrument that splits the light received from an object into its component
      wavelengths by means of a diffraction grating, and then measures the amplitudes of the
      individual wavelengths.

   Sun-synchronous orbit
      An orbit in which a satellite is always in the same position with respect to the rotating
      Earth at the same time of day.

   Surface reflectance
      The fraction of incoming solar radiation that is reflected from Earth's surface for specific
      incident or viewing cases (directional, conical, and hemispherical cases).

   Synthetic Aperture Radar
   SAR
      An imaging radar mounted on an instant moving platform. The signal is responsive to surface
      characteristics like structure and moisture.

      For more information, see: `NASA - What is Synthetic Aperture Radar? <https://www.earthdata.nasa.gov/learn/backgrounders/what-is-sar>`_

   Telemetry
      The science and technology of automatic measurement and transmission of data by wire,
      radio or other means from remote sources (e.g. space vehicles) to receiving stations
      for recording and analysis.

   Thematic Mapper
   TM
      An advanced, multispectral-scanning, Earth resources sensor featured on Landsat 4 and 5.
      TM is designed to acquire data to categorise the Earth's surface and is particularly useful
      for agricultural applications and identification of land use. It continuously scans the surface
      of the Earth, simultaneously acquiring data in seven spectral channels.

      For more information, see `NASA Thematic Mapper Plus. <https://landsat.gsfc.nasa.gov/thematic-mapper/>`_

   Thematic Real-time Environmental Distributed Data Services
   THREDDS
      An National Computational Infrastructure (:term:`NCI`) server, which is a high-performance and
      high-availability installation of Unidata's Thematic Real-time Environmental Distributed Data
      Services (THREDDS).

      THREDDS serves many of NCI’s open data collections at the file level, as well as some aggregations.
      It provides many different types of services to allow individual files to be selected, as well as
      more advanced services such as OpenDAP, NetCDF subsetting, OGC WCS and WMS.

      For more information, see `NCI: Data Services. <https://nci.org.au/our-services/data-services>`_

   Timedelta (seconds)
      The time in seconds from satellite apogee (the point of orbit at which the satellite is furthest
      from the Earth).

   United States Geological Survey
   USGS
      A scientific agency of the United States government. The scientists of the USGS study the landscape
      of the United States, its natural resources, and the natural hazards that threaten it. The USGS and
      :term:`NASA` jointly run the Landsat program of earth observation satellites.

      For more information, see `USGS. <https://www.usgs.gov/>`_

   Vector data
      Vector data, when used in the context of spatial or map information, refers to a format where all
      map data is stored as points, lines, and areas rather than as an image or continuous tone picture.
      These vector data have location and attribute information associated with them.

   Virtual Desktop Infrastructure
   VDI
      The Virtual Desktop Infrastructure was a service offered by the :term:`NCI`
      that provided a linux desktop environment for scientific computing. It has
      been replaced by :term:`ARE`.

   Visible Infrared Imaging Radiometer Suite
   VIIRS
      The Visible Infrared Imaging Radiometer Suite (VIIRS) is one of the key instruments onboard the
      NOAA-20 spacecraft, as well as the Suomi-NPP satellite. It collects visible and infrared imagery
      and global observations of land, atmosphere, cryosphere and oceans.

      For more information, see `Joint Polar Satellite System. <https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system>`_

   Water Observation Feature Layer
   WOFL
      A :term:`WO` observation for one point in time

   Water Observations
   WO
      Previously called Water Observations from Space. A Digital Earth Australia product that classifies
      satellite pixels into 'wet', 'dry', or 'invalid' (e.g. cloudy or a poor quality observation).

      For more information see `Water Observations. <https://www.dea.ga.gov.au/products/dea-water-observations>`_

   Wavelength
      The distance from crest to crest, or trough to trough, of an electromagnetic or other wave. The longer
      the wavelength, the lower the frequency.

   Web Map Service
   WMS
      A HTTP interface for requesting geo-registered map images that can be displayed in a browser application
      or GIS software system.

   Web Feature Service
   WFS
      An interface for querying, modifying and exchanging features or values in a database and retrieving features
      for use.

   World Reference System
      A global indexing scheme designed for the Landsat Program. It is based on nominal scene centres defined
      by path and row coordinates.

      For more information, see `NASA: World Reference System. <https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/>`_

   xarray
      An open source project and Python package for working with labelled
      multi-dimensional arrays such as those returned by the :term:`Open Data Cube` (ODC).

   Yet Another Markup Language
   YAML
      A human readable data storage format.
      It is used throughout :term:`DEA` for metadata files, product
      definitions and other configuration files.

   Zenith
      The point on the celestial sphere directly above the observer, and directly opposite to :term:`nadir`.

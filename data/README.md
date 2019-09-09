More data can be generated with  [JPetGeant4](https://github.com/JPETTomography/J-PET-geant4)
software.

Configuration used for 'extended_geometry' file:

/jpetmc/detector/loadGeomForRun 6 
/jpetmc/detector/loadOnlyScintillators
/jpetmc/detector/loadModularLayer true
/jpetmc/event/saveEvtsDetAcc true
/jpetmc/event/ShowProgress true

/jpetmc/material/xad/oPsFraction 0.9999 
/jpetmc/material/xad/pickOffFraction 0.0  

/run/initialize

/run/beamOn 100000


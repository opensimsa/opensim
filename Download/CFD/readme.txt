FreeCAD v0.17.10423 with CSIR CFD workbench

Installation Instructions - Windows 7 & 10

===========================================


1. Installation of dependency

-----------------------------

The Windows installation is dependent on the BlueCFD-Core Project (bluecfd.github.io/Core/). BlueCFD-Core
version 2016-1 should be downloaded from http://bluecfd.github.io/Core/Downloads/

Exact download link:

   https://github.com/blueCFD/Core/releases/download/blueCFD-Core-2016-1/blueCFD-Core-2016-1-win64-setup.exe

Once downloaded, double-click the blueCFD-Core-2016-1-win64-setup.exe file. The
software can be installed with default options.


2. Installation of FreeCAD package

----------------------------------

The compressed file FreeCAD_0.17.10432.csir_x64_dev_win.zip should be extracted and placed in any 
desired location, e.g. Program Files folder. A shortcut can be created pointing to

<Install location>FreeCAD_0.17.10432.csir_x64_dev_winbinFreeCAD.exe

in order to run the program.


3. Set-up of BlueCFD folder

---------------------------

The first time before running a case, once the "Analysis Control" task panel is open
(see user documentation), click on 

  Tools | Edit Parameters ...

and navigate to

  Preferences | Mod | Cfd | OpenFOAM

and edit the Installation Path parameter. Set this to

  <blueCFD Path>OpenFOAM-4.x

where <blueCFD Path> is the location of the installation of BlueCFD-Core in step 1 above - default value

  C:Program FilesblueCFD-Core-2016


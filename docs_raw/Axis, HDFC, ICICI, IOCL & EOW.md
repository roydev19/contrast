# Axis, HDFC, ICICI, IOCL & EOW
Sure, here are separate insights for Axis, HDFC, ICICI, IOCL, and EOW:

Axis:

*   Axis is involved in one API, which uses a synchronous RFC channel to send information.
*   The live status marked as "Completed", indicating that the transfer of this data is executed successfully.
*   The application name for Axis is "Axis", and it appears to be communicating with ABGPlanet.
*   In this set-up, the PR system is being used and the frequency of data exchange is 3000.

HDFC:

*   HDFC has multiple APIs, such as ECMS Cust Payment, Alert App Customer Payment, and ECMS Cust Payment BPD.
*   These APIs communicate information through synchronous SOAP channels.
*   Live status for all APIs is "Completed", indicating successful data transfer currently.
*   HDFC - RMC, HDFC - Cement, and HDFC - BPD are the associated applications for these APIs.
*   HDFC primarily communicates with the server host [vs4grpcsprd.abgplanet.abg.com](http://vs4grpcsprd.abgplanet.abg.com/), which seems to be part of ABGPlanet.
*   HDFC uses both PO system and DR system. The frequency of data exchange varies among APIs, and includes 100, 3000, and 70.

ICICI:

*   ICICI is involved in one API, Corporate Alert App Customer Payment, which uses synchronous REST channels for communication.
*   The live status for the API is marked as "YTD" (yet to decide) and the status of the API moved to Prod DR is marked as "Y".
*   The associated application for the API is ICICI - CEMENT.
*   ICICI communicates with [vs4grpcsprd.abgplanet.abg.com](http://vs4grpcsprd.abgplanet.abg.com/), which seems to be part of ABGPlanet.

IOCL:

*   IOCL is involved in one API, IOCL to S4, for sending asynchronous data.
*   The API uses REST channels for communication.
*   The live status for the API is marked as "Completed", which suggests that the data transfer is successful and ongoing.
*   The application associated with IOCL is IOCL and the host server communicating is [www.pr.eye2serve.com](http://www.pr.eye2serve.com/).
*   PR system is used in this scenario.

EOW (Autoplant):

*   EOW, or AutoPlant, is involved in multiple APIs such as DI CREATE EOW, Trip Details Completion EOW, Plant IN OUT LOAD EOW, Delivery Weight update for bulker.
*   These APIs communicate data using both synchronous and asynchronous SOAP channels, depending on the use case.
*   Live status for all these APIs is marked as "Completed", which suggests that the data transfer is successful and ongoing.
*   The applications associated with these APIs are EOW(Autoplant) - Abhishesk JI, AutoPlant, and EOW\_Plant.
*   The communicating server host varies and includes 10.1.57.55, 10.120.11.60, and [vs4grpcsprd.abgplanet.abg.com](http://vs4grpcsprd.abgplanet.abg.com/).
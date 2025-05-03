# BATCHING & BPD
The data reflects information about the SAP Process Integration (PI) / Process Orchestration (PO) systems respectively, focusing on running interfaces within these systems.

1.  SOAP and Proxy are the most commonly used Sender and Receiver Adapters among all the interfaces.
2.  For most of the interfaces, the interface mode is Synchronous. However, some interfaces also use Asynchronous mode.
3.  The Component BATCHING\_BUSS is a frequent sender in many interfaces while the component BS\_GRP300 is a common receiver.
4.  Various scenarios are covered in these interfaces like "RMC Ticketing Information", "RMC Tickets Acknowledgement", "RMC Tickets Cancellation", "Customer Creation Automation", etc.
5.  Most of the interfaces have completed the 'go-live' status, indicating that they are fully functional and live in production.
6.  The majority of interfaces consider the PR system (Primary system), with some also incorporating the DR (Disaster Recovery) system.
7.  Frequent connections are established with the "[http://ultratech.rmc.com](http://ultratech.rmc.com/)" namespace.
8.  Not all interfaces use Message Prioritization and PI Receiver Parallelism which might be related to their business priority or technical configuration.
9.  In some interfaces, JDBC Polling time has been established, suggesting active involvement with databases.
10.  The frequency of the interfaces varies. Some interfaces have a high frequency indicating high volume of data, whereas some interfaces show "No recent data", implying they may not be active or not frequently used.

Please note that these insights are general and made based on provided data. For a more accurate understanding, a more profound examination should be performed considering factors like business processes, their criticality, time of execution, and other factors.
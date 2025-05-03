# BCP
The provided dataset describes the sending and receiving activities of various software components in specified departments of a company. Key insights that can be derived include:

1.  Usage of Interface: The 'ASynchronous' interface mode is being utilized for all activities in the dataset.
2.  Sender Composition: The sender components are majorly 'BS\_GRP300' and 'BC\_BCP' in the 'MKT' department.
3.  Usage of Different Adapters: 'IDOC' and 'REST' are the most frequently used adapters. Also, 'Proxy' adapter is used in some cases.
4.  Receiver Organization: The received components are 'BC\_BCP' and 'BS\_GRP300'.
5.  Connection Details: Connection details for sending data majorly includes addresses starting with '[http://10.47.16.250/](http://10.47.16.250/)'. On the other hand, receivers mainly use 'HTTP\_Destination\_GRP300'.
6.  Status: All components are 'Completed' for go-live status.
7.  Synchronous System: In all instances mainly 'PRsystem' is used.
8.  Frequency: There is significant range in frequency for data transmission. While some instances have very high frequency up to 96001, other instances have frequency as low as 1.
9.  Authentication: Username 'SAPtoBCPSyncUser' with password 'S@pD@t@Sync123' is frequently used.
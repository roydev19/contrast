# C4, CAPEX, CIS, LABSYS, BPD, and UBS.
1.  The sender components are mainly from "BS\_GRP300", "LABSYS\_BUSS", and “BusSer\_BPD”. While the receiver component includes "BC\_SCPI", "LABSYS\_BUSS", and "BS\_GRP300".
2.  In most cases, the interface mode used is "ASynchronous", which means that the sender sends a request and then carries on with its own execution without waiting for a response from the receiver.
3.  Different types of adpaters are used, depending on the necessity. They include "IDOC", "RFC", "SOAP", and "JDBC".
4.  The connectivity between sender and receiver in most cases is carried out via API (Application Programming Interface) where sender username and receiver username are provided with secure passwords.
5.  "Completed" is a common status in "status for go-live" field, indicating that most interfaces were able to go live successfully.
6.  In some cases, the InterfaceStatus shows "Recevier Channel Stopped" and "Stopped", indicating that these interfaces might have run into issues and their operations have been halted.
7.  The "Frequency" in these interfaces varies depending on the use case. Some interfaces don't have recent data, which might suggest they are not in active use.
8.  Some interfaces marked as "PassThrough" as "Yes" means they simply relay the received message with no middle processing.
9.  Key application areas include "C4", "LABSYS ", "BPD", and "UBS".

Please note, these are broad insights and may vary based on the system setup and business use-case.
# monitoring
There are several monitoring Transaction Codes (T-codes) used in the SAP S4 and ECC systems. These are primarily used for administration purposes, such as system monitoring, user monitoring, and performance tuning. Here are some commonly used ones:

SM04: SM04 allows you to view the users logged in to an instance.

SM12: With SM12, you can display and delete locks in the SAP system.

SM13: SM13 offers an overview of update records, and if necessary, you can also reset the status of erroneous update requests.

SM21: Checks system logs for warnings, errors, etc.

ST03: ST03 helps in monitoring system workload.

ST22: ST22 is used for analyzing ABAP dumps.

SM50: SM50 is used for Process Overview.

SM51: To see all SAP instances in the system.

SM58: With SM58, you can monitor the transactional Remote Function Call (tRFC).

SM66: SM66 provides you a global work process overview.

SP01: This code is used to monitor spool requests.

SMQ1 / SMQ2: SMQ1 and SMQ2 are used for qRFC (queued Remote Function Call) Monitor.

Note, all these transaction codes are commonly used, but their access generally requires administrative privileges, so a regular user may not have access to these functions. And also it may differ slightly depending on the version of SAP (R/3, S/4HANA, ECC) you are using.

SXMB\_MONI: SXMB\_MONI is a SAP transaction code for 'Integration Engine - Monitoring'. It is mainly used in troubleshooting scenarios, when there are issues in XI messages. It can process XML messages that can be viewed in different stages such as inbound, outbound, pipeline. This code is often used by consultants who are working with XI/PI (Process Integration).

SMQ1: The SAP T-Code SMQ1 is used for qRFC (Queue Remote Function Call) Monitor for the outbound queue. It is used to check and monitor the outbound queues in the SAP system. It can be used for troubleshooting during issues related to asynchronous data transfer between systems, especially in ALE, IDOC scenarios.

SMQ2: Similarly, SAP T-Code SMQ2 is used for qRFC Monitor for the inbound queue. It is used to monitor and troubleshoot problems in the inbound queues during asynchronous data transfer between systems.

WE02: WE02 is a SAP T-Code used for 'IDoc List'. This code mainly helps in displaying a list of IDocs (Intermediate Documents). These are used in SAP for the transfer of application data to other systems. This is useful in situations where you need to track the status of specific IDocs and diagnose problems related to them.

SM58: SM58 is a SAP Transaction Code for 'Transactional RFC'. This transaction code is used to analyze and troubleshoot any failures encountered with asynchronous RFC calls. It is often needed in situations where remote function calls are made from the system and those calls fail due to connection issues, system failures or application errors.
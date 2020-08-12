# Why Is Available Memory of Unused DCS Instances Less Than Total Memory? Why Is Memory Usage of Unused DCS Instances Greater Than Zero?<a name="en-us_topic_0057984494"></a>

Before a newly created DCS instance is put into use, the available memory is less than the total memory because some memory is reserved for system overhead and data persistence \(supported by master/standby instances\). For more information about the available memory for each type of DCS instance, see  [DCS Instance Specifications](dcs-instance-specifications.md).

DCS instances use a certain amount of memory for Redis-server buffers and internal data structures. This is why memory usage of unused DCS instances is greater than zero.


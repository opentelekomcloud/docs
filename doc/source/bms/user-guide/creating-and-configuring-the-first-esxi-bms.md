# Creating and Configuring the First ESXi BMS<a name="EN-US_TOPIC_0159392255"></a>

1.  Log in to the management console. 
2.  Create a BMS. Select a flavor and ESXi image \(see  [Table 3](environment-preparations.md#table5655194511448)\) and configure the VPC to which it connects. Set other parameters as required.
3.  Apply for an EIP and bind it to the BMS port connected to the esx-primary network.
4.  Use the EIP and key pair to log in to the ESXi BMS and change the user  **root**  password of the host.
5.  Enter the EIP of the primary NIC of the ESXi BMS in the browser to log in to the ESXi host.
6.  Add datastores to the ESXi host.


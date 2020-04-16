# How Can I Back Up the RDS Database to an ECS?<a name="rds_faq_0042"></a>

You can back up data to an ECS the same way you export SQL statements. The ECS service does not restrict types of data to be backed up. The data only needs to meet national laws. You can store RDS backup data on an ECS. However, you are advised not to use an ECS as the database backup space. You are advised to use the RDS backup function to store backups to a professional storage object, such as the OBS, to ensure high data reliability and service assurance.


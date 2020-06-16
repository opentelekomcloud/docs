# Do I Need to Stop the Server Before Backing Up EVS Disks on a Server Using VBS?<a name="EN-US_TOPIC_0015667851"></a>

VBS can back up EVS disks that are being used. When a server is running, data is written onto EVS disks on the server, and some newly generated data is stored in the server memory as cached data. During EVS disk backup, the data in the memory will not be automatically written onto the EVS disk, resulting in data inconsistency between the EVS disk and its backup.

To ensure data consistency and integrity, back up EVS disks during off-peak hours when no data write operations are being performed on the EVS disks, or stop all data write operations on the EVS disks before backup. For a strict requirement for data integrity, stop the server \(cached data is written to EVS disks\) and start an offline backup job.


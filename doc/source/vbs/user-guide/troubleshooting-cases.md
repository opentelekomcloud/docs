# Troubleshooting Cases<a name="EN-US_TOPIC_0035111666"></a>

## Symptom<a name="section2019936218759"></a>

Failed to attach EVS disks despite following the procedure: Create EVS disks using the same VBS backup \(XFS file system backup\) and attach them to the same server \(to which multiple EVS disks with XFS file system backup have been attached\). Running the  **mount**  command to attach EVS disks fails.

## Possible Causes<a name="section3606783818917"></a>

The superblock of an EVS disk \(with XFS file systems\) stores a universally unique identifier \(UUID\) about the file system. If a server has multiple disks \(with XFS file systems\), multiple UUIDs will exist on the server. Multiple disks may have the same UUID, which can cause the file system mounting to fail.

## Fault Diagnosis<a name="section56169881181031"></a>

When attaching an EVS disk, use parameters without UUID control or reallocate a new UUID to ensure that each UUID is unique.

## Procedure<a name="section49413786181113"></a>

1.  Log in to the server to which EVS disks failed to be attached.
2.  Resolve the problem in either of the following ways:

    -   Use a parameter without UUID when attaching an EVS disk: Run  **mount -o nouuid /dev/_Device name_  /_Mount path_**, for example:

        **mount -o nouuid /dev/sda6 /mnt/aa**

    -   Reallocate a new UUID: Run  **xfs\_admin -U generate /dev/**_Device name_.

    >![](/images/icon-note.gif) **NOTE:**   
    >Because setting a parameter without UUID requires you to execute the command every time, you are advised to reallocate a new UUID.  



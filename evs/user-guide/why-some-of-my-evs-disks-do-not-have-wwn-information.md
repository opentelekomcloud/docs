# Why Some of My EVS Disks Do Not Have WWN Information?<a name="evs_faq_0021"></a>

EVS disks have two device types: VBD and SCSI. WWNs are used as the unique identifiers for SCSI EVS disks, and VBD EVS disks do not have WWNs.

You can view the WWN of a SCSI EVS disk on the management console. The details are as follows:

-   If the SCSI EVS disk is brand new, you can view the disk WWN on the disk details page.

    [Figure 1](#fig10936527101715)  shows the query result.

    **Figure  1**  Queried WWN information<a name="fig10936527101715"></a>  
    ![](figures/queried-wwn-information.png "queried-wwn-information")

-   If the SCSI EVS disk is created before the WWN feature rollout, the disk WWN will fail to obtain.

    [Figure 2](#fig1293431911208)  shows the query result.

    **Figure  2**  No WWN information<a name="fig1293431911208"></a>  
    ![](figures/no-wwn-information.png "no-wwn-information")



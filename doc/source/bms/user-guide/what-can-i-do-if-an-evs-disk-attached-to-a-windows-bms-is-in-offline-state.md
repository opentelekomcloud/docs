# What Can I Do If an EVS Disk Attached to a Windows BMS Is in Offline State?<a name="EN-US_TOPIC_0103482177"></a>

## Symptom<a name="section123870357116"></a>

After an EVS disk is attached to a Windows BMS, start  **Control Panel**, choose  **System and Security**  \>  **Administrative Tools**, and double-click  **Computer Management**. On the  **Computer Management**  page, choose  **Storage**  \>  **Disk Management**. The EVS disk attached to the BMS is in  **Offline**  state.

## Solution<a name="section4448543152417"></a>

1.  Log in to the Windows BMS.
2.  Click  **Start**, enter  **cmd**  in  **Search programs and files**, and press  **Enter**  to open the command-line interface \(CLI\).
3.  Type  **diskpart**.

    ```
    C:\Users\Administrator>diskpart
    ```

4.  Type  **san**.

    ```
    DISKPART> san
    SAN Policy: Online All
    ```

5.  Type  **san policy=onlineall**.

    ```
    DISKPART> san policy=onlineall
    DiskPart successfully changed the SAN policy for the current operating system
    ```

6.  Type  **list disk**  to display all disks of the BMS.

    ```
    DISKPART> list disk
    Disk ### Status    Size    Free     Dyn    Gpt
    Disk 0   Online   838 GB    0B
    Disk 1   Offline   838 GB    838 GB
    Disk 2   Offline   838 GB    838 GB
    Disk 3   Offline   838 GB    838 GB
    ...
    ```

7.  Type  **select disk** _num_.  _num_  indicates the disk number. Replace it with the specific disk number.

    ```
    DISKPART> select disk 4
    ```

8.  Type  **attributes disk clear readonly**.

    ```
    DISKPART> attributes disk clear readonly
    DiskPart succeed to clear disk attributes.
    ```

9.  Type  **online disk**.

    ```
    DISKPART> online disk
    DiskPart succeed to make the selected disk online.
    ```

10. After the modification, format the EVS disk.


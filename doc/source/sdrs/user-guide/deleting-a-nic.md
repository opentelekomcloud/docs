# Deleting a NIC<a name="sdrs_ug_pi_0007"></a>

## Scenarios<a name="section29001518165019"></a>

A protected instance can have up to 12 NICs, including one primary NIC that cannot be deleted. You can perform steps provided in this section to delete a NIC other than the primary one.

## **Prerequisites**<a name="section149031918165016"></a>

-   The protection group is in the  **Available**  or  **Protecting**  state.
-   The protected instance is in the  **Available**  or  **Protecting**  state.
-   The primary NIC cannot be deleted.

## Procedure<a name="section96871927125019"></a>

1.  Log in to the management console.
2.  Click  **Service List**  and choose  **Storage**  \>  **Storage Disaster Recovery Service**.

    The  **Storage Disaster Recovery Service**  page is displayed.

3.  In the pane of the protection group for which a NIC is to be deleted from the protected instance, click  **Protected Instances**.

    The operation page for the protection group is displayed.

4.  On the  **Protected Instances**  tab, click the protected instance.

    The  **Protected Instance Details**  page is displayed.

5.  Click the  **NICs**  tab. Then, click  **Delete**  in the row that contains the NIC to be deleted.
6.  Click  **Yes**.


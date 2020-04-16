# Why Does the DB Instance Become Faulty After the Original Database Port Is Changed?<a name="rds_faq_0035"></a>

## Symptom<a name="sc599b6af5628403c99d7b598212c947e"></a>

-   The DB instance is in  **Faulty**  state after the original database port is changed.
-   The DB instance cannot be connected using the new database port.

## **Possible Causes**<a name="scdd5c81165d64e3b99b5d591249f21a9"></a>

The submitted database port is occupied.

## Procedure<a name="s901c1fbe15e64306ba114910b0b781e9"></a>

Change the original database port to the new port again. For details, see  [Changing the Database Port](changing-the-database-port.md).

-   If the original database port is changed successfully, the previous change failed because the submitted database port is occupied.
-   If the original database port still fails to be changed, contact technical support.


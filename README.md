## ERPNext Xero Connect

This is alpha software, and is not usable yet.

ERPNext Xero connect is a Frappe app that synchronizes the following
ERPNext and Xero resources;

- ERPNext Stock Item to Xero Inventory Item (Not implemented)
- ERPNext Customers to Xero Contacts (Not implemented)
- ERPNext Suppliers to Xero Contacts (Not implemented)
- ERPNext Sales Invoice to Xero Sales Invoice (Not implemented)
- ERPNext Purchase Invoice to Xero Bill (Not implemented)



#### License

MIT

### Set up Xero API Credentials

Go to: https://app.xero.com/Application/Add
Select "Private Application"
Give your credentials a name, such as "erp_xero_connect" for example.

Generate a public/private key;

- `openssl genrsa -out privatekey.pem 1024`
- `openssl req -new -x509 -key privatekey.pem -out publickey.cer -days 1825`
- `openssl pkcs12 -export -out public_privatekey.pfx -inkey privatekey.pem -in publickey.cer`


Upload the `publickey.cer` file to the Xero API form.

Leave "Enable Payroll API for this organisation" unchecked. 
Check the box to accept the Xero API terms and conditions.

Click Save


In ERPNext, navigate to the ERPNext Xero Connect Settings page.

- Copy the `Consumer Key` from the Xero Application Add (as above) page.
- Copy the `Consumer Secret` from Xero to the corresponding file in ERP
  Xero Settings.
- Copy the contents of the `privatekey.pem` file you created earlier, and
  paste it into the corresponding ERP Xero Settings field.

Click `Save`


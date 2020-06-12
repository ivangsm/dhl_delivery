# DHL delivery
 

DHL delivery provides DHL API Services. It is simple to use.

**Below are list of available services or operations**

   1. DHL Quote and Capability Service.
   2. DHL Shipment Validation and Obtain shipment details and event visibility filtered by Waybill.
   3. DHL Label Image utility – Generates DHL compliant label image using the XML response from Shipment Validation.
   4. DHL Pickup Booking
   5. DHL Tracking and modify or delete courier pick-up (Not impleminted yet but planned to implement it soon)
   6. Internally Check If Response Available form DHL
   7. Spacify Maximum Execution Time - For how many second the API should try to get response from DHL

# Get Started - Install

**How to install**

`pip install dhl_delivery` 

Usage - DHL Quote and Capability Service
========================================

**Example to get Quote and Capability Service - get the DHL delivery
Charges**

``` python
   import dhl_delivery

   # these two generally your company need to contact DHL to obtain form DHL
   dhl_delivery.dhl_site_id = 'your DHL site id - obtained from DHL'
   dhl_delivery.dhl_site_password = 'your DHL Site Password - obtained from DHL' 
   dhl_delivery.dhl_account_no = 'your DHL [ayment account number - obtained from DHL'  # set it to get correct rate

   # Spacify Maximum Execution Time (in second) - For how many second the API should try to get response from DHL (Multiprocess)
   dhl_delivery.max_response_time = 30 

   # the From and to Address - only mendatory fields are provided here
   quote_address = {
       'from_country': 'AU',
       'from_city': 'Melbourne',
       'from_zipcode': '3000',

       'to_country': 'MY',
       'to_city': 'Kuala Lumpur',
       'to_zipcode': '50200'
   }

   # the unit of measurements - only mendatory fields are provided here
   quote_unit = {
       'dimension_unit': 'CM',
       'weight_unit': 'KG'
   }

   # Pieces as List of Dictionary - it can be one ore more pieces - here with two pieces example
   piece_one = {
       'piece_id': '1',
       'piece_height': '15',
       'piece_depth': '15',
       'piece_width': '15',
       'piece_weight': '1'
   }
   piece_two = {
       'piece_id': '2',
       'piece_height': '2',
       'piece_depth': '2',
       'piece_width': '2',
       'piece_weight': '2'
   }
   # Create the list with multiple (here 2) pieces
   quote_pieces = []
   quote_pieces.append(piece_one)
   quote_pieces.append(piece_two)

   # Some oter data
   quote_optional_data = {

       'is_dutiable': 'Y',  # Y|N
       'declared_currency': 'MYR',  # currency code of To Country
       'declared_value': '150.00',

       'insured_value': '100.00',   # Optional
       'insured_currency': 'MYR',   # Optional
   }

   # Finally preapre the data to send to the API 
   quote_data_to_send = {
       'addresses': quote_address,
       'units': quote_unit,
       'pieces': quote_pieces,
       'optional_data': quote_optional_data,
   }

   # with the prepare data call the function and get the response
   dict_response = dhl_delivery.quote.get_quote(quote_data_to_send)
```

**The Reponse you will get will look similar to**
   

``` javascript
   {
       status: true,
       message: "DHL quotes returned."
       quote_data: {
           delivery_charge: "572.800",
           local_product_name: "EXPRESS WORLDWIDE NONDOC",
           product_shortName: "EXPRESS WORLDWIDE",
           dimensional_weight: "3.000",
           weight_unit: "KG",
           currency_code: "MYR"
       }
   }
```

Usage - DHL Shipment
====================

**Example DHL Shipment Validation - DHL Label Image utility - Label
Creation (PDF File) - Airway Bill Number - Pickup - Pickup Reference
Number**

``` python
   import dhl_delivery

   # these three generally your company need to contact DHL to obtain form DHL
   dhl_delivery.dhl_site_id = 'your DHL site id - obtained from DHL'
   dhl_delivery.dhl_site_password = 'your DHL Site Password - obtained from DHL' 
   dhl_delivery.dhl_account_no = 'obtained from DHL'

   # the From and to Address - only mendatory fields are provided here
   address_details = {
       'from_company_name': 'Shopandbox',
       'from_address_line_one': 'some from address',
       'from_address_line_two': 'some from address 2',  # optional
       'from_city': 'New York',
       'from_zipcode': '10022',
       'from_country': 'US',  # two letter abbriviation
       'from_country_name': 'United States',  # country full name
       'from_name': 'SNB Test',
       'from_phone_no': '1111111',
       'from_state': '',  # only for pickup (from_state) - max 35v char - Optional

       'to_company_name': 'Test Company',
       'to_address_line_one': 'some address',
       'to_address_line_two': 'some address two',  # optional
       'to_city': 'Kuala Lumpur',
       'to_zipcode': '50200',
       'to_country': 'MY',  # two letter abbriviation
       'to_country_name': 'Malaysia',  # country full name
       'to_name': 'Hasan Test',
       'to_phone_no': '3333333',
   }

   # Detail about the package - box
   package_details = {
       'package_type': 'DF',  # DF|YP etc
       'total_weight': '2',  # total weight
       'dimension_unit': 'C',
       'weight_unit': 'K',
       'global_product_code': 'P',
       'local_product_code': 'P',
       'door_to': 'DD',
       'shipment_date': '2016-03-25',  # YYYY-mm-dd format
       'content_description': 'Some Content',
       'declared_value': '1.00',
       'declared_currency': 'USD',
       'is_dutiable': 'Y',
       'insured_amount': '100',  # Insured Amount (Required if Special Service of I
       'special_service_type': 'I',  # optional
       'reference_id': '1213122'  # any arbitrary or random number
   }

   # Pieces as List of Dictionary - it can be one ore more pieces - here with two pieces example
   piece_one = {
       'piece_id': '1',
       'package_type': 'DF',  # DF|YP etc - this one can be made optional as package details has the same param
       'piece_height': '1',
       'piece_depth': '1',
       'piece_width': '1',
       'piece_weight': '1'
   }
   piece_two = {
       'piece_id': '2',
       'package_type': 'DF',  # DF|YP etc
       'piece_height': '2',
       'piece_depth': '2',
       'piece_width': '2',
       'piece_weight': '1'
   }
   # Create the list with multiple (here 2) pieces
   pieces_details = []
   pieces_details.append(piece_one)
   pieces_details.append(piece_two)

   # set up for the shipment awb file path and name - if provided then pickup will be created else no pickup
   optional_data = {
       'awb_pdf_file_path': 'path/where/you /want/to/store/the/awb/pdf/file/',
       'awb_pdf_file_name': 'myfile.pdf',  # name of the file 
   }

   # only for pickup - no need to set it if no pick up needed
   pickup_details = {
       'pickup_date': '2016-02-25',  # YYYY-MM-DD format
       'ready_by_time': '14:30',  # hh:mm ie 14:35
       'close_time': '15:30',  # hh:mm ie 15:35
   }

   shipment_data_to_send = {
       'addresses': address_details,
       'package': package_details,
       'pieces': pieces_details,
       # only for pickup not for shipment - if provided then pickup will be created else no pickup
       #'pickup_details': pickup_details,  
       'optional_data': optional_data
   }

   # with the prepare data call the function and get the response
   dict_response = dhl_delivery.shipment.get_shipment(shipment_data_to_send)
```

**The response you will get will look similar to**

``` javascript
   {
       pickup_response: {
           //if in request data pickup details provided then here you will get the status True on success and False on fail
           status: false,  
           //if in request data pickup details provided then this will be True
           request_for_pickup: false,  
           message: "", 
           //if in request data pickup details provided then here you will get the pick up confirmation number
           pickup_confirmation_number: ""  
       },
       shipment_response: {
           status: true,
           awb_pdf_file_path_name: "pdf_shipment_label_2/9687040086__awb_15.pdf",
           message: "DHL Shipment created.",
           awb_pdf_file_name: "9687040086__awb_15.pdf",
           airway_bill_number: "9687040086"
       }
   }
   ```

Remove - Uninstall
==================

**How to uninstall**

`pip uninstall dhl_delivery` 

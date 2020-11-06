# Election Fraud 2020 Center


### Repo Layout

```
/2digitStateCode/parse_registration.py # Converts states data to Registration Data Format
/2digitStateCode/README.MD # links to all data with instructions on how to download
```


### Registration Data Format

```
{
   first: '',
   middle: '' ,
   last: '',
   suffix: '',
   zip: XXXXX, // 5 digit 
   street: '',
   city: '',
   state: '', 
   yob: YYYY,
   yod: YYYY,
   dob: YYYY-MM-DD,
   dod: YYYY-MM-DD,
   voter_id_num: XXXXXX,
}
```

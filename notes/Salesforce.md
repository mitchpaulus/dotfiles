

Getting to setup page
Gear Icon -> Setup

Developer Console
Gear Icon -> Developer Console

Environments -> Sandboxes


```
sfdx force:source:retrieve -o commandcommissioning -m ApexClass
sfdx org display -o mpaulus@command-cx.com
sfdx force:schema:sobject:list -c all -o mpaulus@command-cx.com  # List object types
sfdx data query -o mpaulus@command-cx.com  -q 'SELECT Field FROM Project__c' # Data Query, there is no '*' in SOQL

sfdx force schema sobject describe -o mpaulus@command-cx.com -s Project__c # Schema Describe
sfdx force:schema:sobject:describe -o mpaulus@command-cx.com -s Project__c --json | jq -r '.result.fields | .[] | .name' | paste -sd, -

```

`Project__c`
`Opportunity`

```soql
SELECT Field1, Field2 FROM MyObject__c WHERE MyBooleanField__c = true
```

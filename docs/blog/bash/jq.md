# JQ Json parsing in bash

## For - loop

```shell
response=$(curl -sL "https://api.opet.com.tr/api/fuelprices/prices?ProvinceCode=34&IncludeAllProducts")
products=$(echo $response | jq '.[] | select(.districtCode == "034005") | .prices')

for row in $(echo "${products}" | jq -r '.[] | @base64') ; do
  row=$(echo "$row" | base64 --decode)
  name=$(echo $row | jq -r '.productName')
  amount=$(echo $row | jq -r '.amount')

  echo "$name == $amount"
  break
done
```

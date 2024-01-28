import json
import requests
from ref_resolver import RefResolver

### https://schemas.api.finra.org/FINRAApiPlatformU4Filing.json ###
# # grab python dict from json schema files
# json_obj = json.load(open('U4Filing.json'))
#
# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)
#
# # dict is now inlined with all $ref removed
#
# # save into a new file
# with open("U4Filing_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### https://schemas.api.finra.org/FINRAApiPlatformFilingMetadata.json ###
# # grab python dict from url
# json_obj = requests.get("https://schemas.api.finra.org/FINRAApiPlatformFilingMetadata.json").json()
#
# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)
#
# # dict is now inlined with all $ref removed
#
# # save into a new file
# with open("FINRAApiPlatformFilingMetadata_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/individualInformation.json  ###
# grab python dict from url
json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/individualInformation.json").json()

# call to API resolve method
RefResolver(json_obj['$id']).resolve(json_obj)

# dict is now inlined with all $ref removed

# save into a new file
with open("individualInformation_final.json", "w") as outfile:
    json.dump(json_obj, outfile)
import json
from ref_resolver import RefResolver

# grab python dict from json schema files
json_obj = json.load(open('U4Filing.json'))

# call to API resolve method
RefResolver(json_obj['$id']).resolve(json_obj)

# dict is now inlined with all $ref removed

# save into a new file
with open("U4Filing_final.json", "w") as outfile:
    json.dump(json_obj, outfile)


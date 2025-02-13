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

### Metadata: https://schemas.api.finra.org/FINRAApiPlatformFilingMetadata.json ###
# # grab python dict from url
# json_obj = requests.get("https://schemas.api.finra.org/FINRAApiPlatformFilingMetadata.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("FINRAApiPlatformFilingMetadata_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### individualInformation: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/individualInformation.json  ###
# grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/individualInformation.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("individualInformation_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)
    
### individualNonIndustryEmployments: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/individualNonIndustryEmployments.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/individualNonIndustryEmployments.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("individualNonIndustryEmployments_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### individualOtherBusinesses: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/individualOtherBusinesses.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/individualOtherBusinesses.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("individualOtherBusinesses_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### examsInformation: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/examsInformation.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/examsInformation.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("examsInformation_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### professionalDesignations: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/professionalDesignations.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/professionalDesignations.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("professionalDesignations_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### firmAssociations: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/firmAssociations.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/firmAssociations.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("firmAssociations_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpBond200510: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpBond200510.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpBond200510.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpBond200510_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpBond200905: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpBond200905.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpBond200905.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpBond200905_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpBankruptcy200510: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpBankruptcy200510.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpBankruptcy200510.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpBankruptcy200510_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpBankruptcy200905: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpBankruptcy200905.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpBankruptcy200905.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpBankruptcy200905_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpCivilJudicial200510: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCivilJudicial200510.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCivilJudicial200510.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpCivilJudicial200510_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpCivilJudicial200905: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCivilJudicial200905.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCivilJudicial200905.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpCivilJudicial200905_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpTermination200510: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpTermination200510.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpTermination200510.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpTermination200510_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpTermination200905: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpTermination200905.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpTermination200905.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpTermination200905_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpRegulatoryAction200510: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpRegulatoryAction200510.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpRegulatoryAction200510.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpRegulatoryAction200510_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpRegulatoryAction200905: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpRegulatoryAction200905.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpRegulatoryAction200905.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpRegulatoryAction200905_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpInvestigation200510: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpInvestigation200510.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpInvestigation200510.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpInvestigation200510_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpInvestigation200905: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpInvestigation200905.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpInvestigation200905.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpInvestigation200905_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpJudgmentLien200510: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpJudgmentLien200510.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpJudgmentLien200510.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpJudgmentLien200510_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpJudgmentLien200905A: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpJudgmentLien200905A.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpJudgmentLien200905A.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpJudgmentLien200905A_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpJudgmentLien200905B: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpJudgmentLien200905B.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpJudgmentLien200905B.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpJudgmentLien200905B_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpCriminal200510: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCriminal200510.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCriminal200510.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpCriminal200510_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpCriminal200905: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCriminal200905.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCriminal200905.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpCriminal200905_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpCustomerComplaint200510: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCustomerComplaint200510.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCustomerComplaint200510.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpCustomerComplaint200510_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### drpCustomerComplaint200905: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCustomerComplaint200905.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/drpCustomerComplaint200905.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("drpCustomerComplaint200905_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### disclosureQuestions: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/disclosureQuestions.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/disclosureQuestions.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("disclosureQuestions_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### signatures: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/signatures.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/signatures.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("signatures_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

### dualRegistration: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/dualRegistration.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/dualRegistration.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("dualRegistration_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

# ### common-data-definitions: https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/common-data-definitions.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u4/models/0.0.1/common-data-definitions.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("commonDataDefinitions_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)

# ### U5: https://ramp-schemas.datacollection.finra.org/forms/u5/models/0.0.1/u5.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/u5/models/0.0.1/u5.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("U5Filing_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)


# ### branch filing: https://ramp-schemas.datacollection.finra.org/forms/br/models/0.0.1/br.json ###
# # grab python dict from url
# json_obj = requests.get("https://ramp-schemas.datacollection.finra.org/forms/br/models/0.0.1/br.json").json()

# # call to API resolve method
# RefResolver(json_obj['$id']).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("BRFiling_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)


# ### Composite Individual: https://static.rampweb.finra.org/schemas/individualcomposite.json ###
# grab python dict from url
json_obj = requests.get("https://static.rampweb.finra.org/schemas/individualcomposite.json").json()

# call to API resolve method
RefResolver(None).resolve(json_obj)

# dict is now inlined with all $ref removed

# save into a new file
with open("Composite_Individual_final.json", "w") as outfile:
    json.dump(json_obj, outfile)

# ### Composite Branch: https://static.rampweb.finra.org/schemas/branchcomposite.json ###
# # grab python dict from url
# json_obj = requests.get("https://static.rampweb.finra.org/schemas/branchcomposite.json").json()

# # call to API resolve method
# RefResolver(None).resolve(json_obj)

# # dict is now inlined with all $ref removed

# # save into a new file
# with open("Composite_Branch_final.json", "w") as outfile:
#     json.dump(json_obj, outfile)
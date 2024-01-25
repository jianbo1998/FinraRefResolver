# original codes are from https://github.com/purukaushik/ref-resolver/blob/master/README.md

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from urllib.parse import urlparse, urljoin
import simplejson as json
from os.path import isfile
import jsonpath_rw
import requests


cache = {}

class RefResolver:

    def __init__(self):
        self.url_fragments = None

    def __init__(self, id):
        self.id = id
        if id is not None:
            self.url_fragments = urlparse(id)
        else:
            self.url_fragments = None



    def resolve(self, json_obj):
        if isinstance(json_obj, dict):
            for key, value in json_obj.items():
                if key == "$ref":
                    ref_frag = urlparse(value)
                    # print("\n")
                    # print(value)
                    ref_file = ref_frag.netloc + ref_frag.path
                    cur_json = {}
                    if ref_file in cache:
                        cur_json = cache[ref_file]
                    else:
                        # if self.url_fragments.scheme in ['http', 'https']:
                        if ref_frag.scheme in ['http', 'https']:
                            # ref_url = urljoin(self.id, ref_file)
                            ref_url = value
                            try:
                                if callable(requests.Response.json):
                                    cur_json = requests.get(ref_url).json()
                                else:
                                    cur_json = requests.get(ref_url).json
                                ref_id = None
                                if '$id' in cur_json:
                                    ref_id = cur_json['$id']
                                cache[ref_file] = cur_json
                                # print(cur_json)
                                RefResolver(ref_id).resolve(cur_json)
                                cache[ref_file] = cur_json
                            except:
                                print(value)
                                return {} 
                        # elif self.url_fragments.scheme == 'file':
                        elif ref_frag.scheme == 'file':
                            if isfile(ref_file):
                                # if the ref is another file -> go there and get it
                                cur_json = json.load(open(ref_file))
                                ref_id = None
                                if '$id' in cur_json:
                                    ref_id = cur_json['$id']
                                cache[ref_file] = cur_json
                                RefResolver(ref_id).resolve(cur_json)
                                cache[ref_file] = cur_json
                            else:
                                # if the ref is in the same file grab it from the same file
                                cur_json = json.load(open(self.url_fragments.netloc+self.url_fragments.path))
                                cache[ref_file] = cur_json
                        else: # only has fragment
                            try:
                                cur_json =  cache[self.url_fragments.netloc+self.url_fragments.path]
                            except:
                                cur_json = {}

                    # find the json section based on url fragment part. It will return all if no fragment
                    ref_path_expr = "$" + ".".join(ref_frag.fragment.split("/"))
                    path_expression = jsonpath_rw.parse(ref_path_expr)
                    list_of_values = [match.value for match in path_expression.find(cur_json)]

                    if len(list_of_values) > 0:
                        resolution = list_of_values[0]
                        # print(resolution)
                        return resolution
                    

                resolved = self.resolve(value)
                if resolved is not None:
                    json_obj[key] = resolved
        elif isinstance(json_obj, list):
            for (key, value) in enumerate(json_obj):
                resolved = self.resolve(value)
                if resolved is not None:
                    json_obj[key] = resolved
        return None
# import requests
# def get_interface_id(vm_name, netbox_headers):
#     url = (
#         "http://65.21.252.14:8000/api/virtualization/interfaces/?virtual_machine=%s"
#         % vm_name
#     )
#     result = requests.get(url, headers=netbox_headers)
#     return result.json()["results"][0]["id"]

# def what_does_the_fox_say():
#   print("vixens cry")

# get_interface_id("gns3","{\"Authorization\": \"token 93a28f69a9df5dd92223a09d3c70875801f99229\",\"Content-Type\": \"application/json\"}")

# headers = {                                                                                                                                                                                                                                                                                                                                                                                                                                   
#      'Content-Type': 'application/xml',                                                                                                                                      
# }
# import requests

# headers = {"Authorization": "token 93a28f69a9df5dd92223a09d3c70875801f99229", "Content-Type": "application/json; charset=utf-8"}
# result = requests.get("http://65.21.252.14:8000/api/virtualization/interfaces/?virtual_machine=gns3", headers=netbox_headers")



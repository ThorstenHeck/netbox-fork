# import requests
# import json
 
# url = "https://httpbin.org/post"
 
# headers = {"Content-Type": "application/json; charset=utf-8"}
 
# data = {
#     "id": 1001,
#     "name": "geek",
#     "passion": "coding",
# }
 
# response = requests.post(url, headers=headers, json=data)

# # print("Status Code", response.status_code)
# # print("JSON Response ", response.json())

# url = "http://65.21.252.14:8000/api/virtualization/interfaces/?virtual_machine=gns3"

# netbox_headers = {"Authorization": "token 93a28f69a9df5dd92223a09d3c70875801f99229", "Content-Type": "application/json; charset=utf-8"}
# result = requests.get(url, headers=netbox_headers)

# # print("Status Code", result.status_code)
# # print("JSON Response ", result.json())


# def get_interface_id(vm_name, netbox_headers):
#     url = (
#         "http://65.21.252.14:8000/api/virtualization/interfaces/?virtual_machine=%s"
#         % vm_name
#     )
#     result = requests.get(url, headers=netbox_headers)
#     return result.json()["results"]

# b = "gsn3"
# a = get_interface_id("gns3", netbox_headers)
# print("JSON Response ", a)

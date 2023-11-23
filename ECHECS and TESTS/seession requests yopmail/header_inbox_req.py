
headers =  [
			{
				"name": "Accept",
				"value": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
			},
			{
				"name": "Accept-Encoding",
				"value": "gzip, deflate, br"
			},
			{
				"name": "Accept-Language",
				"value": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3"
			},
			{
				"name": "Cache-Control",
				"value": "no-cache"
			},
			{
				"name": "Connection",
				"value": "keep-alive"
			},
			{
				"name": "Cookie",
				"value": "yc=EZmRkZmDlAQRlZmxmZQZ1ZwZ; ycons=IA6QOw7BmdSQe86FGdyiH9AXK9eU/+F7IGylRA/FLfeIU3ehvj1fdPhNNSWz1tvl; compte=bordel:jaja:patrik:jeanyohann:alicebernouilli:alicenernouilli:mihaita; ywm=bordel; yses=RbyPVrZl2WYMyhmFHVeZMeI17uMEc9oEe8d/tiB7CaFn1iAHtR3iQQzdlCJOH2yN; ytime=14:54; ygen=x_xaudeuppofracau-1746"
			},
			{
				"name": "DNT",
				"value": "1"
			},
			{
				"name": "Host",
				"value": "yopmail.com"
			},
			{
				"name": "Pragma",
				"value": "no-cache"
			},
			{
				"name": "Referer",
				"value": "https://yopmail.com/fr/wm"
			},
			{
				"name": "Sec-Fetch-Dest",
				"value": "iframe"
			},
			{
				"name": "Sec-Fetch-Mode",
				"value": "navigate"
			},
			{
				"name": "Sec-Fetch-Site",
				"value": "same-origin"
			},
			{
				"name": "Upgrade-Insecure-Requests",
				"value": "1"
			},
			{
				"name": "User-Agent",
				"value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
			}
		]
h = {}
for i in headers : 
	h[i["name"]] = i["value"]


def convert(headers : list[dict]) -> dict : 
	h = {}
	for i in headers : 
		h[i["name"]] = i["value"]
	return h



# Python Ngrok URL

## Description
This package is a utility tool to make your life easier while using Ngrok with Python. 
This package contains a simple way to get the tunnel in string format inside your script.

Get tunnel url code example:

```python
from ngrok_connection.connection.sync import SyncNgrokConnection

ngrok = SyncNgrokConnection()
ngrok.load_tunnel_data()
url = ngrok.get_tunnel_url()

print(url)
```

Output:

```
'https://your_url.ngrok.io'
```
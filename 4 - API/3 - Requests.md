# Requests

In Python, you can use the `requests` library to interact with HTTP REST methods. The `requests` library simplifies sending HTTP requests and handling responses. If you don't have it installed, you can install it using:

```bash
pip install requests
```

### 1. GET Request


```python
import requests

# Example: Fetch a list of products from a Fakestore API
url = "https://fakestoreapi.com/products"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print(data)
else:
    print(f"Error: {response.status_code}")
```

This example sends a GET request to the specified URL (`https://fakestoreapi.com/products`) and prints the JSON data if the request is successful.

### 2. POST Request

```python
import requests

# Example: Create a fake user on a Fakestore API
url = "https://fakestoreapi.com/users"
data = {"name": "John Doe", "email": "john@example.com", "username": "johnny"}
response = requests.post(url, json=data)

# Check if the request was successful (status code 201 for resource creation)
if response.status_code == 201:
    user_data = response.json()  # Parse JSON response
    print(f"User created: {user_data}")
else:
    print(f"Error: {response.status_code}")
```

This example sends a POST request to the specified URL (`https://fakestoreapi.com/users`) with JSON data to create a fake user.

### 3. PUT Request

```python
import requests

# Example: Update information for a specific product on a Fakestore API
url = "https://fakestoreapi.com/products/1"  # Replace with the actual product ID
data = {"title": "New Title", "price": 99.99}
response = requests.put(url, json=data)

# Check if the request was successful (status code 200 for successful update)
if response.status_code == 200:
    updated_product = response.json()  # Parse JSON response
    print(f"Product updated: {updated_product}")
else:
    print(f"Error: {response.status_code}")
```

This example sends a PUT request to update information for a specific product identified by its ID.

### 4. DELETE Request

```python
import requests

# Example: Delete a specific product on a Fakestore API
url = "https://fakestoreapi.com/products/1"  # Replace with the actual product ID
response = requests.delete(url)

# Check if the request was successful (status code 200 for successful deletion)
if response.status_code == 200:
    print("Product deleted successfully.")
else:
    print(f"Error: {response.status_code}")
```

This example sends a DELETE request to remove a specific product identified by its ID.


### Handling Responses:

After sending a request, you get a response object that contains information about the response from the server. Key attributes and methods for handling responses include:

- **Status Code:**

  ```python
  print(response.status_code)
  ```

  The `status_code` attribute provides the HTTP status code returned by the server. This code indicates the success or failure of the request.

- **Response Content:**

  ```python
  content = response.content  # Raw binary content
  text_content = response.text  # Text content (decoded from bytes)
  json_content = response.json()  # JSON content (if response contains JSON)
  ```

  Depending on the response content type, you can access the raw binary content, text content, or parse JSON directly from the response.

- **Headers:**

  ```python
  headers = response.headers  # Dictionary containing response headers
  ```

  The `headers` attribute provides a dictionary containing the HTTP headers sent by the server.

- **Checking for Success:**

  ```python
  if response.ok:
      print("Request was successful!")
  ```

  The `ok` attribute is `True` if the HTTP status code indicates success (2xx range).

- **Handling Errors:**

  ```python
  if response.status_code != 200:
      print(f"Error: {response.status_code}")
  ```

  You can check the status code and handle errors accordingly.


# Exercise

Write a Python script to retrieve a list of categories available on the Fakestore API.

The script should print the list of categories if the request is successful, or print an error message if the request fails.

**Hint:** The URL for retrieving categories is `https://fakestoreapi.com/docs`.

```python
import requests

url = ""
categories = []

categories = response.json()
print(f"Available Categories:\n{categories}")

```
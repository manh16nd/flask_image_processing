# Image Processing Flask Server

## Requirements

- Python 3.7

## Run the server


```
python app.py
```

Server runs on port 5000

## Usage

Go to `http://127.0.0.1:5000` on your browser and upload the image. See result below.

## API 

### Get image's grayscale value

- **URL**

```
/img
```

- **Method**

`POST`

- **Data params**

**Required**
`img=[File]`

- **Success Response**

```json
{
    "success": true,
    "data": {
        "total": "Sum of all pixel in grayscale",
        "avarage_value": "The grayscale avarage value",
        "pixel_quantity": "Quantity of pixel"
    }
}
```

- **Fail Response**
```json
{
    "success": false,
    "message": "The message"
}
```
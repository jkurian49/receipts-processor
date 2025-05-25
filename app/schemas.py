RECEIPT_SCHEMA = {
    "type": "object",
    "properties": {
        "retailer": {
            "type": "string"
        },
        "purchaseDate": {
            "type": "string",
            "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "purchaseTime": {
            "type": "string",
            "pattern": "^\\d{2}:\\d{2}$"
        },
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "shortDescription": {
                        "type": "string"
                    },
                    "price": {
                        "type": "string"
                    }
                },
                "required": ["shortDescription", "price"]
            }
        },
        "total": {
            "type": "string"
        }
    },
    "required": ["retailer", "purchaseDate", "purchaseTime", "items", "total"]
}
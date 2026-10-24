
{
  "name": "get_post",
  "description": "Retrieve a post using its ID.",
  "input": {
    "post_id": {
      "type": "integer",
      "description": "The ID of the post to retrieve.",
      "required": true
    }
  },
  "output": {
    "id": "integer",
    "title": "string",
    "body": "string",
    "userId": "integer"
  },
  "possible_errors": [
    "404",
    "429",
    "500",
    "Timeout"
  ]
}

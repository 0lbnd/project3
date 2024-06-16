# Blog API

## Endpoints

- `POST /api/posts/` - Create a new post
- `GET /api/posts/` - Retrieve all posts
- `GET /api/posts/<id>/` - Retrieve a specific post
- `PUT /api/posts/<id>/` - Update a specific post (Authenticated users only)
- `DELETE /api/posts/<id>/` - Delete a specific post (Authenticated users only)

- `POST /api/comments/` - Create a new comment
- `GET /api/comments/` - Retrieve all comments
- `GET /api/comments/<id>/` - Retrieve a specific comment
- `PUT /api/comments/<id>/` - Update a specific comment (Authenticated users only)
- `DELETE /api/comments/<id>/` - Delete a specific comment (Authenticated users only)

## Authentication

- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token

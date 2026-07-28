# GitHub User Finder

A Python console application that retrieves public GitHub user information using the GitHub REST API.

## Features

- Search for GitHub users by username
- Display name and location
- Display public repository count
- Display followers and following
- Display profile URL
- Handle users that do not exist
- Handle connection errors

## Technologies

- Python 3
- Requests
- GitHub REST API
- JSON

## How to Run

Install the dependency:

```bash
python -m pip install requests
```

Run the application:

```bash
python github_user_finder.py
```

## Example

```text
===== GITHUB USER FINDER =====

Enter GitHub username: octocat

===== GITHUB USER =====
Username: octocat
Name: The Octocat
Public repositories: 8
Followers: ...
Following: ...
Location: ...
Profile: ...
```

## What I Learned

- Making HTTP requests with Python
- Working with REST APIs
- Reading JSON responses
- HTTP status codes
- Exception handling
- Functions
- User input validation
- f-strings

## Future Improvements

- Display repositories
- Search repositories
- Save results to JSON
- Add a graphical or web interface

## Author

Julio

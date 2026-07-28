import requests


def get_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            user = response.json()

            print("\n===== GITHUB USER =====")
            print(f"Username: {user['login']}")
            print(f"Name: {user['name'] or 'Not available'}")
            print(f"Public repositories: {user['public_repos']}")
            print(f"Followers: {user['followers']}")
            print(f"Following: {user['following']}")
            print(f"Location: {user['location'] or 'Not available'}")
            print(f"Profile: {user['html_url']}")

        elif response.status_code == 404:
            print("User not found.")

        else:
            print(f"Error: HTTP {response.status_code}")

    except requests.exceptions.RequestException:
        print("Connection error. Please try again.")


def main():
    print("===== GITHUB USER FINDER =====")

    while True:
        username = input("\nEnter GitHub username (or 'exit' to quit): ").strip()

        if username.lower() == "exit":
            print("Goodbye!")
            break

        if not username:
            print("Username cannot be empty.")
            continue

        get_user(username)


if __name__ == "__main__":
    main()

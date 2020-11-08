import time
import requests
import webbrowser
from openpyxl import load_workbook
from InstagramAPI import InstagramAPI


book = load_workbook('path-to-block-with-list-of-usernames-only-in-each-row.xlsx')
sheet = book['Sheet1']

def instagram_unfollow():
    try:
        api = InstagramAPI('your-insta-username', 'your-insta-password')
        res = api.login()

        for rowdd in sheet.rows:
            username = rowdd[0].value
            print(username)
            # Unblock function works on user_id, so first lets get the userid
            res = requests.get("https://www.instagram.com/"+username+"/?__a=1")
            user_id = res.json()['graphql']['user']['id']
            print(f"User ID : ",user_id)

            # Block the userid
            api.block(user_id)
            print(f"BLOCKED SUCCESSFULLY {user_id}")

            # Let's wait few secs to avoid any spam or any automation'
            time.sleep(4)

            print("--------------------")

            # To verify : Test Code
            # Check the instagram accounts
            # new = 2 # open in a new tab, if possible

            # open a public URL, in this case, the webbrowser docs
            # url = "https://www.instagram.com/"+rowdd[0].value+"/"
            # webbrowser.get(using='google-chrome').open(url,new=new)

        print("Yay!... Done!")
    except Exception as e:
        print(e)


def main():
    print("[+] Starting Script [+]")
    instagram_unfollow()

if __name__ == "__main__":
    main()

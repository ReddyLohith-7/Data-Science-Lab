
# ==========================================================
# DATA SCIENCE - PROGRAM 8
# TOPIC: WEB SCRAPING USING BEAUTIFUL SOUP
# Roll no : 23102A010287
# Name    : B.Reddy Lohith
# Section : B4
# ==========================================================

import requests
from bs4 import BeautifulSoup

# Define request headers
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Define the target URL
url = "https://www.amazon.in/product-reviews/B09G9BL5CP/"

# Send HTTP GET request
try:
    response = requests.get(url, headers=headers, timeout=20)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Find review sections
        reviews = soup.find_all(
            "span",
            {"data-hook": "review-body"}
        )

        print("Number of Reviews Found:", len(reviews))

        for review in reviews[:5]:
            print("\nReview:")
            print(review.get_text(strip=True))

        if len(reviews) == 0:
            print("No reviews found. The website may have changed its page structure.")

    else:
        print("Unable to retrieve reviews from the website.")

except requests.RequestException as error:
    print("Request failed:", error)

print("\nProgram Completed")

import requests
from bs4 import BeautifulSoup
def scrape_books():

    url = "http://books.toscrape.com/"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book items (each is contained in an <article> tag with class "product_pod")
    books = soup.find_all("article", class_="product_pod")

    # Create a list to store the extracted book data
    book_data = []

    # Loop through each book and extract details
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()
        # Append the data as a dictionary to the list
        book_data.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })

    return book_data

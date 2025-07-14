# array = [2,4,5,7,8,6]
# x = 6
# n = len(array)
#
# def linearsearch(array, n, x):
#
#     for i in range(0,n):
#
#         if array[i] == x:
#             return i
#         return -1
#
# result = linearsearch(array,n,x)
#
# if result == -1:
#     print("Element is not found in the array")
# else:
#     print(f'Element found at Index : {result}')

#linear search problems
#1.Searching for a username in a list

users = ["alice", "bob", "charlie", "david"]
search_name = "charlie"

for i in range(len(users)):
    if users[i] == search_name:
        print(f"{search_name} found at index {i}")
        break
else:
    print(f"{search_name} not found")

#2.Verifying UI Labels in a list
expected_labels = ["Home", "About", "Services", "Contact"]
ui_labels = ["Home", "Blog", "Services", "Contact"]

missing = []
for label in expected_labels:
    if label not in ui_labels:
        missing.append(label)

print("Missing labels:", missing)

#3.Find the first broken link from a list
links = ["https://valid.com", "https://invalid.com", "https://another.com"]

def is_broken(link):
    # Dummy condition for demo
    return "invalid" in link

for link in links:
    if is_broken(link):
        print(f"Broken link found: {link}")
        break

#4.Check the duplicate entries in a form submission
emails_entered = ["test1@example.com", "test2@example.com", "test1@example.com"]
seen = []

for email in emails_entered:
    if email in seen:
        print(f"Duplicate found: {email}")
        break
    seen.append(email)

#5.Search for a product in a list
products = ["T-Shirt", "Jeans", "Shoes", "Watch"]
search_product = "Shoes"

for i in range(len(products)):
    if products[i] == search_product:
        print(f"{search_product} is available at position {i}")
        break
else:
    print(f"{search_product} is not in stock")

#6.Find a button or element text in Selenium web automation
buttons = driver.find_elements(By.TAG_NAME, "button")
target_text = "Submit"

found = False
for btn in buttons:
    if btn.text == target_text:
        btn.click()
        found = True
        break

if not found:
    print("Submit button not found!")


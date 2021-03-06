import csv

products = []

products_csv = "data/products.csv"
headers = ["id", "name", "aisle", "department", "price"]
user_input_headers = [header for header in headers if header != "id"]

def get_product_id(product): return int(product["id"])

def Provide_ID():
    product_id = input("Please provide the product ID:")
    return product_id

def additonal_id():
    product_ids = map(get_product_id, products)
    return max(product_ids) + 1

with open(products_csv, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for ordered_dict in reader:
        products.append(dict(ordered_dict))

def list_products():
    print("Here are the products")
    for product in products:
        print(" + Product " + str(product["id"]) + ": " + product["name"])

def show_product():
    product_id = Provide_ID()
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("Reading product here", product)
    else:
        print("No product could be found with ID")

def create_product():
    print("Please provide the product information.")
    product = {"id": additonal_id() }
    for header in user_input_headers:
        product[header] = input("The '{0}' is: ".format(header))
    products.append(product)
    print("Creating product here", product)

def update_product():
    product_id = Provide_ID()
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("Please provide the products information")
        for header in user_input_headers:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("Updating product here", product)
    else:
        print("Product could not be found with ID", product_id)
#Source: Professor Rossetti
def destroy_product():
    product_id = Provide_ID()
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("Destroying product", product)
        del products[products.index(product)]
    else:
        print("Product could not be found with ID", product_id)

menu = """
---------------------------------------
PRODUCTS APPLICATION
---------------------------------------

Welcome to the Grocery Store Database!

There are {1} products in the database.

Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

Please select an operation: """.format("@mswan", len(products))

chosen_operation = input(menu)

if chosen_operation.title() == "List": list_products()
elif chosen_operation.title() == "Show": show_product()
elif chosen_operation.title() == "Create": create_product()
elif chosen_operation.title() == "Update": update_product()
elif chosen_operation.title() == "Destroy": destroy_product()
else: print("Operation does not exist.")


with open(products_csv, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()

    for product in products:
        writer.writerow(product)

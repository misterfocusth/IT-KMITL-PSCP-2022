"""iPhone 13 Again"""


def get_price_by_storage_opt(model, storage):
    """Check additional price for selected model and storage option"""
    if storage == "128 GB":
        return 0
    elif storage == "256 GB":
        return 4000
    elif storage == "512 GB":
        return 12000
    elif storage == "1 TB":
        if model == "iPhone 13 mini" or model == "iPhone 13":
            return -1
        else:
            return 20000
    else:
        return -1


def main():
    """Main Function"""
    model = input()
    storage = input()
    storage_price = get_price_by_storage_opt(model, storage)

    if storage_price == -1:
        print("Not Available")
    else:
        if model == "iPhone 13 mini":
            print(25900 + storage_price)
        elif model == "iPhone 13":
            print(29900 + storage_price)
        elif model == "iPhone 13 Pro":
            print(38900 + storage_price)
        elif model == "iPhone 13 Pro Max":
            print(42900 + storage_price)
        else:
            print("Not Available")


main()

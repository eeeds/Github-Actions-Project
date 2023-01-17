from datetime import datetime


def write_on_text(path="dates.txt", data=None):
    """
    Function to write on a text file.
    Args:
        path (str): Path to the file.
        data (str): Data to write on the file.
    Returns:
        None
    """
    with open(path, "a") as file:
        file.write(data)


def main():
    """
    Main function using in this script.
    Args:
        None
    Returns:
        None
    """
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    write_on_text(data=fecha)


if __name__ == "__main__":
    main()

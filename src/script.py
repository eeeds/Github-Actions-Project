from datetime import datetime 

def write_on_text(path = 'dates.txt', data=None):
    with open(path, 'a') as file:
        file.write(data)


def main():
    fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    write_on_text(data = fecha)
    

if __name__ == '__main__':
    main()
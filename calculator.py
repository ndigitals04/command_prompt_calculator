
def readInput(result, record):
    number = ""
    if result == "":
        print("\n")
        while number != "close":
            input_error = False
            number = input("Input number: ")
            if number == "close":
                return "close"
            if number == "clear":
                return ("clear", result)
            if number == "record":
                return "record"
            try:
                number = float(number)
                 
            except(ValueError):
                print("Only numbers should be specified here")
                print(number, type(number), " why")
                input_error = True
            if input_error == False:
                break
                print("Reached input error statment")
        # print(number)
        return number
    else:
        print(result)
        operator = ""
        while operator != "close":
            operator = input("Input operator: ")
            if operator == "close":
                return "close"
            if operator == "clear":
                return ("clear", result)
            if operator == "record":
                return "record"
            if operator == "+":
                break
            elif operator == "-":
                break
            elif operator == "/":
                break
            elif operator == "*":
                break
            elif operator == "=":
                print("= ",result)
                context = {
                    "result": result,
                    "operator": "="
                }
                return context
            else:
                print("Please input one of the four opearators '+,-,/,*' ")
        
        while number != "close":
            input_error = False
            number = input("Input number: ")
            if number == "clear":
                return "clear"
            if number == "close":
                return "close"
            if number == "record":
                return "record"
            try:
                number = float(number)
                
            except(ValueError):
                print("Only numbers should be specified here")
                input_error = True
                # print(input_error)
            if input_error == False:
                break
        if number == "close":
                return "close"
        
        context = {
            "result": result,
            "operator": operator,
            "number": number
        }

        if int(number) == float(number):
            number = int(number)
        print(str(result) + operator+ str(number))
        return(context)

def additionOperation(result,number):
    result += number
    return result

def subtractionOperation(result,number):
    result -= number
    return result

def divisionOperation(result,number):
    result /= number
    return result

def multiplicationOperation(result,number):
    result *= number
    return result


def runCalculator():
    result = ""
    record = []
    print("Follow the prompts of the calculator for use \nType 'clear' to close a calculation and start another\nType 'close' to close the calculator")
    print("Type 'record' to see all your calculation results")
    print("NB: Calculation results are stored after typing the '=' operator")
    while result != "close":
        data = readInput(result, record)
        if data == "close":
            break
        elif data == "record":
            for calculation in record:
                print (calculation)
            print("\n")
        elif type(data) == tuple:
            result = ""
        elif type(data) == float or type(data) == int:
            result = data
            new_record = str(data)
        elif type(data) == dict:
            if data["operator"] == "+":
                result = additionOperation(data["result"], data["number"])
                new_record += "+" + str(data["number"])
            elif data["operator"] == "-":
                result = subtractionOperation(data["result"], data["number"])
                new_record += "-" + str(data["number"])
            elif data["operator"] == "/":
                result = divisionOperation(data["result"],  data["number"])
                new_record += "/" +str(data["number"])
            elif data["operator"] == "*":
                result = multiplicationOperation(data["result"], data["number"])
                new_record += "*" + str(data["number"])
            elif data["operator"] == "=":
                new_record = new_record + "= " + str(data["result"])
                record.append(new_record)
                new_record = str(data["result"])
    print("Session ended, Bye")
        
runCalculator()


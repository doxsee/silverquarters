## Calculate the value of a given number of silver quarters.

import urllib.request

address = "https://www.kitco.com/"
response = urllib.request.urlopen(address)

theBytes = response.read()
response.close()

text = theBytes.decode()

i = text.find("AG-bid")

agBid = float(text[i + 8 : i + 13])

def main() :
    option = input("Are you (B) buying or (S) selling silver quarters?: ")
    if option.upper() == "B" :
        result = buy(float(input("Enter amount in $: ")))
        print("\n$%d dollars will buy %d quarters with $%.2f left over." % (result[0], result[1], result[2]))
    elif option.upper() == "S" :
        result = sell(int(input("How many quarters are you selling?: ")))
        print("\n%d quarters will sell for $%.2f" % (result[0],result[1]))
    elif option.upper() == "Q" :
        return
    else :
        main()
    return
def buy(cost) :
    dollarsPerQuarter = agBid * .1808
    leftOver = cost % dollarsPerQuarter
    numberOfQuarters = cost // dollarsPerQuarter
    return cost, numberOfQuarters, leftOver
def sell(quantity) :
    value = quantity * .1808 * agBid
    return quantity, value
main()
    
    
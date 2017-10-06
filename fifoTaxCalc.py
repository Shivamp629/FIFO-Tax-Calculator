def calculateTax(trades):
    amountOwed = 0
    numberBought = 0
    sellingPrice = 0
    for transcation in range(len(trades)):
        if (type(trades[transcation]) == str):
            individualTransaction = trades[transcation].split(",")
            #Buying
            if (individualTransaction[2] == "B"):
                if (numberBought < 0):
                    if ((numberBought + int(individualTransaction[3])) < 0):
                        profit = ((sellingPrice - float(individualTransaction[4])) * int(individualTransaction[3]))
                        amountOwed += profit
                    else:
                        profit = ((sellingPrice - float(individualTransaction[4])) * abs(numberBought))
                        amountOwed += profit
                numberBought += int(individualTransaction[3])

            #Selling
            else:
                profit = 0
                sellingNum = int(individualTransaction[3])
                if  (sellingNum > 0):
                    #FIFO Selling
                      rangeTrades = range(len(trades))
                      individualtranscationInner = 0
                      while(sellingNum > 0 and individualtranscationInner < transcation):

                        transcationInner = trades[individualtranscationInner].split(",")

                        if (transcationInner[2] == "B" and int(transcationInner[3]) > 0):
                            #taking all shares from a date
                            if (sellingNum >= int(transcationInner[3])):
                                #print((individualTransaction[4]) + "     "+ transcationInner[4] + "   " + transcationInner[3])
                                profit += ((float(individualTransaction[4]) - float(transcationInner[4])) * int(transcationInner[3]))
                                sellingNum -= int(transcationInner[3])
                                numberBought -= int(transcationInner[3])
                                transcationInner[3] = "0"
                            #taking only needed amount of shares from a date
                            else:
                                #print((individualTransaction[4]) + "     "+ transcationInner[4] + "   " + str(sellingNum))
                                profit += ((float(individualTransaction[4]) - float(transcationInner[4])) * sellingNum)
                                numberBought -= sellingNum
                                transcationInner[3] = str(int(transcationInner[3]) - sellingNum)
                                sellingNum = 0

                            trades[individualtranscationInner] = ",".join(transcationInner)
                        individualtranscationInner += 1
                print("profit is " + str(profit))
                #If there is a negative balance worth of stocks
                amountOwed += profit
                sellingPrice = (float(individualTransaction[4]))
                numberBought -= sellingNum
                trades[transcation] = ",".join(individualTransaction)
    print(amountOwed)
    return "$" + str(round(amountOwed, 2))








trade = ["2015-01-03,AAPL,B,50,80.0",
"2015-01-05,AAPL,B,60,100.0",
"2015-02-05,AAPL,S,70,130.0",
"2015-02-08,AAPL,S,10,90.0",
"2015-03-10,AAPL,S,80,120.0",
"2015-03-12,AAPL,B,10,70.0",
"2015-04-08,AAPL,B,70,160.0"]
calculateTax(trade)

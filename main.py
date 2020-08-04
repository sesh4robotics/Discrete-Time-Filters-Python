from filters import Discrete_Low_Pass_Filter


if __name__ == "__main__":

    filter =  Discrete_Low_Pass_Filter(2, 1)
    params = [1, 20, 3, 40, 5, 6, 70, 8, 9, 10]

    for i in range (len(params)):
        print(filter.Order_1_LP_Filter(params[i]))


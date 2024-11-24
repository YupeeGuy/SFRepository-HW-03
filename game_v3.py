import numpy as np

#function of predict 
def game_v3(number: int = 1) -> int:
    """The game 'Predict number'
       Predicting random number in no more than 20 attempts

    Args:
        number (int, optional): The hidden number. Defaults to 1.

    Returns:
        int: count of attempts
    """
    
    count = 0 #count of attempts
    low = 0 #min border of predict's list
    high = 101 #max border of predict's list
    np.random.seed(1) #freeze seed
    predict = (high + low) // 2 #start point of prediciction
    
    #cycle prediction
    while number != predict:
        count += 1        
        if number > predict:
            low = predict
        elif number < predict:
            high = predict
            
        predict = (high + low) // 2 
    
    return count

#function check predictions
def score(predict) -> int:
    """Middle count attemps on 1000 numbers

    Args:
        predict (int): Predict function

    Returns:
        int: Count of attemps
    """
    
    count_list = [] #list of count attempts
    predict_list = np.random.randint(1, 101, size = 1000) #array predict numbers
    
    #cycle numbers in predict list and return list with counts attemps
    for num in predict_list:
        count_list.append(game_v3(num))
        
    result = int(np.mean(count_list)) #middle count attempts
    print (f'Все числа угаданы! Среднее количество попыток: {result}') #output result
    return result

score(game_v3)
    
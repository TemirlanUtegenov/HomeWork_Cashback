def calculate_cashback(summ, type_of_operation):
    """
      >>> calculate_cashback(1000, 'original')
      10.0
      >>> calculate_cashback(1000, 'high')
      50.0
      >>> calculate_cashback(1000, 'vip')
      300.0
      >>> calculate_cashback(100000, 'vip')
      3000.0

      :return:
    """
    cashback = 0.

    if type_of_operation == 'vip':
        cashback = summ * 0.3
    elif type_of_operation == 'high':
        cashback = summ * 0.05
    else:
        cashback = summ * 0.01

    if cashback > 3000:
        cashback = 3000.

    return cashback


print('original purchase =', calculate_cashback(1000, 'original'))
print('vip =', calculate_cashback(1000, 'vip'))
print('hight =', calculate_cashback(1000, 'high'))
print('>100000 =', calculate_cashback(100000, 'vip'))

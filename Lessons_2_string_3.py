S = 'Spam'
print(S)
print(S.find('pa'))                #пошук підстроки 'pa' в S і вивід на екран кількості знайдених елементів

print(S.replace('pa', 'XYZ'))      #заміна підстроки 'ра' на 'XYZ' і вивід на екран

N = 'spam'
print(N)
print(N.upper())                   #перетворює в верхній і нижній регістр SPAM
print(N.isalpha())                 #перевіряє вміст: isalpha, isdigit і т.д.

line = 'aaa,bbb,ccccc,dd\n'        #\n додає пробіл
print(line)
print(line.split(','))             #розбиття по розділювачу в список підстрок
print(line.rstrip())               #видалення пробілів з правої сторони
print(line.rstrip().split(','))    #комбінація з двох операцій

print('%s, eggs, and %s' %('spam', 'SPAM!'))        #вираз форматування
print('{}, eggs, and {}'.format('spam', 'SPAM!'))
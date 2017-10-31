import pandas as pd
from restaurantmanagementsystem.models import Food

fooddata=pd.read_excel('WokThisWay.xlsx')
for i in range(fooddata.shape[0]):
	row=fooddata.iloc[i]
	Food.objects.create(ID=row['items_id'],name=row['items_name'],description=row['items_description'],price=row['items__baseprice'],course=row['Course'],cuisine=row['Cuisine'],category=row['Category'])
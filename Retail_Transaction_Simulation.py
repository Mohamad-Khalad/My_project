
import pandas as pd
import time 
import random 
import os

header=['transaction_id','timestamp','product_id','quantity','price','customer_id']
file_name = 'retail_transactions.csv'


if not os.path.exists(file_name):
    pd.DataFrame(columns=header).to_csv(file_name,index=False)
    trans_id = 1 # I made that the transaction_id start with 1 and it increases with each transaction
else:
    df_exist=pd.read_csv(file_name)
    trans_id = df_exist['transaction_id'].max()+1


def transaction_generate() -> dict:
    
    global trans_id
    transaction={
        'transaction_id': trans_id,
        'timestamp':pd.Timestamp.now(),
        'product_id':random.randint(100,1000),
        'qunatity':random.randint(1,5),
        'price':round(random.uniform(5,100),2),
        'customer_id':random.randint(100,1000)
    }
    trans_id+=1
    return transaction 

try:
    while True:
        retail_transaction=transaction_generate()
        df=pd.DataFrame([retail_transaction])
        df.to_csv(file_name,mode='a',header=False,index=False)
        time.sleep(60)
except KeyboardInterrupt:
    print('Retail transactions generated successfully')
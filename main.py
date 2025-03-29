from fastapi import FastAPI
from pydantic import BaseModel

class users_object(BaseModel):
    name:str
    password:str
class sender_message(BaseModel):
    to : str
    frome : str
    message : str
app = FastAPI()




try :
    with open("howUsersIhave.txt" , 'r') as f :
        numbers_of_id = int(f.read())
except :
    with open("howUsersIhave.txt" , 'w') as f :
        f.write("0")
try :
    with open("all_users_id.txt" , "r") as f :
        f.read()
except :
    with open("all_users_id.txt" , "w") as f :
        f.write()
try :
    with open("all_users_name.txt" , "r") as f :
        f.read()
except :
    with open("all_users_name.txt" , "w") as f :
        f.write()
try :
    with open("all_users_password.txt" , "r") as f :
        f.read()
except : 
    with open("all_users_password.txt" , "w") as f :
        f.write()


@app.post('/')
async def _to_connect():
    return {"hello":"world"}


@app.get('/login_connect')
async def want_to_connect(name,password):
    with open("all_users_name.txt" , 'r') as f :
        # all_name = f.read()
        all_names = f.readlines()
    with open("all_users_password.txt" , 'r') as f :
        all_passwords = f.readlines()
    with open("all_users_id.txt" , 'r') as f :
        # all_id = f.read()
        all_ids = f.readlines()
    
    with open("all_users_name.txt" , 'r') as f :
        all_name = f.read()
    with open("all_users_id.txt" , 'r') as f :
        all_id = f.read()

    for i in range(len(all_names)):
        print(all_names[i][:-1],",",all_passwords[i][:-1])
        if all_names[i][:-1] == str(name) and all_passwords[i][:-1] == str(password) :
            return {"status": "1","id":f"{all_ids[i]}" , "users" : all_name , "ids" : all_id}
    return {"status" : "0"}




@app.post('/login_creat')
async def want_to_creat(rece:users_object):
    global numbers_of_id
    name = rece.name
    password = rece.password
    print(name,password)
    with open("all_users_name.txt" , 'r') as f :
        all_names = f.readlines()
    for i in all_names :
        if i == name+'\n' :
            return {"status" : "0" , "id" : ""}
        
    numbers_of_id+=1
    with open("howUsersIhave.txt" , 'w') as f :
        f.write(str(numbers_of_id))

    with open("all_users_id.txt" , 'a') as f :
        f.write(str(numbers_of_id)+'\n')
    
    with open("all_users_name.txt" , 'a') as f :
        f.write(name+'\n')

    with open("all_users_password.txt" , 'a') as f :
        f.write(password+'\n')

    # red page
    with open("all_users_name.txt" , 'r') as f :
        names = f.read()
    with open("all_users_id.txt" , 'r') as f :
        ids = f.read()
    print(names,ids)
    return {"status" : "1" , "id" : f"{numbers_of_id}", "names" : names , "ids" : ids}




@app.post("/send_message")
async def receve_message(what:sender_message):
    to,frome,message = what.to,what.frome,what.message
    with open(f"wait_message/{to}wait.txt" , "a") as f :
        f.write(f"{message}\n")
    with open(f"wait_message/{to}id.txt" , "a") as f :
        f.write(f"{frome}\n")
    return {"status": "1"}


@app.get("/radio_message")
async def repeat_on(id):
    try:
        print(id,"kk")
        with open(f"wait_message/{id}wait.txt","r") as f :
            data_mes = f.read()
        with open(f"wait_message/{id}id.txt","r") as f :
            data_ids = f.read()
        print(data_mes,data_ids,"ee")
        if len(data_mes)<1 :
            return {"status":"no"}
        else :
            with open(f"wait_message/{id}wait.txt","w") as f :
                f.write("")
            with open(f"wait_message/{id}id.txt","w") as f :
                f.write("")
            return {"status" : "yes" , "messages" : data_mes , "ids" : data_ids}
    except :
        print("nooooooooooooooooooo")
        return {"status":"no"}


@app.get("/radio_server")
async def flo():
    with open("all_users_name.txt" , 'r') as f :
        names = f.read()
    with open("all_users_id.txt" , 'r') as f :
        ids = f.read()
    return {"names":names , "ids" : ids}




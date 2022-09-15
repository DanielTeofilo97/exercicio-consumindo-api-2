import requests,json

def getCep(cep):
  try:
     res = requests.get("https://viacep.com.br/ws/"+str(cep)+"/json/")
     if res.status_code==200:
       obj = json.loads(res.text)
       try:
          err = obj["erro"]
          return True,"CEP Inválido"
       except Exception as e:
           return False,[obj["logradouro"],obj["bairro"],obj["localidade"],obj["uf"],obj["cep"]]
     else:
       return True,res.status_code 
  except Exception as e:
     return True,e

cep = int(input("Digite o seu cep : "))

err,ret=getCep(cep)
if err:
  print(f"Erro : {ret}")
else:
  print(f"Endereço: {ret[0]} , Bairro : {ret[1]} , Cidade : {ret[2]} , UF : {ret[3]} , Cep : {ret[4]}")  
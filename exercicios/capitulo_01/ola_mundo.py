import time
# Get the current time as a time tuple
current_time = time.localtime()

# Format the time using strftime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)


print("Current Formatted  Time:", formatted_time)
print("Olá, mundo!") # imprime a frase "Olá, mundo!"
time.sleep(2)
print("Agora sou uma pessoa programadora Python.")
print("Aguarde 4.5 segundos")
time.sleep(4.5)
print("Última linha do programa.")
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print("Current Formatted  Time:", formatted_time)
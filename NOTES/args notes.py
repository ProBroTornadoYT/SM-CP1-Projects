

def hello(*args):
    for name in args:
        print(f"Hello {name}!")


hello("Alex","Katie","katie2")
hello("Kris")



def clean(type, data):
    if type == "str":
        return data.strip().lower()
    elif type == "int":
        return (data)
    elif type == "float":
        return round(float(data),2)
    elif type == "list":
        return str(f"{x}, "for x in data)
    elif type == "bool":
        return f"{data}"

print(clean(type="float", data="3.14152639"))
print(clean(data="utah", type="str")) 



def clean(**kwargs):
    if kwargs["type"] == "str":
        return kwargs["data"].strip().lower()
    elif kwargs["type"] == "int":
        return int(kwargs["data"])
    elif kwargs["type"] == "float":
        return round(float(kwargs["data"]),2)
    elif kwargs["type"] == "list":
        return str(f"{x}, "for x in kwargs["data"])
    elif kwargs["type"] == "bool":
        return f"{kwargs["data"]}"

print(clean(type="float", data="3.14152639", decimals=3))
print(clean(data="utah", type="str")) 



def clean(**kwargs):
    if kwargs("type") == "str":
        return kwargs["data"].strip().lower()
    elif kwargs("type") == "int":
        return int(kwargs["data"])
    elif kwargs("type") == "float":
        return round(float(kwargs["data"]),2)
    elif kwargs("type") == "list":
        return str(f"{x}, "for x in kwargs["data"])
    elif kwargs("type") == "bool":
        return f"{kwargs["data"]}"

print(clean(type="float", data="3.14152639", decimals=3))
print(clean(data="utah", type="str")) 



def clean(**kwargs):
    if not kwargs.get("data"):
        return "No data provided"
    if kwargs.get("type") == "str":
        return kwargs.get("data").strip().lower()
    elif kwargs.get("type") == "int":
        return int(kwargs.get("data"))
    elif kwargs.get("type") == "float":
        return round(float(kwargs.get("data")),2)
    elif kwargs.get("type") == "list":
        return str(f"{x}, "for x in kwargs.get("data"))
    elif kwargs.get("type") == "bool":
        return f"{kwargs.get("data")}"

print(clean(type="float", data="3.14152639", decimals=3))
print(clean(data="utah", type="str")) 



def clean(decimals= 0,**kwargs):
    if not kwargs.get("data"):
        return "No data provided"
    if kwargs.get("type") == "str":
        return kwargs.get("data").strip().lower()
    elif kwargs.get("type") == "int":
        return int(kwargs.get("data"))
    elif kwargs.get("type") == "float":
        return round(float(kwargs.get("data")),2)
        if kwargs.get("decimals"):
            decimals = kwargs.get("decimals")
    elif kwargs.get("type") == "list":
        return str(f"{x}, "for x in kwargs.get("data"))
    elif kwargs.get("type") == "bool":
        return f"{kwargs.get("data")}"

print(clean(type="float", data="3.14152639", decimals=3))
print(clean(data="utah", type="str")) 
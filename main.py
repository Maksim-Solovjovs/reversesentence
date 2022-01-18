teksts = input("ievadiet skaitli: ")
def reverseSentence(teksts):
  sar1 = teksts.split(";")
  if len(sar1)>1:
    sar1.reverse()
    teksts = ""
    for elements in sar1:
      teksts += elements + ";"
    print(teksts)
  else:
    teksts = "parak iss teikums"
    print(teksts)
  return teksts
reverseSentence(teksts)
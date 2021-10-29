def age_assignment(*args, **kwargs):
  #  return {el: kwargs[el[0]] for el in args}      tova ili ostanalite redove nadolu
    result = {}
    for el in args:
        result[el] = kwargs[el[0]]
    return result



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


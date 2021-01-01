

class dict_objecter:
  def __init__(self, dict_):
    """
    this class converts any dictionary into an instance, nesteds are supported.
    '_' will be added on the start of any key starts with digit
    any spaces will be replaced by '_' also
    """
    for key in dict_:
      if str(key)[0].isdigit():
        key_ = '_' + str(key)
      else:
        key_ = str(key)
      key_ = key_.replace(' ', '_')
      if isinstance(dict_[key], dict):
        setattr(self, key_, dict_objecter(dict_[key]))
      else:
        setattr(self, key_, dict_[key])


# This is the target dictionary, as you see it has a 2 times nested
infos = {
  'infos_date': '2001/01/01',
  'author': 'Mohamed El-Hasnaouy',
  'nested dict': {
    0: 'this is 0',
    1: 'this is 1',
    2: 'this is 2'
  },
  'users': {
    0: {
      'name': 'Mohamed',
      'age': 21,
    },
    1: {
      'name': 'A name',
      'age': 12
    }
  }
}


# Creating the object
ob = dict_objecter(infos)

# Printing out its attributes
print('attributes of ob:')
for f in dir(ob):
  if not str(f).startswith('__'):
    print('   ', f)

print('\n' * 2)

print(ob.author)
print(ob.nested_dict._2)
print(ob.users._0.age)

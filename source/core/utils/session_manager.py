from newsletter.utils import hash

class SessionManager():

  def __init__(self, request):
    self.request = request

  def __str__(self):
    return f'SessionManager({self.request})'
  
  def __repr__(self):
    return f'SessionManager({self.request})'
  
  def __len__(self):
    return len(self.request.session)

  def _secure_session(self, key, *sub_keys):
    self.request.session.set_expiry(24 * 60 * 60 * 365) # 1 year
    self.request.session.setdefault(key[0], key[1]())
    for sub_key in sub_keys:
      _sub_key, _type = sub_key[0], sub_key[1]
      self.request.session[_sub_key] = _type()

  def get(self, key):
    hashed_key: str = hash.create_hash(key)
    return self.request.session.get(hashed_key)
  
  def set(self, key, value):
    hashed_key: str = hash.create_hash(key)
    self._secure_session([hashed_key, type(value)])
    self.request.session[hashed_key] = value

  def remove(self, key, value):
    hashed_key: str = hash.create_hash(key)
    self._secure_session([hashed_key, list])
    self.request.session[hashed_key].remove(value)

  def append(self, key, value):
    hashed_key: str = hash.create_hash(key)
    self._secure_session([hashed_key, list])
    self.request.session[hashed_key].append(value)

  def has(self, key, value):
    hashed_key: str = hash.create_hash(key)
    return value in self.request.session.get(hashed_key, [])
  
  def has_key(self, key):
    hashed_key: str = hash.create_hash(key)
    return hashed_key in self.request.session
  
  def has_sub_key(self, key, sub_key):
    hashed_key, hashed_sub_key = hash.create_hash(key), hash.create_hash(sub_key)
    return self.has_key(key) and hashed_sub_key in self.request.session[hashed_key] 

  def delete(self, key, sub_key):
    hashed_key, hashed_sub_key = hash.create_hash(key), hash.create_hash(sub_key)
    self._secure_session([hashed_key, dict], [hashed_sub_key, str])

    del self.request.session[hashed_key][hashed_sub_key]

  def set_map_value(self, key, sub_key, value):
      hashed_key, hashed_sub_key = hash.create_hash(key), hash.create_hash(sub_key)
      self._secure_session([hashed_key, dict], [hashed_sub_key, str])
      
      self.request.session[hashed_key][hashed_sub_key] = value 
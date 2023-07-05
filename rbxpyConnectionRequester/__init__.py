from rbxpy.rbxpyConnectionRequester.initResource import *

import requests

class _Requester:
  def __init__(self, *args, **kwargs) -> None:
    self.id_url = "https://users.roblox.com/v1/users/"
    self.name_url = "https://users.roblox.com/v1/usernames/users"
    self.group_url = "https://groups.roblox.com/v2/groups?groupIds="
    self.groupgames_url = "https://games.roblox.com/v2/groups/ID_HERE/games?accessFilter=1&limit=10&sortOrder=Asc"
    self.usergames_url = "https://games.roblox.com/v2/users/ID_HERE/games?accessFilter=2&limit=10&sortOrder=Asc"
    self.userfriends_url = "https://friends.roblox.com/v1/users/ID_HERE/friends"

  def _info_by_id(self, _, *args, **kwargs) -> object:
    _response = requests.get(f"{self.id_url}{_}")
    if _response.status_code == 200:
      _user_data = _response.json()
      return _user_data
    else:
      _E_STATUS = _response.status_code
      _E_RETURN = E_RETURN
      _E_MSG = f"{E_MSG}Status Code: {_E_STATUS}"
      _E_ERROR = True
      return _E_STATUS, _E_RETURN, _E_MSG, _E_ERROR

  def info_by_id(self, id, *args, **kwargs) -> object:
    try:
      return self._info_by_id(id)
    except Exception as e:
      return e

  def _info_by_name(self, _, *args, **kwargs) -> object:
    _headers = {
        "Content-Type": "application/json"
    }
    _payload = {
        "usernames": [
            _
        ],
        "excludeBannedUsers": True
    }
    _response = requests.post(self.name_url, json=_payload, headers=_headers)
    if _response.status_code == 200:
      _user_data = _response.json()
      _id = _user_data["data"][0]["id"]
      return self._info_by_id(_id)
    else:
      _E_STATUS = _response.status_code
      _E_RETURN = E_RETURN
      _E_MSG = f"{E_MSG}Status Code: {_E_STATUS}"
      _E_ERROR = True
      return _E_STATUS, _E_RETURN, _E_MSG, _E_ERROR

  def info_by_name(self, name, *args, **kwargs) -> object:
    try:
      return self._info_by_name(name)
    except Exception as e:
      return e

  def _group_by_id(self, _, *args, **kwargs) -> object:
    _response = requests.get(f"{self.group_url}{_}")
    if _response.status_code == 200:
      _group_data = _response.json()
      return _group_data
    else:
      _E_STATUS = _response.status_code
      _E_RETURN = E_RETURN
      _E_MSG = f"{E_MSG}Status Code: {_E_STATUS}"
      _E_ERROR = True
      return _E_STATUS, _E_RETURN, _E_MSG, _E_ERROR

  def group_by_id(self, id, *args, **kwargs) -> object:
    try:
      return self._group_by_id(id)
    except Exception as e:
      return e

  def _group_games(self, _, *args, **kwargs) -> object:
    _response = requests.get(f"{self.groupgames_url.replace('ID_HERE', str(_))}")
    if _response.status_code == 200:
      _group_data = _response.json()
      return _group_data
    else:
      _E_STATUS = _response.status_code
      _E_RETURN = E_RETURN
      _E_MSG = f"{E_MSG}Status Code: {_E_STATUS}"
      _E_ERROR = True
      return _E_STATUS, _E_RETURN, _E_MSG, _E_ERROR

  def group_games(self, id, *args, **kwargs) -> object:
    try:
      return self._group_games(id)
    except Exception as e:
      return e

  def _user_games(self, _, *args, **kwargs) -> object:
    _response = requests.get(f"{self.usergames_url.replace('ID_HERE', str(_))}")
    if _response.status_code == 200:
      _user_data = _response.json()
      return _user_data
    else:
      _E_STATUS = _response.status_code
      _E_RETURN = E_RETURN
      _E_MSG = f"{E_MSG}Status Code: {_E_STATUS}"
      _E_ERROR = True
      return _E_STATUS, _E_RETURN, _E_MSG, _E_ERROR

  def user_games(self, id, *args, **kwargs) -> object:
    try:
      return self._user_games(id)
    except Exception as e:
      return e

  def _user_friends(self, _, *args, **kwargs) -> object:
    _response = requests.get(f"{self.userfriends_url.replace('ID_HERE', str(_))}")
    if _response.status_code == 200:
      _user_data = _response.json()
      return _user_data
    else:
      _E_STATUS = _response.status_code
      _E_RETURN = E_RETURN
      _E_MSG = f"{E_MSG}Status Code: {_E_STATUS}"
      _E_ERROR = True
      return _E_STATUS, _E_RETURN, _E_MSG, _E_ERROR

  def user_friends(self, id, *args, **kwargs) -> object:
    try:
      return self._user_friends(id)
    except Exception as e:
      return e

  def _user_friends_count(self, _, *args, **kwargs) -> object:
    _response = requests.get(f"{self.userfriends_url.replace('ID_HERE', str(_))}/count")
    if _response.status_code == 200:
      _user_data = _response.json()
      return _user_data
    else:
      _E_STATUS = _response.status_code
      _E_RETURN = E_RETURN
      _E_MSG = f"{E_MSG}Status Code: {_E_STATUS}"
      _E_ERROR = True
      return _E_STATUS, _E_RETURN, _E_MSG, _E_ERROR

  def user_friends_count(self, id, *args, **kwargs) -> object:
    try:
      return self._user_friends_count(id)
    except Exception as e:
      return e

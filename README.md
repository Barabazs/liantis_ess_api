liantis-ess-api
========

Unofficial API wrapper for [Liantis ESS](https://www.liantis.be/myliantis/).

Based on the now obsolete [e-OK wrapper](https://github.com/dotEsuS/e_ok_api). The code is partially rewritten since Liantis changed their API and heavily modified some parts.


Usage
-------

	
Examples
-------
```python
y = MijnPrestaties()
y.login('Username', 'Password')
my_user_id = y.get_employee_id()

print(y.get_organisation_counter_settings(my_user_id))
```
 

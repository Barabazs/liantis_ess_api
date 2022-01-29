liantis-ess-api
========

[![PyPI version shields.io](https://img.shields.io/pypi/v/liantis_ess_api.svg)](https://pypi.python.org/pypi/liantis_ess_api/)
[![Travis - CI ](https://img.shields.io/travis/dotEsuS/liantis_ess_api.svg)](https://travis-ci.org/dotEsuS/liantis_ess_api)

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
 

## Donation

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/T6T51XKUJ)

|Ethereum|Bitcoin|
|:-:	|:-:	|
|0x6b78d3deea258914C2f4e44054d22094107407e5|bc1qvvh8s3tt97cwy20mfdttpwqw0vgsrrceq8zkmw|
|![eth](https://raw.githubusercontent.com/Barabazs/Barabazs/master/.github/eth.png)|![btc](https://raw.githubusercontent.com/Barabazs/Barabazs/master/.github/btc.png)|


<p align="center">
  <img src="https://github.com/l4tt/uscan/assets/97377137/f6034b22-1e39-411b-80cd-11f3b00b680f" /></img>
  
  ![Build Status](https://travis-ci.org/evyatarmeged/Raccoon.svg?branch=master)
  ![license](https://img.shields.io/github/license/mashape/apistatus.svg)
  ![os](https://img.shields.io/badge/OS-Linux,%20macOS-yellow.svg)
  ![pythonver](https://img.shields.io/badge/python-3.5%2B-blue.svg)
  ![uscan](https://img.shields.io/badge/version-0.2.1-lightgrey.svg)  
</p>


### Contact
join uscans telegram community to hear about updates and request new features or talk about issues
<a href="https://t.me/uscan_updates">https://t.me/uscan_updates</a>


### To install uscan, follow these steps:
1. Clone the uscan repository from GitHub using the following command:
```sh
   git clone https://github.com/l4tt/uscan.git
```
2. Install the google Python package using pip:
```sh
   pip install google
```
3. Run Uscan.py using Python 3:
```sh
   python3 Uscan.py
```
4. Type help in the interactive shell, and please use this format for urls (``https:// | http://``)

### Features [Uscan remastered]
- [x] DNS details
- [x] DNS visual mapping using DNS dumpster
- [x] WHOIS information
- [x] Auto Dorker
- [x] Sql injection finder
- [x] LFI finder
- [x] Xss injection finder   
- [x] TLS Data - supported ciphers, TLS versions,
certificate details and SANs
- [x] Port Scan
- [x] Services and scripts scan
- [x] URL fuzzing and dir/file detection
- [x] Subdomain enumeration - uses Google dorking, DNS dumpster queries,
 SAN discovery and bruteforce
- [x] Web application data retrieval:<br>
  - CMS detection [users, plugins, themes]
  - Detects Vuln plugins and recent CVE's
  - Web server info and X-Powered-By
  - robots.txt and sitemap extraction
  - Header detection
- [x] Detects known WAFs & Cloudflare
- [x] Retrys timeout requests 
- [x] Supports anonymous routing through Tor/Proxies
- [x] Uses asyncio for improved performance
- [x] Saves output to json format - results/*


### About uscan
``uscan`` is a universal scanner designed to target systems such as WordPress, Joomla, Drupal, and Vbulletin. It uses automation to identify vulnerabilities in a target system, making it a more efficient and effective tool than similar tools like ``Vulnnr``.
With ``uscan``, you can quickly and easily scan your target system for vulnerabilities, allowing you to take proactive steps to secure your system and protect it from potential attacks.
Overall, uscan is a powerful and versatile tool that can help you keep your systems secure and protected from potential threats. vist <a href="https://github.com/l4tt/uscan/wiki">wiki</a> for more information about uscan.

### Coming Soon
I have decided it was a good idea to remake ``uscan``, Since this code is messy and gross to my own eyes. The version i am working on is not for public use yet and will be contained in a seprate repo until I think it's fit to move the code over to this repo. You can check out ``uscan remastered`` here <a href="https://github.com/l4tt/Uscan_Remastered">Alpha</a>. I will be adding new modules, exploits, DNS Mapping and more! come check it out.

### Showcase of uscan remastered, <a href="https://github.com/l4tt/Uscan_Remastered">Uscan Remastered</a>
![2023-06-14 22-47-20](https://imgur.com/CsiPC8X.gif)


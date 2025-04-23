
<b><p align='center'>[![Packt Sale](https://static.packt-cdn.com/assets/images/humble+bundle/3.png)](https://www.humblebundle.com/books/networking-mastery-packt-books?utm_medium=affiliate&utm_campaign=&utm_term=472505a3-5e1b-ea11-a812-00224801bc51&utm_content=)</p></b> 

# Network Automation with Nautobot

<a href="https://www.packtpub.com/product/network-automation-with-nautobot/9781837637867?utm_source=github&utm_medium=repository&utm_campaign=9781837637867"><img src="https://content.packt.com/_/image/original/B19544/cover_image_large.jpg" alt="" height="256px" align="right"></a>

This is the code repository for [Network Automation with Nautobot](https://www.packtpub.com/product/network-automation-with-nautobot/9781837637867?utm_source=github&utm_medium=repository&utm_campaign=9781837637867), published by Packt.

**Adopt a network source of truth and a data-driven approach to networking**

## What is this book about?
This book will help you understand why a network source of truth is needed for long-term network automation success, which will in turn save you hundreds of hours in deploying and integrating Nautobot into network automation.

This book covers the following exciting features:
* Understand network sources of truth and the role they play in network automation architecture
* Gain an understanding of Nautobot as a network source and a network automation platform
* Convert Python scripts to enable self-service Nautobot Jobs
* Understand how YAML files in Git can be easily integrated into Nautobot
* Get to grips with the NetDevOps ecosystem around Nautobot and its app ecosystem
* Delve into popular Nautobot Apps including Single Source of Truth and Golden Config

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1837637865) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, chapter-03.

The code will look like the following:
```
devices_url = "https://demo.nautobot.com/api/dcim/devices/"
# adds ams01-leaf-11 to the location AMS01
r = session.post(devices_url, data=json.dumps(payload))
# the UUID of the device will be saved for the next API call
device_id = r.json()["id"]
```

**Following is what you need for this book:**
This book is for network engineers, network automation engineers, and software engineers looking to support their network teams by building custom Nautobot Apps. A basic understanding of networking (e.g. CCNA) and knowledge of the fundamentals of Linux, Python programming, Jinja2, YAML, and JSON are needed to get the most out of this book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-16).
### Software and Hardware List
| Software required |
| -------- | 
| Ubuntu 22.04 |  
| Python 3+ |  
| Ansible 2.16+ |  
| Nautobot 2.1+ |  


### Related products
* Pentesting Active Directory and Windows-based Infrastructure [[Packt]](https://www.packtpub.com/product/pentesting-active-directory-and-windows-based-infrastructure/9781804611364?utm_source=github&utm_medium=repository&utm_campaign=9781804611364) [[Amazon]](https://www.amazon.com/dp/1804611360)

* Security Monitoring with Wazuh [[Packt]](https://www.packtpub.com/product/security-monitoring-with-wazuh/9781837632152?utm_source=github&utm_medium=repository&utm_campaign=9781837632152) [[Amazon]](https://www.amazon.com/dp/1837632154)

## Get to Know the Authors
**Jason Edelman**
is the Founder and CTO at Network to Code (NTC). Prior to NTC, Jason spent a career in networking developing and architecting network solutions with his last role leading efforts around SDN and programmability. Jason is co-author of O’Reilly’s Network Programmability & Automation book. He is a former CCIE and has a B.E. in Computer Engineering from Stevens Institute of Technology. He can be found on X as @jedelman8.

**Glenn Matthews**
is a Principal Engineer at Network to Code and is the tech lead of the Nautobot project. Prior to NTC, he worked at Cisco for more than a decade in various software roles. Glenn is committed to designing and developing quality software to help make the world a better place. His academic background includes a master’s degree in computer science from the University of Georgia. He lives in North Carolina with his daughter and a very persistent cat.

**Josh VanDeraa**
is a network veteran turned network automation geek and currently a Services Director at NTC. Josh has spent many years in large enterprise network engineering before diving into network automation. Josh is the author of the self published book Open Source Network Management and has a B.S. of Telecom Systems from University of Wisconsin, Stout. Find Josh on social through his blog at josh-v.com.

**Ken Celenza**
is VP of Network Automation Architecture at NTC. Ken is an experienced network and automation engineer with over 20 years of experience working in military, consulting, and enterprise environments. Ken leads client engagements at NTC as both a developer and an architect and serves as a mentor to Network Engineers. He can be found on X as @itdependsnet.

**Christian Adell**
is a Principal Architect at NTC. He is focused on building network automation solutions for diverse use cases, with great emphasis on open source software. He is passionate about learning and helping others to be happier, but also has more hobbies than hours in the day, so working remotely from Barcelona gives him the time and the space to achieve his dreams. Christian is co-author of O’Reilly’s Network Programmability & Automation book. He can be found on X as @chadell0.

**Brad Haas**
is a VP of Professional Services at NTC. With a career spanning more than two decades, Brad has been instrumental in delivering innovative solutions, particularly in automation and the integration of software-defined infrastructure. His career is distinguished by his achievement of numerous certifications, encompassing multiple CCIEs as well as cloud certifications, demonstrating his commitment to ongoing learning and staying at the forefront of industry developments.

**Bryan Culver**
is an Engineering Manager at NTC, where he is building the team behind Nautobot Cloud. He has served many roles in his career related to automation, andh he maintains a strong software engineering background, graduating from Oakland University with a B.S. in Computer Science. Outside of work he enjoys time with his wife and children, wielding power tools on home renovation projects, traveling, and Formula 1 races. He can be found on Mastodon at @bryanculver@fosstodon.org.

**John Anderson**
is a Principal Consultant at NTC and the Nautobot Product Owner. John has 10 years of experience in networking and software development, and has been a maintainer and contributor to a number of open source projects over the years. John lives in South Carolina and is working on a Ph.D. in Computer Science with a focus on zero trust network security, at Clemson University.

**Gary Snider**
is a software engineer with 10 years of experience in Network Automation. He is currently a core developer for the Nautobot project at NTC. Prior to NTC, he had a career in networking designing and maintaining data centers, branch offices, and large campus networks for state and federal governments.

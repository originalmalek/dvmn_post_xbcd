# Post comics XKCD to VK.com automatically 
The project post comics XKCD to VK.com automatically. 


## Description
The code: 
Download random comic from [XKCD](https://xkcd.com/) and post the comic to [VK.com](https://vk.com) public automatically using API.

* The project use:  
  * [XKCD API](https://xkcd.com/json.html);  
  * [VK API](https://vk.com/dev).
  

## Requirements
Python >=3.7  
Register application on [VK API](https://vk.com/dev) ang get API key.  
Creat public on vk.com  
  
Create file '.env' and add the code:
```
VK_ACCESS_TOKEN = your_vk_app_token
```

Install requirements modules:
```
pip install -r requirements.txt	
```


### How to use

Install requirements.  
Open and run 'main.py'.
```
python main.py	
```


## Additional information
You have to change Group ID. For it change variable group_id in **main()** function:
```
group_id = your_group_ID
```

* How to get Access token [vk.com](https://vk.com/apps?act=manage):
  * Use [Implicit Flow](https://vk.com/dev/implicit_flow_user) procedure
  * Delete **redirect_url** from url
  * In scope parameters enter scope=photos,groups

* How to create [vk.com](https://vk.com/apps?act=manage) app:
  * Go to page [vk.com/apps](https://vk.com/apps?act=manage)
  * Click on 'Creat App' button
  * Fill fields
  * Change platform 'Standalone'

* Where to get group id:
  * Go to page [vk.com/groups](https://vk.com/groups)
  * Click on 'Creat community' button
  * Fill fields
  * You'll see link 'https://vk.com/publicXXXXXXXXX' where XXXXXXXXX is your group id


## Project goal

The code was written for educational purpose on online course for Api developers [Devman](http://dvmn.org). 

![Solar Host](https://scott.ee/assets/img/solar-host.png)

# Solar Host

* Status: ✅ Active
* Contributors: [@scottsweb](http://twitter.com/scottsweb)
* Description: Solar hosting with a Raspberry Pi Zero. 
* Author: [Scott Evans](https://scott.ee)
* Author URI: [https://scott.ee](https://scott.ee)

## About

This repo holds some code that will be useful if you wish to host a [static website on a solar powered Raspberry Pi](https://scott.ee/project/solar-hosting-raspberry-pi/). The `battmon` folder contains a Python script that calculates the battery percentage, battery voltage, load, uptime and CPU temperature and ouputs it as JSON to be read by your website. 

The `docker-compose.yaml` can be used to re-create the hosting environment. The web server is [Static Web Server](https://github.com/joseluisq/static-web-server) and is perfect for a low powered device like the Pi. The `deploy.sh` script is used to clone and deploy my website to two Raspberry Pi hosts (one solar, one backup).

This project is ongoing and a full write up and hardware requirements can be found on my website:

[https://scott.ee/project/solar-hosting-raspberry-pi/](https://scott.ee/project/solar-hosting-raspberry-pi/)

My site is the one being served from the solar Pi!

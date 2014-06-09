Titan
=====

Titan was designed with one large goal in mind, continuous reporting. The framework is tied closely with the Mac OS X core to detect an active Internet connection and push any reports which may have been blocked.

Origination
-----------
Titan spawned from the hard work of the MIDAS/Tripyarn project, a Etsy/Facebook masterpiece. We wanted to create a framework that was easily extended and simply managed by utilities like Chef/Puppet. Additionally, MIDAS used Syslog to report back to a centralized logging service. This is great, but we wanted a solution that would store/queue results and relay them when an Internet connection was detected. 

Features
--------

The following features are currently supported in Titan:

  - Dynamic module loading
  - Easy 3rd-party module installation
  - Supports Python, Ruby, Bash, Perl or PHP module runtimes
  - REST endpoint and reporting via Olympus
  - Inventory management __[in dev]__
  - Local report viewing __[in dev]__
  - Customizable reporting mechanism __[in dev]__

Usage
-----

### Installation:



### Configuration:

Default configuration expects Titan to exist in `/usr/local/titan/`. Of course, you can change this and update `TITAN_PATH` in `/etc/profile.d` or `/etc/environments` depending on what system you are using. You can use the `titan.conf-example` file as a boilerplate for your configuration which should be named `titan.conf`.

    cd /path/to/titan
    cp titan.conf-example titan.conf
    vi titan.conf


### Adding Modules:

Adding modules is **simple** using `git clone` in the `modules/` directory. 

    cd /path/to/titan/modules
    git clone https://github.com/titan-modules/git_repository.git

The autoloader will identify and load the module on next run.


### Creating Modules:

Take a look at some of the existing modules until we are able formalize our documentation.

Contributors
---------------------------

#### Titan Contributors

+ __Mike Mackintosh__ ([@mikemackintosh](https://twitter.com/mikemackintosh))

#### Original MIDAS Contributors

+ __Mike Arpaia__ ([@mikearpaia](https://twitter.com/mikearpaia))
+ __Chris Biettchert__ ([@chrisbiettchert](https://twitter.com/chrisbiettchert))
+ __Ben Hughes__ ([@benjammingh](https://twitter.com/benjammingh))
+ __Zane Lackey__ ([@zanelackey](https://twitter.com/zanelackey))
+ __mimeframe__ ([@mimeframe](https://twitter.com/mimeframe))

Enjoy.
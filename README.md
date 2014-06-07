Titan
=====

Titan was designed with one large goal in mind, continuous reporting. The framework is tied closely with the Mac OS X core to detect an active Internet connection and push any reports which may have been blocked. 

Origination
-----------
Titan spawned from the hard work of the MIDAS/Tripyarn project, a Etsy/Facebook masterpiece. Although effective, MIDAS uses syslog as a reporting mechanism. This is great, but we already log over 500 million logs a day from our services. We wanted to create a RESTful interface with anomaly detection and hooks that can report and take action immediately, rather than having to parse through a butt-load of logs at a later time.

Features
--------

The following features are currently supported in Titan:

  - Easy 3rd-party module installation
  - Dynamic module loading
  - Added PHP runtime for modules
  - Inventory management [in dev]
  - Local report viewing [in dev]
  - Customizable reporting mechanism [in dev]

Usage
-----

### Installation:

### Configuration:

### Adding Modules:

### Creating Modules:


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
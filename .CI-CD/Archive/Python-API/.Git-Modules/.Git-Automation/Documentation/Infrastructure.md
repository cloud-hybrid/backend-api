# Infrastructure - _Server & Technology Information_

> __Proprietary Notice__
>
> The following source file(s) contains confidential, proprietary information. Unauthorized use is strictly prohibited. No portions may be accessed, copied, reproduced, or incorporated outside of this domain without Cloud Hybrid (LLC.)'s written consent.
>
> Special permissions have been givin to the _**20r - 20th Regiment of Foot**_ namespace; such permissions are limited to access, usage, and revisioning. Under no circumstances can the **20r [...]** namespace claim ownership or copyright the source code created by Cloud Hybrid. However, usage and further development of such source code can continue regardless of Cloud Hybrid's future involvment(s).
>
> Please contact [jacob.sanders@cloudhybrid.io](jacob.sanders@cloudhybrid.io) for further copyright, contact, and authorization information.

***

![Header-Diagram](./Documentation/Online-Gaming-Infrastructure.png)

***

## Table of Contents ##

[__**Overview**__](#overview)

[__**Cloud-API**__](#cloud-api)

[__**Server Infrastructure**__](#server-infrastructure)

- [**Definitions**](#server-definitions)
- [**Virtual Machines**](#virtual-machines)

[__**Licensing**__](#license-notice-and-contact-information)

***

## Task Board ##

### Critical ###

- [ ] Complete Manual

### Important ###

- [ ] Create Server-Event Calendar
  - <details><summary><strong>Details</strong></summary>

    - Shutdown Times
    - Start Times
    - In-Game Events
    - Scheduled Maintence

  </details>
  
  - <details><summary><strong><code>Calendar.html</code></strong></summary>

    ```html
    <div class="ui container">
      <div class="ui menu">
        <div class="header item">Brand</div>
        <a class="active item">Link</a>
        <a class="item">Link</a>
        <div class="ui dropdown item">
          Dropdown
          <i class="dropdown icon"></i>
          <div class="menu">
            <div class="item">Action</div>
            <div class="item">Another Action</div>
            <div class="item">Something else here</div>
            <div class="divider"></div>
            <div class="item">Separated Link</div>
            <div class="divider"></div>
            <div class="item">One more separated link</div>
          </div>
        </div>
        <div class="right menu">
          <div class="item">
            <div class="ui action left icon input">
              <i class="search icon"></i>
              <input type="text" placeholder="Search">
              <button class="ui button">Submit</button>
            </div>
          </div>
          <a class="item">Link</a>
        </div>
      </div>
    </div>

    <br>
    <div class="ui container">
      <div class="ui grid">
        <div class="ui sixteen column">
          <div id="calendar"></div>
        </div>
      </div>
    </div>

    </div>
    ```

    </details>
  - <details><summary><strong><code>Calendar.js</code></strong></summary>

    ```javascript
    $(document).ready(function() {
      $('#calendar').fullCalendar({
          header: {
              left: 'prev,next today',
              center: 'title',
              right: 'month,basicWeek,basicDay'
          },
          defaultDate: '2016-12-12',
          navLinks: true, // can click day/week names to navigate views
          editable: true,
          eventLimit: true, // allow "more" link when too many events
          events: [
              {
                  title: 'All Day Event',
                  start: '2016-12-01'
              },
              {
                  title: 'Long Event',
                  start: '2016-12-07',
                  end: '2016-12-10'
              },
              {
                  id: 999,
                  title: 'Repeating Event',
                  start: '2016-12-09T16:00:00'
              },
              {
                  id: 999,
                  title: 'Repeating Event',
                  start: '2016-12-16T16:00:00'
              },
              {
                  title: 'Conference',
                  start: '2016-12-11',
                  end: '2016-12-13'
              },
              {
                  title: 'Meeting',
                  start: '2016-12-12T10:30:00',
                  end: '2016-12-12T12:30:00'
              },
              {
                  title: 'Lunch',
                  start: '2016-12-12T12:00:00'
              },
              {
                  title: 'Meeting',
                  start: '2016-12-12T14:30:00'
              },
              {
                  title: 'Happy Hour',
                  start: '2016-12-12T17:30:00'
              },
              {
                  title: 'Dinner',
                  start: '2016-12-12T20:00:00'
              },
              {
                  title: 'Birthday Party',
                  start: '2016-12-13T07:00:00'
              },
              {
                  title: 'Click for Google',
                  url: 'https://google.com/',
                  start: '2016-12-28'
              }
          ]
      });
    });
    ```

    </details>
  - <details><summary><strong>SQL Schema</code></strong></summary>

    ```sql
    +----------+----------------+
    | ID       | NAME           |
    +----------+----------------+
    | 1        | Sample event 1 |
    | 2        | Second  event  |
    | 3        | Third event    |
    +----------+----------------+

    +----+----------+--------------+------------------+-------------+--------------+------------+-------------+----------------+
    | ID | event_id | repeat_start | repeat_interval  | repeat_year | repeat_month | repeat_day | repeat_week | repeat_weekday |
    +----+----------+--------------+------------------+-------------+--------------+------------+-------------+----------------+
    | 1  | 1        | 2014-07-04   | 7                | NULL        | NULL         | NULL       | NULL        | NULL           |
    | 2  | 2        | 2014-06-26   | NULL             | 2014        | *            | *          | 2           | 5              |
    | 3  | 3        | 2014-07-04   | NULL             | *           | *            | *          | *           | 5              |
    +----+----------+--------------+------------------+-------------+--------------+------------+-------------+----------------+
    ```

    </details>
  - <details><summary><strong>SQL Code</code></strong></summary>

    ```sql
    CREATE TABLE IF NOT EXISTS `events` (
      `ID` int(11) NOT NULL AUTO_INCREMENT,
      `NAME` varchar(255) NOT NULL,
      PRIMARY KEY (`ID`)
    ) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

    --
    -- Dumping data for table `events`
    --

    INSERT INTO `events` (`ID`, `NAME`) VALUES
    (1, 'Sample event'),
    (2, 'Another event'),
    (3, 'Third event...');

    CREATE TABLE IF NOT EXISTS `events_meta` (
      `ID`               int(11) NOT NULL AUTO_INCREMENT,
      `event_id`         int(11) NOT NULL,
      `repeat_start`     date NOT NULL,
      `repeat_interval`  varchar(255) NOT NULL,
      `repeat_year`      varchar(255) NOT NULL,
      `repeat_month`     varchar(255) NOT NULL,
      `repeat_day`       varchar(255) NOT NULL,
      `repeat_week`      varchar(255) NOT NULL,
      `repeat_weekday`   varchar(255) NOT NULL,
      PRIMARY KEY (`ID`),
      UNIQUE KEY `ID` (`ID`)
    ) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

    --
    -- Dumping data for table `events_meta`
    --

    INSERT INTO `events_meta` (`ID`, `event_id`, `repeat_start`, `repeat_interval`, `repeat_year`, `repeat_month`, `repeat_day`, `repeat_week`, `repeat_weekday`) VALUES
    (1, 1, '2014-07-04', '7', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL'),
    (2, 2, '2014-06-26', 'NULL', '2014', '*', '*', '2', '5'),
    (3, 3, '2014-07-04', 'NULL', '*', '*', '*', '*', '1');
    ```

    </details>

- [ ] Reimplement WYSIWYG Editor using Python Backend

### Normal ###

- [ ] Show 20r Applicable Staff how to create Wiki pages on website, as well as, document such procedures in manual

### Backlog ###

- [ ] Bring Cloud-Container Bot
- [ ] Include Markdown Guide and overall all Reading-Library materials in Manual

### Ideas ###

- [ ] Video Games Are "Categories" and have directories/pages on website
  - Essentially a blog -- Users from the game's division are selected to discuss/make a tutorial/essentially blog about a certain aspect related to the game

***

## Overview ##

The technology administrator, **Jacob B. Sanders** _(Null Byte, Segmentatational, Snow)_, owns a United States _Limited Liability Company_ (LLC) called _**Cloud Hybrid**_. Under the Cloud Hybrid namespace exists various software programs, APIs, and other technology stacks; one of which includes gaming.

Cloud Hybrid is both investing and hosting gaming infrastructure for **20r**. Null Byte is providing such resources in hope 20r can eventually become profitable where staff members are paid for their services and contribututions. However, it should be noted Null Byte is also _developing_ various software-related programs and services to ease the operations and management of infrastructure -- these services may or may not be open-source and should be assumed owned by Cloud Hybrid. Such services _**do not include the development of the website**_. Null Byte is developing the website free-of-charge and ownership of the website and gaming-servers is and always will be 20r, but some of the backend services, such as the server dashboard, is ultimately owned by Cloud Hybrid.

As a final & important note:

Null Byte's programs, source code, etc. related to 20r are all licensed to give the 20r namespace special access, usage, and development. In the event of Null Byte's leave, 20r can continue to use and further develop such services, APIs, and programs owned by Cloud Hybrid. At the end of the day, with or without Null Byte, operational function and availability will remain the same.

***

## Cloud-API ##

### Installation ###

__Ubuntu +18.04__
1. Open `Terminal.app`.
2. Install [nodeJS](https://nodejs.org/dist/v12.16.1/node-v12.16.1-linux-x64.tar.xz) via link or APT Package Manager:
  ```bash
  sudo apt install nodejs \
    npm \
      -y
  ```
3. Create a `package.json` file (auto-generates project dependencies):
  ```bash
  npm init \
    --yes
  ```
4. Install __Fomantic-UI__:
  ```bash
  npm install fomantic-ui-css
  ```
5. Move directories:
  ```bash
  sudo mkdir ./API/Website/Static/User-Interface
  sudo cp -r ./node_modules/fomantic-ui-css/* ./API/Website/Static/User-Interface
  sudo cp -r ./node_modules/jquery ./API/Website/Static/
  ```

***

## Server Infrastructure ##

The meaning of ***Server Infrastructure*** is a general, blanketed term used to reference **_everything related to servers_**. Server infrastructure includes the programming, automation, and management of physical or virtual machines, containers, and gaming servers. An important note regarding gaming servers: they're always a _process_ or _service_ that runs on a server -- **Video game servers are not the actual physical servers or virtual machines, but just a simple process**.

These distinctions need to be understood when further reading the infrastructure manual.

### Server Definition(s) ###

![Server-Example](./Documentation/Server-Virtual-Machines-Example.png) ![Dedicated-Server-Example](./Documentation/Virtual-Dedicated-Server.png)

The term **_server_** refers to a computer program or process (running program), however, in the context of the infrastructure manual, a server **_is a virtual machine_**; virtual machines are encapsulated kernals (Operating Systems) that reside on a physical computer. **_Processes_**, also referenced as _service(s)_, are the instances of a computer program that gets executed by one or many threads of a processor (CPU). Processes contains the program code and its activity. Depending on the kernal's operating system (OS), a process may be made up of multiple threads of execution that execute instructions concurrently (at the same time). In the gaming industry, a **_dedicated gaming server_** is a multiplayer-based networking connection that allows all connected clients (players) to interact in real-time. 

> Please awknowledge the aforementioned definitions are heavily dependent upon *context* -- i.e. if discussion is taking place while managing a fleet of virtual machines or playing a video game.

Finally, summarizing the terms and definitions:

- **_Server_**: A Physical or Virtual Machine with a subsequent Operating System.
- **_Dedicated Gaming Server_**: Networking process(es) or service(s) that allow server-client interactions.
- **_Process_ (Service)**: Instances of a computer program.

### Management vs Administration ###

Server infrastructure management is different than administration. Specifically, *administration is about defining and adjusting service-level settings* such as adding an administrator to a dedicated gaming server. Management almost always comes down to a lower level where a User may be turning the actual server on or off, or spinning up a new dedicated gaming server **process**. Accessing server infrastructure is also apart of management where Users need either RDP, SSH, or physical access in order to modify settings. Administration can usually be done while in game, but all administrative actions are also available while accessing the server via RDP, SSH, or physically.

Because Cloud Hybrid primarily uses Linux-based server infrastructure, management is done via SSH. Please visit the [SSH](#ssh) section for further details.

Upon need for a Windows server, a section and instructions will be provided for RDP information.

***

## Accessing Server Infrastructure via SSH ##

### Overview ###

SSH is a cryptographic network protocol that gives users, particularly system administrators, a secure way to access a computer or server over an unsecured network (Internet). SSH provides strong authentication and encrypted data communications between two computers connecting over an open network such as the internet. It is a secure alternative to the non-protected login protocols (such as telnet, rlogin) and insecure file transfer methods (such as FTP). SSH refers both to the cryptographic network protocol and to the suite of utilities that implement that protocol. An SSH server (process), by default, listens on the standard Transmission Control Protocol (TCP) port 22. In the context of gaming and within the infrastructure manual, all servers (gaming and otherwise) are always, additionally, SSH servers.

While Null Byte may be working on APIs and certain programs that may make working with servers easier, such services are take time to develop & automate. Additionally, general programs are first created that can be used with all servers -- regardless of perhaps a game or service. SSH allows system administrators to perform these same API functions and many more specific server-related actions.

Unfortunetly, working within SSH requires knowledge of shell-related technologies/programming languages. The upside is that many functions + commands can be described in as little as a single line of text.

To make such access easier, Users can download an SSH client called [**PuTTY**](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) (Available for both linux systems and Windows OS).

Please see [PuTTY - Getting Started](https://the.earth.li/~sgtatham/putty/0.73/htmldoc/Chapter2.html#gs-hostkey) for PuTTY-specfic documentation and guides.

### Use-Case: Restarting a Server ###

Restarting a server usually fixes most issues related to a failed service. For example, say a video game server (_the service_) is not showing up on a User's server-list; restarting the server will often reinitialize the failed service and consquently correct itself upon reboot.

_In-Progress_

***

## Virtual Machines ##

<details><summary><strong>Cloud-Hybrid-Development</code></strong></summary>

- ID: **i-053816703448863e1**
- Elastic-IP: **13.58.122.68**
- Region: **US-East-2 (Ohio)**
- Type: **t2.micro**

[**Cloud-Hybrid-Development.pem**](Keys/Cloud-Hybrid-Development.pem)

</details>

<details><summary><strong>20r-Mordhau-1</code></strong></summary>

- Servers:
  - **`20r Duels Server (1) - Compute Optimized`**
  - **`20r Competitve Server (1) - Compute Optimized`**
  - **`20r Competitve Server (2) - Compute Optimized`**
  - **`20r Experimental Server (1) - Compute Optimized`**

- ID: **i-0e7002c513ac74793**
- Elastic-IP: **3.20.245.245**
- Region: **US-East-2 (Ohio)**
- Type: **c5.large**
  - `25.0 Gb/s Network I/O`
  - `75.00 GB HDD`

[**20r-Mordhau-Server-1.pem**](Keys/20r-Mordhau-Server-1.pem)

</details>

<details><summary><strong>20r-Squad-1</code></strong></summary>

- Servers:
  - **`20th Regiment of Foot - Compute Optimized`**

- ID: **i-0904cc89dc05ead52**
- Elastic-IP: **3.20.245.245**
- Region: **US-East-2 (Ohio)**
- Type: **c5.large**
  - `25.0 Gb/s Network I/O`
  - `75.00 GB HDD`

[**20r-Squad-Server-1.pem**](Keys/20r-Squad-Server-1.pem)

</details>

<details><summary><strong>20r-Rust-1</code></strong></summary>

- Servers:
  - **`20r Rust Server (1) - Compute Optimized`**

- ID: **i-0c9de1d2f9bcce1c4**
- Elastic-IP: **3.126.155.54**
- Region: **EU-Central-1 (Frankfurt)**
- Type: **c5n.large**
  - `25.0 Gb/s Network I/O`
  - `50.00 GB HDD`

[**20r-Rust-Server-1.pem**](Keys/20r-Rust-Server-1.pem)

</details>

***

## Storage ##

Files and other entities that require storage are stored in cloud resource called a [**_bucket_**](https://en.wikipedia.org/wiki/Amazon_S3).

Cloud Hybrid provides the following:

- [Cloud-Hybrid-Storage](http://cloud-hybrid.s3-website.us-east-2.amazonaws.com/)
- [Cloud-Hybrid-Logging](http://s3-cloud-hybrid.s3-website.us-east-2.amazonaws.com/)
- [20r-Storage](http://20r.s3-website.us-east-2.amazonaws.com/)

Additionally, select locations and domain archives may be located at [cloudhybrid.io](https://cloudhybrid.io/) or [storage.cloudhybrid.io](https://storage.cloudhybrid.io/).

***

## License, Notice, and Contact Information ##

<details><summary><strong>Proprietary Notice</strong></summary>

```Markdown
┌─────────────────────────────────────────────────────────┐
│                                                         │
│                   Proprietary Notice                    │
│               ──────────────────────────                │
│   The following source file(s) contains confidential,   │
│  proprietary information. Unauthorized use is strictly  │
│    prohibited. No portions may be copied, reproduced,   │
│      or incorporated outside of this domain without     │
│          Cloud Hybrid LLC prior written consent.        │
│                                                         │
│          Copyright (C) 2019, Cloud Hybrid, LLC.         │
│                    All rights reserved.                 │
│                                                         │
│   ┌────────────────────────────────────────────────┐    │
│   │ Copyright │         Cloud Hybrid, LLC.         │    │
│   │───────────│────────────────────────────────────│    │
│   │  License  │         (Private-Use Only)         │    │
│   │───────────│────────────────────────────────────│    │
│   │  Creator  │          Jacob B. Sanders          │    │
│   │───────────│────────────────────────────────────│    │
│   │   Email   │   jacob.sanders@cloudhybrid.io     │    │
│   └────────────────────────────────────────────────┘    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

</details>

<details><summary><strong>Source Code</strong></summary>

The “source code” for a work means the preferred form of the work for making modifications to it. “Object code” means any non-source form of a work.

A “Standard Interface” means an interface that either is an official standard defined by a recognized standards body, or, in the case of interfaces specified for a particular programming language, one that is widely used among developers working in that language.

The “System Libraries” of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component, but which is not part of that Major Component, and (b) serves only to enable use of the work with that Major Component, or to implement a Standard Interface for which an implementation is available to the public in source code form. A “Major Component”, in this context, means a major essential component (kernel, window system, and so on) of the specific operating system (if any) on which the executable work runs, or a compiler used to produce the work, or an object code interpreter used to run it.

The “Corresponding Source” for a work in object code form means all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. However, it does not include the work's System Libraries, or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work. For example, Corresponding Source includes interface definition files associated with source files for the work, and the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work.

The Corresponding Source need not include anything that users can regenerate automatically from other parts of the Corresponding Source.

The Corresponding Source for a work in source code form is that same work.

</details>

<details><summary><strong>Special Access and Permissions</strong></summary>

“Additional permissions” are terms that supplement the terms of this License by making exceptions from one or more of its conditions. Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License, to the extent that they are valid under applicable law. If additional permissions apply only to part of the Program, that part may be used separately under those permissions, but the entire Program remains governed by this License without regard to the additional permissions.

When you convey a copy of a covered work, you may at your option remove any additional permissions from that copy, or from any part of it. (Additional permissions may be written to require their own removal in certain cases when you modify the work.) You may place additional permissions on material, added by you to a covered work, for which you have or can give appropriate copyright permission.

Notwithstanding any other provision of this License, for material you add to a covered work, you may (if authorized by the copyright holders of that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the terms of sections 15 and 16 of this License; or
    b) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or
    c) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or
    d) Limiting the use for publicity purposes of names of licensors or authors of the material; or
    e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or
    f) Requiring indemnification of licensors and authors of that material by anyone who conveys the material (or modified versions of it) with contractual assumptions of liability to the recipient, for any liability that these contractual assumptions directly impose on those licensors and authors.

All other non-permissive additional terms are considered “further restrictions” within the meaning of section 10. If the Program as you received it, or any part of it, contains a notice stating that it is governed by this License along with a term that is a further restriction, you may remove that term. If a license document contains a further restriction but permits relicensing or conveying under this License, you may add to a covered work material governed by the terms of that license document, provided that the further restriction does not survive such relicensing or conveying.

If you add terms to a covered work in accord with this section, you must place, in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms.

Additional terms, permissive or non-permissive, may be stated in the form of a separately written license, or stated as exceptions; the above requirements apply either way.

</details>

<details><summary><strong>Patents</strong></summary>

A “contributor” is a copyright holder who authorizes use under this License of the Program or a work on which the Program is based. The work thus licensed is called the contributor's “contributor version”.

A contributor's “essential patent claims” are all patent claims owned or controlled by the contributor, whether already acquired or hereafter acquired, that would be infringed by some manner, permitted by this License, of making, using, or selling its contributor version, but do not include claims that would be infringed only as a consequence of further modification of the contributor version. For purposes of this definition, “control” includes the right to grant patent sublicenses in a manner consistent with the requirements of this License.

Each contributor grants you a non-exclusive, worldwide, royalty-free patent license under the contributor's essential patent claims, to make, use, sell, offer for sale, import and otherwise run, modify and propagate the contents of its contributor version.

In the following three paragraphs, a “patent license” is any express agreement or commitment, however denominated, not to enforce a patent (such as an express permission to practice a patent or covenant not to sue for patent infringement). To “grant” such a patent license to a party means to make such an agreement or commitment not to enforce a patent against the party.

If you convey a covered work, knowingly relying on a patent license, and the Corresponding Source of the work is not available for anyone to copy, free of charge and under the terms of this License, through a publicly available network server or other readily accessible means, then you must either (1) cause the Corresponding Source to be so available, or (2) arrange to deprive yourself of the benefit of the patent license for this particular work, or (3) arrange, in a manner consistent with the requirements of this License, to extend the patent license to downstream recipients. “Knowingly relying” means you have actual knowledge that, but for the patent license, your conveying the covered work in a country, or your recipient's use of the covered work in a country, would infringe one or more identifiable patents in that country that you have reason to believe are valid.

If, pursuant to or in connection with a single transaction or arrangement, you convey, or propagate by procuring conveyance of, a covered work, and grant a patent license to some of the parties receiving the covered work authorizing them to use, propagate, modify or convey a specific copy of the covered work, then the patent license you grant is automatically extended to all recipients of the covered work and works based on it.

A patent license is “discriminatory” if it does not include within the scope of its coverage, prohibits the exercise of, or is conditioned on the non-exercise of one or more of the rights that are specifically granted under this License. You may not convey a covered work if you are a party to an arrangement with a third party that is in the business of distributing software, under which you make payment to the third party based on the extent of your activity of conveying the work, and under which the third party grants, to any of the parties who would receive the covered work from you, a discriminatory patent license (a) in connection with copies of the covered work conveyed by you (or copies made from those copies), or (b) primarily for and in connection with specific products or compilations that contain the covered work, unless you entered into that arrangement.

</details>

<style>

body {
  color: white;
  background: black;
}

img[alt=Server-Example] {
  align: center;
  height: 325px;
  margin-left: auto;
  margin-right: auto;
}

img[alt=Dedicated-Server-Example] {
  align: center;
  height: 325px;
  margin-left: auto;
  margin-right: auto;
}

img[alt=Header-Diagram] {
  /* display: block; */
  align: center;
  margin-left: auto;
  margin-right: auto;
}

</style>

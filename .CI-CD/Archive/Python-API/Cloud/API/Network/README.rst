python setup.py install

**Note that you will need the relevant developer tools for your platform**,
as netifaces is written in C and installing this way will compile the extension.

>>> import netifaces

>>> netifaces.interfaces()
['lo0', 'gif0', 'stf0', 'en0', 'en1', 'fw0']

You can ask for the addresses of a particular interface by doing

>>> netifaces.ifaddresses('lo0')
{18: [{'addr': ''}], 2: [{'peer': '127.0.0.1', 'netmask': '255.0.0.0', 'addr': '127.0.0.1'}], 30: [{'peer': '::1', 'netmask': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'addr': '::1'}, {'peer': '', 'netmask': 'ffff:ffff:ffff:ffff::', 'addr': 'fe80::1%lo0'}]}

Hmmmm.  That result looks a bit cryptic; let's break it apart and explain
what each piece means.  It returned a dictionary, so let's look there first::

  { 18: [...], 2: [...], 30: [...] }

Each of the numbers refers to a particular address family.  In this case, we
have three address families listed; on my system, 18 is ``AF_LINK`` (which means
the link layer interface, e.g. Ethernet), 2 is ``AF_INET`` (normal Internet
addresses), and 30 is ``AF_INET6`` (IPv6).

But wait!  Don't use these numbers in your code.  The numeric values here are
system dependent; fortunately, I thought of that when writing netifaces, so
the module declares a range of values that you might need.  e.g.

>>> netifaces.AF_LINK
18

Again, on your system, the number may be different.

So, what we've established is that the dictionary that's returned has one
entry for each address family for which this interface has an address.  Let's
take a look at the ``AF_INET`` addresses now:

>>> addrs = netifaces.ifaddresses('lo0')
>>> addrs[netifaces.AF_INET]
[{'peer': '127.0.0.1', 'netmask': '255.0.0.0', 'addr': '127.0.0.1'}]

You might be wondering why this value is a list.  The reason is that it's
possible for an interface to have more than one address, even within the
same family.  I'll say that again: *you can have more than one address of
the same type associated with each interface*.

*Asking for "the" address of a particular interface doesn't make sense.*

Right, so, we can see that this particular interface only has one address,
and, because it's a loopback interface, it's point-to-point and therefore
has a *peer* address rather than a broadcast address.

Let's look at a more interesting interface.

>>> addrs = netifaces.ifaddresses('en0')
>>> addrs[netifaces.AF_INET]
[{'broadcast': '10.15.255.255', 'netmask': '255.240.0.0', 'addr': '10.0.1.4'}, {'broadcast': '192.168.0.255', 'addr': '192.168.0.47'}]

This interface has two addresses (see, I told you...)  Both of them are
regular IPv4 addresses, although in one case the netmask has been changed
from its default.  The netmask *may not* appear on your system if it's set
to the default for the address range.

Because this interface isn't point-to-point, it also has broadcast addresses.

Now, say we want, instead of the IP addresses, to get the MAC address; that
is, the hardware address of the Ethernet adapter running this interface.  We
can do

>>> addrs[netifaces.AF_LINK]
[{'addr': '00:12:34:56:78:9a'}]

Note that this may not be available on platforms without getifaddrs(), unless
they happen to implement ``SIOCGIFHWADDR``.  Note also that you just get the
address; it's unlikely that you'll see anything else with an ``AF_LINK`` address.
Oh, and don't assume that all ``AF_LINK`` addresses are Ethernet; you might, for
instance, be on a Mac, in which case:

>>> addrs = netifaces.ifaddresses('fw0')
>>> addrs[netifaces.AF_LINK]
[{'addr': '00:12:34:56:78:9a:bc:de'}]

No, that isn't an exceptionally long Ethernet MAC address---it's a FireWire
address.

As of version 0.10.0, you can also obtain a list of gateways on your
machine:

>>> netifaces.gateways()
{2: [('10.0.1.1', 'en0', True), ('10.2.1.1', 'en1', False)], 30: [('fe80::1', 'en0', True)], 'default': { 2: ('10.0.1.1', 'en0'), 30: ('fe80::1', 'en0') }}

This dictionary is keyed on address family---in this case, ``AF_INET``---and
each entry is a list of gateways as ``(address, interface, is_default)`` tuples.
Notice that here we have two separate gateways for IPv4 (``AF_INET``); some
operating systems support configurations like this and can either route packets
based on their source, or based on administratively configured routing tables.

For convenience, we also allow you to index the dictionary with the special
value ``'default'``, which returns a dictionary mapping address families to the
default gateway in each case.  Thus you can get the default IPv4 gateway with

>>> gws = netifaces.gateways()
>>> gws['default'][netifaces.AF_INET]
('10.0.1.1', 'en0')

Do note that there may be no default gateway for any given address family;
this is currently very common for IPv6 and much less common for IPv4 but it
can happen even for ``AF_INET``.

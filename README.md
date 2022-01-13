# Intro
Site developers can use `/ipfs/<address>` and `/ipns/<address>` links by hosting in own domain, setting an IPFS gateway. But how can it be implemeted in ZeroNet?

# LinkIPFS
Resolves `/ipfs/<address>` and `/ipns/<address>` links in ZeroNet sites, redirecting to local IPFS gateway (if it's available via port 8080 and "always Tor mode" is not selected) or, alternatively, to [ipfs.io](https://ipfs.io).

Used [FilePack](https://github.com/HelloZeroNet/ZeroNet/tree/py3/plugins/FilePack) as an example.

# TODO
It should be build-in plugin in all mainstream ZeroNet forks.
Check links like /ipfs/<hash>/file.zip/1 and /ipfs/<hash>/.

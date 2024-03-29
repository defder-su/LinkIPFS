# Intro
Site developers can use `/ipfs/<address>` and `/ipns/<address>` links by hosting in own domain, setting an IPFS gateway. But how can it be implemeted in ZeroNet?

# LinkIPFS
Resolves `/ipfs/<address>` and `/ipns/<address>` links in ZeroNet sites.
For now, [beta release](https://github.com/defder-su/LinkIPFS/releases/tag/v0.1-redirector) just redirects such links.

# Development
Used [FilePack](https://github.com/HelloZeroNet/ZeroNet/tree/py3/plugins/FilePack) and [Cors](https://github.com/ZeroNetX/ZeroNet-Plugins/tree/master/Cors) as examples.

# TODO
- [ ] Proxy requests (not redirect), represent html pages inside Zero Frame, disabling AJAX
- [ ] Support `/raw/ipfs/<address>` and `/raw/ipns/<address>` links
- [ ] Read settings like `local_gateway_port`, `external_gateway` from `zeronet.conf` (section `ipfs`)
- [ ] Add visited resources to [MFS](https://docs.ipfs.io/concepts/file-systems/#mutable-file-system-mfs) `/ZeroNet`
- [ ] Support [MiceWeb](https://github.com/Robotizing/MiceWeb/) resolving system
- [ ] It should be built in all mainstream ZeroNet forks

# Discussions
- [Resolve /ipfs/<address> and /ipns/<address> links](https://github.com/ZeroNetX/ZeroNet/issues/134)
- [Lokinet for private transport](https://github.com/ipfs/notes/issues/431)
- [node-Tor is now open source in clear and modular](https://github.com/ipfs/ipfs/issues/439)
- [About images in blogs](http://127.0.0.1:43110/1MaQ4W5D6G52TpBfPACU9k9QcB1DxvHZ5v/?Post:35#Comments)

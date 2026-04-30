# Changelog

## 0.2.0 (2026-04-30)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/unlayer/unlayer-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** api update ([d8c02a2](https://github.com/unlayer/unlayer-python/commit/d8c02a28202f28aff216e1c51b4dc183bf758246))
* **internal:** implement indices array format for query and form serialization ([e8555c7](https://github.com/unlayer/unlayer-python/commit/e8555c785eb5ac3fd4f46eba86514c83279c8455))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([75acb50](https://github.com/unlayer/unlayer-python/commit/75acb50baa973b93439b0e1e803e34ec5ea0f891))
* **deps:** bump minimum typing-extensions version ([b7baa1e](https://github.com/unlayer/unlayer-python/commit/b7baa1e5d138b5a33b63bed9dae37bfabb6d968d))
* ensure file data are only sent as 1 parameter ([16c4a95](https://github.com/unlayer/unlayer-python/commit/16c4a958a038f89843bfd0287656f14c222bbc9a))
* **pydantic:** do not pass `by_alias` unless set ([d31637b](https://github.com/unlayer/unlayer-python/commit/d31637bd182be359df4af936cb715cc554d9a14b))
* sanitize endpoint path params ([bc0d6b6](https://github.com/unlayer/unlayer-python/commit/bc0d6b6b147d33cd2f65855284e7f435bdee09f9))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([9e8bba9](https://github.com/unlayer/unlayer-python/commit/9e8bba9900b5252766dae4d7cd835fb264136ed4))


### Chores

* **ci:** skip lint on metadata-only changes ([3343492](https://github.com/unlayer/unlayer-python/commit/33434927ad6ab7c508d758335944cdc4123a5e17))
* **ci:** skip uploading artifacts on stainless-internal branches ([907041a](https://github.com/unlayer/unlayer-python/commit/907041a9070f3c4a86605a21c9ab9a004a9bf553))
* **internal:** codegen related update ([c76b368](https://github.com/unlayer/unlayer-python/commit/c76b3685383f50f9446c8d0c6844aed7ad8f3696))
* **internal:** codegen related update ([d58e1b8](https://github.com/unlayer/unlayer-python/commit/d58e1b80f026a3fbb93c51e57af8afedcdb866e9))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([caea803](https://github.com/unlayer/unlayer-python/commit/caea803e4fc873ade6fbc9b9b66ff67938780f65))
* **internal:** more robust bootstrap script ([2543d0b](https://github.com/unlayer/unlayer-python/commit/2543d0b9a29711c39f5b8b5bfeac15dfc66b79b3))
* **internal:** tweak CI branches ([4e152dc](https://github.com/unlayer/unlayer-python/commit/4e152dccd0191c2dd4d321e8ca7b6550dc6bc3f0))
* **internal:** update gitignore ([5a510e6](https://github.com/unlayer/unlayer-python/commit/5a510e6edf2e26d612be067b6c95e70780d01d57))
* **test:** do not count install time for mock server timeout ([3ad7bbb](https://github.com/unlayer/unlayer-python/commit/3ad7bbb203d27a7b7f69fda2d0f3aebea329c49e))
* **tests:** bump steady to v0.19.4 ([775fe46](https://github.com/unlayer/unlayer-python/commit/775fe461f02f96ebc4b7cd6ff2d8cab4c52d291d))
* **tests:** bump steady to v0.19.5 ([9ef3615](https://github.com/unlayer/unlayer-python/commit/9ef3615041ea171a462a29f8cfd268133df0c6fc))
* **tests:** bump steady to v0.19.6 ([33d721e](https://github.com/unlayer/unlayer-python/commit/33d721e46826c23bf5b1ce78477d003cb9cd83da))
* **tests:** bump steady to v0.19.7 ([3d09621](https://github.com/unlayer/unlayer-python/commit/3d09621f6d61c74d431b9af1336c6c51d8396d4f))
* **tests:** bump steady to v0.20.1 ([649317d](https://github.com/unlayer/unlayer-python/commit/649317dda33455a5b5e25aedeb0210a746b767f2))
* **tests:** bump steady to v0.20.2 ([2c51cba](https://github.com/unlayer/unlayer-python/commit/2c51cba746385da9a9e5ec0ea00bf6c4cdee2bbd))
* **tests:** bump steady to v0.22.1 ([0a6f60a](https://github.com/unlayer/unlayer-python/commit/0a6f60a8acb8c85a937166884ba523cc59821b8f))


### Refactors

* **tests:** switch from prism to steady ([d2618bd](https://github.com/unlayer/unlayer-python/commit/d2618bd109fcd053b5845009bc8221090930a369))
* **types:** use `extra_items` from PEP 728 ([19677f4](https://github.com/unlayer/unlayer-python/commit/19677f4a04cd989500eecce93cbb0506cf1ebf32))

## 0.1.0 (2026-02-24)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/unlayer/unlayer-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** api update ([e247358](https://github.com/unlayer/unlayer-python/commit/e24735806fc790506d1d3b9ee84954809bd02258))
* **api:** api update ([1255c9b](https://github.com/unlayer/unlayer-python/commit/1255c9b3e6bd708eefb21313c022a1018a78fc3e))
* **api:** api update ([3901e44](https://github.com/unlayer/unlayer-python/commit/3901e44ec76d4bdc1ae8055639d1121965f8e6c6))
* **api:** api update ([e90df1d](https://github.com/unlayer/unlayer-python/commit/e90df1d06e53f40707ccc73610d797eaa3c51fa5))
* **api:** api update ([d0bb085](https://github.com/unlayer/unlayer-python/commit/d0bb0855866ba1daf54f700415c01fcf752090f3))
* **api:** api update ([39253ba](https://github.com/unlayer/unlayer-python/commit/39253ba25f6a5da8e18da9d564af41e0c7e4c0e7))
* **api:** api update ([b65e14e](https://github.com/unlayer/unlayer-python/commit/b65e14e7a19564d228e7436bae27b35a9ede6693))
* **api:** api update ([d83034d](https://github.com/unlayer/unlayer-python/commit/d83034df2dbb4dfc3ee96d101bcdce87dc66306f))
* **api:** api update ([93b319e](https://github.com/unlayer/unlayer-python/commit/93b319e21ac5f484c9d3efa4a51fba4269fe6737))
* **api:** api update ([dd927cc](https://github.com/unlayer/unlayer-python/commit/dd927cc54abf0b619091f71e91d778da87323043))
* **api:** api update ([1a2f183](https://github.com/unlayer/unlayer-python/commit/1a2f183e4fd9a9e512a41855aa1b91b4d28d6bdf))
* **api:** api update ([1cf5d8e](https://github.com/unlayer/unlayer-python/commit/1cf5d8e9a10c2b8684838fa628b1b864bbe74209))
* **api:** api update ([35876ba](https://github.com/unlayer/unlayer-python/commit/35876ba78ab506c86a36ae8aead33bf3f04549a6))
* **api:** api update ([eafe372](https://github.com/unlayer/unlayer-python/commit/eafe372ab530d1a516b6f88630060dd1e384a288))
* **api:** api update ([db50139](https://github.com/unlayer/unlayer-python/commit/db5013964e0c7efdc485708d622c12fde20c9420))
* **api:** api update ([37dfa82](https://github.com/unlayer/unlayer-python/commit/37dfa8228ed4158855318afb16b50dc71c78b1bb))
* **api:** api update ([04d7f14](https://github.com/unlayer/unlayer-python/commit/04d7f14ec06f71d777b7624b8898e3594dcb88f0))
* **api:** api update ([7dbfb1a](https://github.com/unlayer/unlayer-python/commit/7dbfb1aa7fa765b1750f6ed5a733f4cf584c9766))
* **api:** api update ([51ce8ef](https://github.com/unlayer/unlayer-python/commit/51ce8ef8927b0824ccd847e0acf61cd57388ae0f))
* **client:** add custom JSON encoder for extended type support ([16d4717](https://github.com/unlayer/unlayer-python/commit/16d4717e1dec685c212a6c7d74e969660cf7e03c))
* **client:** add support for binary request streaming ([191bd18](https://github.com/unlayer/unlayer-python/commit/191bd18a0c2588e3742b49b2bb85c23f31c18367))


### Bug Fixes

* use async_to_httpx_files in patch method ([f9bdb58](https://github.com/unlayer/unlayer-python/commit/f9bdb58b5c218d7310e8c3328fc79d2322bc7d24))


### Chores

* **ci:** upgrade `actions/github-script` ([89356cd](https://github.com/unlayer/unlayer-python/commit/89356cd10af2df4ce00e52b3857e772c2ffdda9f))
* configure new SDK language ([9596a35](https://github.com/unlayer/unlayer-python/commit/9596a35093e7c1a7bfb9c1a9da7319482ed4f9c8))
* format all `api.md` files ([eaab341](https://github.com/unlayer/unlayer-python/commit/eaab341586836de0b5d88ccd15ba91bf5d9fb8a9))
* **internal:** add `--fix` argument to lint script ([3402766](https://github.com/unlayer/unlayer-python/commit/340276634acd12227076b5b3fbc3a1d5a8aaaf2f))
* **internal:** add missing files argument to base client ([011c5b3](https://github.com/unlayer/unlayer-python/commit/011c5b3e1d285ad929aa23fbd18f22ded6e37bc2))
* **internal:** add request options to SSE classes ([8215016](https://github.com/unlayer/unlayer-python/commit/82150166172718373d5c625fcb2abd63b996d1c4))
* **internal:** bump dependencies ([4796143](https://github.com/unlayer/unlayer-python/commit/47961438c81e3263207987628d1f00c04a117189))
* **internal:** codegen related update ([d4e8db7](https://github.com/unlayer/unlayer-python/commit/d4e8db7de852054c9232097b80832e630383da0e))
* **internal:** fix lint error on Python 3.14 ([e825b41](https://github.com/unlayer/unlayer-python/commit/e825b41fa160ab18110a59b28ffdf3c504d63407))
* **internal:** make `test_proxy_environment_variables` more resilient ([17a5609](https://github.com/unlayer/unlayer-python/commit/17a5609325e6661d12910c96b3f41ecde33e5cf1))
* **internal:** update `actions/checkout` version ([942160b](https://github.com/unlayer/unlayer-python/commit/942160b8a331a9d21fe2349fba265fd6fb520034))
* speedup initial import ([a0429e9](https://github.com/unlayer/unlayer-python/commit/a0429e971dcf003df2bbfd2d523bea4aab46db76))
* update mock server docs ([e835dc3](https://github.com/unlayer/unlayer-python/commit/e835dc37eab896b138333888f423ba0aae6f0958))
* update SDK settings ([52e5d05](https://github.com/unlayer/unlayer-python/commit/52e5d054a25723d3798cd8a571cd48bc7625bce9))
* update SDK settings ([63ab6f7](https://github.com/unlayer/unlayer-python/commit/63ab6f7d4fee33593fe9d3dfb6daa615bc00897e))

# mediawiki_unembed

Expands embedded MediaWiki pages into full text

MediaWiki lets you embed pages into other pages, with code like:

```
{{:Page_title}}
```

This leads to great advances in modularity, but what if you want to recombine all of these embedded pages into one big page again? That's where mediawiki_unembed comes in. It'll go through your page recursively, so if you have pages embedded in pages embedded in pages, it'll spit out one big file in plain old wikitext format.

## Configuration

Edit mediawiki_unmbed.py and change base_url to your MediaWiki install

## Running it

From your command line:

To dump the wikitext straight to stdout:

```
mediawiki_unembed.py Page_title
```

To pipe the wikitext into a file

```
mediawiki_unembed.py Page_title > file.wikitext
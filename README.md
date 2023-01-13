# reversebibnames
Reverses names for BibTex (and Zotero).

It can be super annoying if Zotero does not get the names from a publication. Or when you manually need to add the authors names to your bib file.

See this article in the Financial times by [Owen Walker](https://www.ft.com/owen-walker), [Laura Noonan](https://www.ft.com/laura-noonan) and [Ian Smith](https://www.ft.com/ian-smith):

**[Bank of England criticises UK banks’ risk management systems](https://www.ft.com/content/4758200d-4356-47f8-a8c3-8eee21b79ba8)**

For BibTex you need the author names in reverse order, with `and` in between:

`Walker, Owen and Noonan, Laura and Smith, Ian`

For Zotero you need them stacked to enter them as a batch using the single field name switch:

`Owen, Walker` 

`Laura, Noonan` 

`Ian, Smith`

See this [link](https://forums.zotero.org/discussion/54351/inserting-batch-author-names/) for help on entering a batch of names in Zotero.

**This script sorts you out:**

All you need to do is entering this in a terminal:

`reversebibnames 'Owen Walker, Laura Noonan and Ian Smith'`

and presto. It will give you the all you need. Plus it copies the below to your clipboard for easy entry into Zotero. 

`Owen, Walker

`Laura, Noonan`

`Ian, Smith`

If you want the BibTex line copied to the clipboard use the `b` switch:

`reversebibnames b 'Owen Walker, Laura Noonan and Ian Smith'`

**Note**, to make this run from within any folder on your system, copy `reversebibnames.py`  to a path folder that Python scans when looking for executable files. In my case that is  `/usr/local/games`. Once copied into that folder, eliminate the extension: `'.py'`. 






















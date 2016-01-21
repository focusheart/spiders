# spiders

During working and learning, I write some spiders for specific usage. I want to make a collection here to keep all codes under management.

## Download ACM Paper (DAP)

We know that it's not good to download whole site, but somethings it's necessary to download a conference prceeding in order to print it. Read all of them on screen hurts my eyes a lot. I need a printed version. So, I must download all the PDF files. Obviously, click and save is very stupid. Spider is a right choice.

It's very easy to use, for example in the following. Attention, the url **MUST** include `prelayout=flat`:

    $ python dap.py -u http://dl.acm.org/citation.cfm?id=2724660&preflayout=flat


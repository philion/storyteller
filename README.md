# storyteller

Tinkering with text-to-speech (TTS) and how to get it to sound more like a human reader, who has to take breaths while speaking.

The intention for this code is to act a basis for a series of voice-based art projects demonstrating various ways voice can be incorporated into an interactive art project.

## Building

A [`Makefile`](Makefile) is included for common tasks.

    % make

Should build an VENV (in `/.env`), install the requirements and start running the main entry.

## Status

Current implementation, 0.0.1, uses [vosk](https://github.com/alphacep/vosk-api) and [pyttsx3](https://github.com/nateshmbhat/pyttsx3) 

## Notes

Some the of the specific ideas:
* A magical storyteller trapped in a mundane object, that can tell a story.
* Add simple controls of some kind, and a minimal display to select from many stories.
* Add voice recognition to:
  * Search for stories
  * Provide 'fact' evaluation (answer queries)
  * Interactive fiction
  
Challenges:
* speech: need to think about human speech and pauses and breathing, and build an SSML version to reflect.
  * could take advantage of mutiple voices on higher-end systems.
* ASR, high-quality voices and big knowledges bases don't fit on microelectronics.

Simple models include:
* Low-quality TTS with or w/o simple controls (my kindle could do that, but for story-ssml!) for feathers, picos, etc.
* Mid-quality ASR and TTS on a RasPi4 or CM4.
* High-quality TTS using cloud. ASR?

For now, focus on all-on-one RasPi running ASR -> IF7 -> TTS

### Experimenting with models

* Smallest
* Fastest
* Performant on RP4
* Service overview (local vs cloud)

### Experimenting with prosody/SSML

Generate SSML from text, html and markdown.

Source -> SSML -> Engine -> Audio

What engines support SSML?

Future of SSML: https://github.com/w3c/pronunciation/

## Related Projects

### Story Scraper
Scrapes a few categories in Gutenburg to generate a ZIM of all those stories. Focused on small/lean.

Starting catagories:
https://www.gutenberg.org/ebooks/bookshelf/20
https://www.gutenberg.org/ebooks/bookshelf/18
https://www.gutenberg.org/ebooks/bookshelf/216
https://www.gutenberg.org/ebooks/bookshelf/17
https://www.gutenberg.org/ebooks/bookshelf/218
https://www.gutenberg.org/ebooks/bookshelf/213

### Story Search
* Simple voice query (vosk)
* Local search for matching data (grep in py?)
* Present results as voice menu
* read selected story.


## Notes

* al.h - `/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/System/Library/Frameworks/OpenAL.framework/Headers`

## Z-Machine interpreter

forked from https://github.com/ravdin/zmachine

Python 3 implementation of a z-machine interpreter, for playing Infocom games. To play a z-machine file:

`python zmachine [GAME_FILE]`

The interpreter supports versions 3 and 4 (version 4 games include Trinity, AMFV, and Bureaucracy). Save files are in [Quetzal](http://inform-fiction.org/zmachine/standards/quetzal/index.html) format and should be compatible with the Frotz interpreter.

The original Zork trilogy (written by Tim Anderson, Marc Blank, Bruce Daniels, and Dave Lebling) is in the `games` directory.

### Further notes

The [Z-Machine Standards Document](https://www.inform-fiction.org/zmachine/standards/z1point1/index.html), by Graham Nelson, is an indispensable guide for decoding the z-machine instructions.

This space intentionally left blank.
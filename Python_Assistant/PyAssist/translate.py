def translate(input):
    import goslate
    if input.startswith("translate "):
        gs = goslate.Goslate()
        trans = input[10:-7]
        lang = input[-2:]
        print 'Translated: '+trans+' into '+lang
        print gs.translate(trans , lang)
    if 'languages' in input:
        gs = goslate.Goslate()
        print "I know a lot of languages, almost 90:  use the languages below and there key to translate: "
        espeak.synth("I know 90 languages")
        print gs.get_languages()

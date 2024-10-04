import spacy
import pytextrank

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("textrank")

example_text = """Mechanical processing
In mechanical processing, everything takes place that gives the desired result the necessary fine-tuning. We are at work for you with our own state-of-the-art machines.
We drill, turn, mill and leave nothing untouched that does not correspond one-to-one to your ideas of the planned casting.
To ensure that this is achieved in the most elegant way and with minimal time expenditure, we use CNC lathes and CNC milling machines as well as conventional processing machines in practice. This enables us to process all castings directly in our factory according to the respective requirements.
Our principle is to always manufacture to the highest standards. Precision and efficiency are therefore top priorities.
And if certain requirements are particularly complex, the further processing of the casting is carried out with special CNC machining centres. Here, 3D milling operations, which can process the geometry of the casting, as well as drilling and threading work, are carried out - and at maximum speed.

The advantage: Only a single clamping is necessary. A fact that accelerates processes immensely. By equipping ourselves with different tools, we are able to carry out one work step directly after the other, for example:

Machining of form and position tolerances with an accuracy of 1/100 mm
Manufacturing of fits up to H7
Thread production from M1 to M20 in all pitches
Milling of sealing grooves
Lathes with live tools
Also possible in our production:

Machine deburring or grinding in free form or according to contour
Carrying out pressure and leak tests
Assembly of assemblies
Pre-assembly of castings (use of threaded inserts, modular components or inlays)
As a result, thanks to modern mechanical processing, castings are manufactured and machined in a versatile way exactly as you want them to be: precise down to the last detail."""
doc = nlp(example_text)

for sent in doc._.textrank.summary(limit_phrases=2, limit_sentences=2):
    print(sent)
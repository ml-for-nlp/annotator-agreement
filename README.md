# Kappa agreement tutorial

Some intro to kappa with two little scripts to a) perform some annotation and b) calculate kappa over the produced annotation.

Before you start, find a friend to annotate with!

### Revising kappa

Here is some toy annotation produced for a Named Entity Recognition task by two coders, Kim and Sandy.

<table>
<tr><td></td><td>Kim</td><td>Sandy</td></tr>
<tr><td>Washington</td><td>PER</td><td>LOC</td></tr>
<tr><td>Italy</td><td>ORG</td><td>LOC</td></tr>
<tr><td>Einstein</td><td>PER</td><td>PER</td></tr>
<tr><td>Rovereto</td><td>LOC</td><td>LOC</td></tr>
<tr><td>Google</td><td>ORG</td><td>ORG</td></tr>
<tr><td>Jupiter</td><td>LOC</td><td>LOC</td></tr>
</table>

Manually calculate the kappa agreement between Kim and Sandy for this annotation. Then, check your answer by running the following:

    python3 kappa.py --test

Now, switch the first disagreement (Kim says LOC and Sandy says PER). Manually re-calculate. Do you get what you expected?


### Annotation

You are to perform some annotation which first involves reading a text and then answering some simple question about the person in the text.

Open the file Marie_Curie.txt in the data/ directory and read the text. Once you're done, run:

    python3 annotation.py

and follow the instructions. This will generate an annotation file containing your answers in the annotations/ folder.

Once you're done, have a look at the code in annotation.py. Explain the code with respect to producing reliable annotation. In particular, be sure to understand what shuffling does.


### Calculating kappa on your annotation

Informally compare your annotation to your partner's. To have the file sorted in the same order, you can do 

    cat annotations/[username].txt | sort | less

Get some intuition for how much agreement there is between you.

Now, exchange annotations with your partner. Both files should now be in your annotations folder. 

Run

    python3 kappa.py |less

Look at the output and check whether it agrees with your intuition. Also look at your disagreements, printed at the end of the output, and discuss your choices. Can you resolve the disagreements? (Please don't start a fight!)

Share your annotations with another group and see what happens when you have four coders.


### Adding 'fake' annotators

You can now experiment further with the properties of kappa by creating 'fake' annotators. Run annotation.py again and produce new files with various biases (for instance, an annotator who answered with the same class to all questions, or one who is in perfect agreement with another annotator). What happens? And what happens when you add/remove annotators from the annotations/ folder? 

NB: you can move an annotator 'out' by doing:

    mv annotations/[username].txt .

You can move the annotator 'back' by doing:

    mv [username].txt annotations/


### Did you spot the problem?

We calculated simple kappa over scores on a scale of 1-5. What do you think the problem is with this method?

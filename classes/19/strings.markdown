---
layout: slides
title: Character is ...
---
<section markdown="block" class="title-slide">
# Character is ...
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Character is a Number

__What are some ways to check if character is a number?__ &rarr;

<div markdown="block" class="incremental">

* use isdigit()
* check if character in "0123456789"

{% highlight python %}
"a".isdigit()
"1".isdigit()
"a" in "0123456789"
"1" in "0123456789"
{% endhighlight %}


</div>

</section>

<section markdown="block">
### Character is a Vowel

__What are some ways to check if character is a vowel?__ &rarr;


<div markdown="block" class="incremental">

* check if character in "AEIOUaeiou"
* ch in "AEUIOIaeiou"

</div>

</section>

<section markdown="block">
### An Example

Write a function that counts the number of characters in a word that are either a vowel or a number:

{% highlight python %}
def count_vowels_numbers(word):
	count = 0
	for ch in word:
		if ch.isdigit() or ch in "AEIOUaeiou":
			count += 1
	return count
{% endhighlight %}
</section>


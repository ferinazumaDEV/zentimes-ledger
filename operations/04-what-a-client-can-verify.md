# What a client can verify on their own

> Everything on this list is checked from outside, with no access to anything of ours and without taking our word for it.

1. **That the inspector says the same as the recipe.** Every inspector metric that corresponds to a cookbook recipe carries its identifier (`words_visible_no_js`, `typed_entities`, `ai_user_agents_allowed`, `llms_txt_bytes`) in the HTML as `data-metric` and `data-value`. Run the recipe of the stated version on the same URL and the numbers have to match. If they do not match, the inspector is wrong, not the recipe.
2. **That every published command reproduces its figure.** Next to every data point there is a `curl` command. Copy it, run it, and the same number has to come out. If it does not, the error is ours.
3. **That the rating rules are the published ones.** Every label carries in writing the rule that decides it and the criteria version. It can be checked by hand whether the page meets, or not, what the rule says.
4. **That the criteria are not changed on the sly.** The criteria history is on the inspector page. A label can change without the site changing, and when that happens, the history says which rule changed and why.
5. **That the site practises what it preaches.** The inspector can be run on zentimes.es. Today it does not score "excellent" on everything, and the reasons are in the history.
6. **That the sources exist.** The claims in the notes and the frequently asked questions link to their source; the glossary's `sameAs` were checked one by one. Anyone can open them.
7. **That nothing is promised that is not measured.** No page claims that an AI will cite anyone, and the inspector says so explicitly: no check measures citation.
